# # database.py - Database operations
import json
import os
class DatabaseManager:
    def __init__(self, db_file="data.json"):
        self.db_file = db_file
        self.db = self.refresh_data()  # Initialise les données au lancement

    def refresh_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                return json.load(f)
        return {}

    def register_user(self, uuid, password):
        self.db = self.refresh_data()  # Rafraîchit les données
        data = {uuid: {"password": {"pwd": password}}}

        if uuid in self.db:
            return False

        self.db.update(data)
        with open(self.db_file, "w") as f:
            json.dump(self.db, f, indent=4)
        return True

    def verify_login(self, uuid, password):
        self.db = self.refresh_data()  # Rafraîchit les données
        if uuid in self.db and self.db[uuid]["password"]["pwd"] == password:
            site_names = self.get_site_names(uuid)
            return True, site_names
        return False, []

    def get_site_names(self, uuid):
        self.db = self.refresh_data()  # Rafraîchit les données
        site_names = [
            key for key in self.db.get(uuid, {}) if key != "password"
        ]
        return site_names

    def get_site_info(self, site_name):
        self.db = self.refresh_data()  # Rafraîchit les données
        site_info = []

        for uuid, entries in self.db.items():
            if site_name in entries and site_name != "password":
                site_data = entries[site_name]
                site_info.append({
                    "url": site_data.get("url", "N/A"),  # Utilise "N/A" si manquant
                    "mail_username": site_data.get("mail_username", "N/A"),
                    "password": site_data.get("password", "N/A"),
                })

        return site_info


    def add_data(self, info, uuid):
        self.db = self.refresh_data()  # Rafraîchit les données
        site_name, url, mail_username, password = info
        new_entry = {
            site_name: {
                "url": url,
                "mail_username": mail_username,
                "password": password,
            }
        }

        if uuid not in self.db:
            self.db[uuid] = {}

        self.db[uuid].update(new_entry)

        with open(self.db_file, "w") as f:
            json.dump(self.db, f, indent=4)
