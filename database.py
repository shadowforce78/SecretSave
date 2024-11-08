# database.py - Database operations
import json
import os


class DatabaseManager:
    def __init__(self, db_file="data.json"):
        self.db_file = db_file

    def refresh_data(self):
        """Recharge les données depuis le fichier JSON."""
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                return json.load(f)
        return {}

    def register_user(self, uuid, password):
        data = {uuid: {"password": {"pwd": password}}}
        db = self.refresh_data()

        if uuid in db:
            return False  # L'utilisateur existe déjà
        db.update(data)

        with open(self.db_file, "w") as f:
            json.dump(db, f, indent=4)
        return True

    def verify_login(self, uuid, password):
        db = self.refresh_data()

        if uuid in db and db[uuid]["password"]["pwd"] == password:
            site_names = self.get_site_names(uuid)
            return True, site_names
        return False, []

    def get_site_names(self, uuid):
        db = self.refresh_data()
        site_names = []

        if uuid in db:
            for key in db[uuid].keys():
                if key != "password":
                    site_names.append(key)
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

        with open(self.db_file, "w") as f:
            json.dump(db, f, indent=4)
            
    def delete_data(self, site_name, uuid):
        db = self.refresh_data()

        if uuid in db and site_name in db[uuid]:
            del db[uuid][site_name]

            with open(self.db_file, "w") as f:
                json.dump(db, f, indent=4)
                return True
        return False