# utils.py - Utility functions for encryption and UUID management
import os
import uuid
from cryptography.fernet import Fernet

class CryptoManager:
    def __init__(self):
        self.key_file = "key.key" if os.name == "nt" else ".key.key"
        self.uuid_file = "uuid.txt" if os.name == "nt" else ".uuid.txt"
        
    def generate_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            if os.name == "nt":
                os.system(f"attrib +h {self.key_file}")
            return True
        return False

    def load_key(self):
        with open(self.key_file, "rb") as f:
            return f.read()
    
    def create_uuid(self):
        self.generate_key()
        key = self.load_key()
        cipher = Fernet(key)

        if not os.path.exists(self.uuid_file):
            my_uuid = uuid.uuid4()
            encrypted_uuid = cipher.encrypt(str(my_uuid).encode())
            with open(self.uuid_file, "wb") as f:
                f.write(encrypted_uuid)
            if os.name == "nt":
                os.system(f"attrib +h {self.uuid_file}")
            return True
        return False
    
    def decrypt_uuid(self):
        key = self.load_key()
        cipher = Fernet(key)
        with open(self.uuid_file, "rb") as f:
            encrypted_uuid = f.read()
        return cipher.decrypt(encrypted_uuid).decode()
