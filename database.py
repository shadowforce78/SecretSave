# # database.py - Database operations
import json
import os
from cryptography.fernet import Fernet

class DatabaseManager:
    def __init__(self, db_file="data.json", key_file="key.key"):
        self.db_file = db_file
        self.key_file = key_file
        self.key = self.load_or_create_key()
        self.cipher = Fernet(self.key)

    def load_or_create_key(self):
        # Génère une clé de chiffrement si elle n'existe pas encore
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
            return key
        # Charge la clé existante
        with open(self.key_file, "rb") as key_file:
            return key_file.read()

    def refresh_data(self):
        """Recharge et déchiffre les données depuis le fichier JSON."""
        if os.path.exists(self.db_file):
            with open(self.db_file, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = self.cipher.decrypt(encrypted_data).decode()
            return json.loads(decrypted_data)
        return {}

    def save_data(self, data):
        """Chiffre et sauvegarde les données dans le fichier JSON."""
        json_data = json.dumps(data).encode()
        encrypted_data = self.cipher.encrypt(json_data)
        with open(self.db_file, "wb") as f:
            f.write(encrypted_data)

    def register_user(self, uuid, password):
        db = self.refresh_data()
        if uuid in db:
            return False  # L'utilisateur existe déjà
        db[uuid] = {"password": {"pwd": password}}
        self.save_data(db)
        return True

    def verify_login(self, uuid, password):
        db = self.refresh_data()
        if uuid in db and db[uuid]["password"]["pwd"] == password:
            site_names = self.get_site_names(uuid)
            return True, site_names
        return False, []

    def get_site_names(self, uuid):
        db = self.refresh_data()
        site_names = [key for key in db.get(uuid, {}) if key != "password"]
        return site_names

    def get_site_info(self, site_name):
        db = self.refresh_data()
        site_info = []
        for uuid, entries in db.items():
            if site_name in entries and site_name != "password":
                site_data = entries[site_name]
                site_info.append({
                    "url": site_data.get("url", "N/A"),
                    "mail_username": site_data.get("mail_username", "N/A"),
                    "password": site_data.get("password", "N/A"),
                })
        return site_info

    def add_data(self, info, uuid):
        db = self.refresh_data()
        site_name, url, mail_username, password = info
        new_entry = {
            site_name: {
                "url": url,
                "mail_username": mail_username,
                "password": password,
            }
        }
        if uuid not in db:
            db[uuid] = {}
        db[uuid].update(new_entry)
        self.save_data(db)

    def delete_data(self, site_name, uuid):
        db = self.refresh_data()
        if uuid in db and site_name in db[uuid]:
            del db[uuid][site_name]
            self.save_data(db)
            return True
        return False