# ui.py - User interface functions
from simple_chalk import chalk

class UserInterface:
    @staticmethod
    def clear_screen():
        print("\033[H\033[J")
    
    @staticmethod
    def main_menu():
        print(chalk.yellow("Main Menu"))
        print(chalk.green("1. Login"))
        print(chalk.green("2. Register"))
        print(chalk.red("3. Exit"))
    
    @staticmethod
    def login_menu():
        print(chalk.yellow("Login Menu"))
        print(chalk.green("1. Login"))
        print(chalk.red("2. Back"))
    
    @staticmethod
    def register_menu():
        print(chalk.yellow("Register Menu"))
        print(chalk.green("1. Register"))
        print(chalk.red("2. Back"))
    
    @staticmethod
    def show_sites_menu(site_names):
        print(chalk.yellow("Sites"))
        for i, site in enumerate(site_names):
            print(chalk.blue(f"{i + 1}. {site}"))
        print(chalk.red("q. Back"))
    
    @staticmethod
    def show_site_info(site_name, site_info):
        print(chalk.yellow(f"Site: {site_name}"))
        for info in site_info:
            print(chalk.blue(f"URL: {info['url']}"))
            print(chalk.blue(f"Username: {info['username']}"))
            print(chalk.blue(f"Password: {info['password']}"))
            
            
    @staticmethod
    def logged_menu():
        print(chalk.yellow("Logged in"))
        print(chalk.green("1. Show sites"))
        print(chalk.green("2. Add site"))
        print(chalk.green("3. Delete site"))
        print(chalk.red("4. Logout"))