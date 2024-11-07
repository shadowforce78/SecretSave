# database.py - Database operations
import json
import os

class DatabaseManager:
    def __init__(self, db_file="data.json"):
        self.db_file = db_file
    
    def register_user(self, uuid, password):
        data = {uuid: {"password": {"pwd": password}}}
        
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                db = json.load(f)
            if uuid in db:
                return False
            db.update(data)
            with open(self.db_file, "w") as f:
                json.dump(db, f, indent=4)
        else:
            with open(self.db_file, "w") as f:
                json.dump(data, f, indent=4)
        return True
    
    def verify_login(self, uuid, password):
        if not os.path.exists(self.db_file):
            return False, []
            
        with open(self.db_file, "r") as f:
            db = json.load(f)
            
        for key, value in db.items():
            if key == uuid and value["password"]["pwd"] == password:
                site_names = self.get_site_names(db, key)
                return True, site_names
        return False, []
    
    def get_site_names(self, data, uuid):
        site_names = []
        for key, value in data[uuid].items():
            if key != "password":
                site_names.append(value.get('title'))
        return site_names
    
    def get_site_info(self, site_name):
        with open(self.db_file, "r") as f:
            db = json.load(f)
        site_info = []
        for uuid, entries in db.items():
            for key, value in entries.items():
                if key != "password" and value.get("title") == site_name:
                    site_info.append({
                        "url": value["url"],
                        "username": value["mail_username"],
                        "password": value["password"]
                    })
        return site_info
