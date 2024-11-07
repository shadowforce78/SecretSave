import simple_chalk as chalk
import json
import os
import uuid
from cryptography.fernet import Fernet

dbFile = "data.json"
uuidFile = "uuid.txt"


def generateKey():
    keyFile = "key.key"
    if not os.path.exists(keyFile):
        key = Fernet.generate_key()
        with open(keyFile, "wb") as f:
            f.write(key)
        print(chalk.green("Encryption key generated!"))
    else:
        print(chalk.blue("Encryption key already exists!"))


def createUUID():
    generateKey()
    with open("key.key", "rb") as f:
        key = f.read()
    cipher = Fernet(key)

    if os.path.exists(uuidFile):
        print(chalk.blue("UUID already exists!"))
    else:
        myuuid = uuid.uuid4()
        encrypted_uuid = cipher.encrypt(str(myuuid).encode())
        with open(uuidFile, "wb") as f:
            f.write(encrypted_uuid)
        print(chalk.green("Encrypted UUID created successfully!"))
        if os.name == "nt":
            os.system(f"attrib +h {uuidFile}")
        else:
            os.rename(uuidFile, f".{uuidFile}")


def mainMenu():
    print(chalk.yellow("Main Menu"))
    print(chalk.green("1. Login"))
    print(chalk.green("2. Register"))
    print(chalk.red("3. Exit"))


def registerMenu():
    print(chalk.yellow("Register Menu"))
    print(chalk.green("1. Register"))
    print(chalk.red("2. Back"))


def loginMenu():
    print(chalk.yellow("Login Menu"))
    print(chalk.green("1. Login"))
    print(chalk.red("2. Back"))


def register(uuid):
    username = input("Enter username: ")
    password = input("Enter password: ")
    data = {uuid: {"password": {"pwd": password}}}

    if os.path.exists(dbFile):
        with open(dbFile, "r") as f:
            db = json.load(f)
        db.update(data)
        with open(dbFile, "w") as f:
            json.dump(db, f, indent=4)
    else:
        with open(dbFile, "w") as f:
            json.dump(data, f, indent=4)


def login(uuid):
    password = input("Enter password: ")

    if not os.path.exists(dbFile):
        print(chalk.red("No user registered!"))
        return

    with open(dbFile, "r") as f:
        db = json.load(f)

    for key, value in db.items():
        if key == uuid and value["password"]["pwd"] == password:
            print(chalk.green("Login successful!"))
            read_data_from_json(db)
            break
    else:
        print(chalk.red("Invalid credentials!"))


def read_data_from_json(data):
    print("\033[H\033[J")
    for uuid, entries in data.items():
        for key, value in entries.items():
            if key != "password":
                print(value.get("title"))


def main():
    while True:
        mainMenu()
        UUID = decryptUUID()
        print(chalk.blue(f"UUID: {UUID}"))

        choice = input("Enter your choice: ")
        if choice == "1":

            print("\033[H\033[J")
            loginMenu()
            choice = input("Enter your choice: ")
            if choice == "1":
                print("\033[H\033[J")
                login(UUID)
            elif choice == "2":
                continue
            else:
                print(chalk.red("Invalid choice!"))
        elif choice == "2":
            print("\033[H\033[J")
            registerMenu()
            choice = input("Enter your choice: ")
            if choice == "1":
                print("\033[H\033[J")
                register(UUID)
            elif choice == "2":
                continue
            else:
                print(chalk.red("Invalid choice!"))
        elif choice == "3":
            break
        else:
            print(chalk.red("Invalid choice!"))


def decryptUUID():
    if os.name == "nt":
        uuidFile = "uuid.txt"
    else:
        uuidFile = ".uuid.txt"
    with open("key.key", "rb") as f:
        key = f.read()
    cipher = Fernet(key)
    with open(f"{uuidFile}", "rb") as f:
        encrypted_uuid = f.read()
    uuid = cipher.decrypt(encrypted_uuid).decode()
    return uuid
