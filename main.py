# main.py - Main application file
from ui import UserInterface
from utils import CryptoManager
from database import DatabaseManager
import simple_chalk as chalk


class PasswordManager:
    def __init__(self):
        self.ui = UserInterface()
        self.crypto = CryptoManager()
        self.db = DatabaseManager()

    def start(self):
        self.crypto.create_uuid()
        self.main_loop()

    def main_loop(self):
        while True:
            self.ui.clear_screen()
            self.ui.main_menu()
            uuid = self.crypto.decrypt_uuid()
            print(chalk.blue(f"UUID: {uuid}"))

            choice = input("Enter your choice: ")

            if choice == "1":
                self.handle_login(uuid)
            elif choice == "2":
                self.handle_registration(uuid)
            elif choice == "3":
                break
            else:
                print(chalk.red("Invalid choice!"))

    def handle_login(self, uuid):
        self.ui.clear_screen()
        self.ui.login_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            self.ui.clear_screen()
            password = input("Enter password: ")
            login_success, _ = self.db.verify_login(uuid, password)

            if login_success:
                self.logged_in_menu(uuid)  # Passer uniquement uuid ici
            else:
                print(chalk.red("Invalid credentials!"))
        elif choice != "2":
            print(chalk.red("Invalid choice!"))

    def handle_registration(self, uuid):
        self.ui.clear_screen()
        self.ui.register_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            self.ui.clear_screen()
            password = input("Enter password: ")
            if self.db.register_user(uuid, password):
                print(chalk.green("Registration successful!"))
            else:
                print(chalk.red("User already exists!"))
        elif choice != "2":
            print(chalk.red("Invalid choice!"))

    def logged_in_menu(self, uuid):
        while True:
            self.ui.clear_screen()
            self.ui.logged_menu()
            
            # Recharger `site_names` pour afficher les données actualisées
            site_names = self.db.get_site_names(uuid)
            
            choice = input("Enter your choice: ")
            if choice == "1":
                self.show_site(site_names)
            elif choice == "2":
                info = self.ui.add_site()
                self.db.add_data(info, uuid)
            elif choice == "3":
                self.ui.show_sites_to_delete(site_names)
                site_to_delete = self.ui.delete_site()
                self.db.delete_data(site_to_delete, uuid)
            elif choice == "4":
                break
            else:
                print(chalk.red("Invalid choice!"))

    def show_site(self, site_names):
        while True:
            self.ui.clear_screen()
            self.ui.show_sites_menu(site_names)

            choice = input("Enter your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= len(site_names):
                site_name = site_names[int(choice) - 1]
                self.ui.clear_screen()
                site_info = self.db.get_site_info(site_name)
                self.ui.show_site_info(site_name, site_info)
                input(chalk.green("Press Enter to go back..."))
            elif choice.lower() == "q":
                break
            else:
                print(chalk.red("Invalid choice!"))


if __name__ == "__main__":
    app = PasswordManager()
    app.start()
