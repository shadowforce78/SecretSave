import customtkinter as ctk
from ui import UserInterface
from utils import CryptoManager
from database import DatabaseManager
import threading
from flask import Flask
import pystray
from PIL import Image, ImageDraw

# Initialiser Flask pour le serveur
appF = Flask(__name__)


@appF.route("/")
def get_data():
    html = """
    <h1> Password Manager </h1>
    """
    return html


class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.ui = UserInterface(root)
        self.crypto = CryptoManager()
        self.db = DatabaseManager()
        self.uuid = None

    def start(self):
        # Initialiser l'UUID et lancer le menu principal
        self.crypto.create_uuid()
        self.uuid = self.crypto.decrypt_uuid()
        self.ui.main_menu(
            self.handle_login,
            self.handle_registration,
            self.exit_app,
            self.handle_reset_data,
        )

    def handle_login(self):
        # Afficher le menu de connexion
        self.ui.login_menu(self.verify_login, self.show_main_menu)

    def handle_registration(self):
        # Afficher le menu d'inscription
        self.ui.register_menu(self.register_user, self.show_main_menu)

    def show_main_menu(self):
        # Retourner au menu principal
        self.ui.main_menu(
            self.handle_login,
            self.handle_registration,
            self.exit_app,
            self.handle_reset_data,
        )

    def verify_login(self, password):
        # Vérifier les identifiants pour la connexion
        login_success, _ = self.db.verify_login(self.uuid, password)
        if login_success:
            self.show_logged_in_menu()
        else:
            ctk.CTkLabel(
                self.ui.root, text="Invalid credentials!", text_color="red"
            ).pack()

    def register_user(self, password):
        # Inscription d'un nouvel utilisateur
        if self.db.register_user(self.uuid, password):
            ctk.CTkLabel(
                self.ui.root, text="Registration successful!", text_color="green"
            ).pack()
            self.show_main_menu()
        else:
            ctk.CTkLabel(
                self.ui.root, text="User already exists!", text_color="red"
            ).pack()

    def show_logged_in_menu(self):
        # Menu après connexion
        self.ui.logged_menu(
            self.show_sites,
            self.show_add_site_form,
            self.show_delete_site_form,
            self.show_main_menu,
        )

    def show_sites(self):
        # Afficher les sites sauvegardés
        site_names = self.db.get_site_names(self.uuid)
        self.ui.show_sites_menu(
            site_names, self.show_site_info, self.show_logged_in_menu
        )

    def show_site_info(self, site_name):
        # Afficher les informations du site sélectionné
        site_info = self.db.get_site_info(site_name)
        self.ui.show_site_info(site_name, site_info, self.show_sites)

    def show_add_site_form(self):
        # Appeler le formulaire d'ajout de site de l'interface UI
        self.ui.add_site(self.add_site, self.show_logged_in_menu)

    def add_site(self, site_name, url, mail_username, password):
        # Ajouter un nouveau site après avoir obtenu les valeurs
        info = [site_name, url, mail_username, password]
        self.db.add_data(info, self.uuid)
        self.show_logged_in_menu()

    def show_delete_site_form(self):
        # Appeler le formulaire de suppression de site de l'interface UI
        site_names = self.db.get_site_names(self.uuid)
        self.ui.delete_site(site_names, self.delete_site, self.show_logged_in_menu)

    def delete_site(self, site_name):
        # Supprimer un site
        self.db.delete_data(site_name, self.uuid)
        self.show_logged_in_menu()

    def handle_reset_data(self):
        # Réinitialiser les données
        self.ui.reset_data_confirmation(self.db.reset_data, self.show_main_menu)

    def exit_app(self):
        # Quitter proprement
        icon.stop()  # Arrêter l'icône système
        self.root.destroy()  # Fermer l'interface Tkinter


# Démarre le serveur Flask dans un thread séparé
def start_server():
    appF.run(host="localhost", port=63246)


# Fonction pour créer l'icône système
def create_icon():
    image = Image.new("RGB", (64, 64), color="blue")
    d = ImageDraw.Draw(image)
    d.ellipse((16, 16, 48, 48), fill="white")
    return image


# Fonction pour afficher/masquer la fenêtre principale
def toggle_visibility():
    if root.state() == "normal":
        root.withdraw()  # Masquer la fenêtre
    else:
        root.deiconify()  # Afficher la fenêtre


# Fonction pour quitter l'icône système proprement
def quit_app(icon, item):
    icon.stop()
    root.quit()


if __name__ == "__main__":
    # Lancer le serveur Flask dans un thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Initialiser CustomTkinter et lancer l'application
    root = ctk.CTk()
    root.geometry("400x400")
    root.title("Password Manager")
    app = PasswordManager(root)
    app.start()

    # Configuration de l'icône de tray
    icon = pystray.Icon(
        "PasswordManager",
        create_icon(),
        menu=pystray.Menu(
            pystray.MenuItem(
                "Afficher/Masquer", lambda icon, item: toggle_visibility()
            ),
            pystray.MenuItem("Quitter", quit_app),
        ),
    )

    # Redéfinir l'action de fermeture de la fenêtre
    root.protocol("WM_DELETE_WINDOW", lambda: root.withdraw())

    # Lancer l'icône de tray dans un thread
    icon_thread = threading.Thread(target=icon.run)
    icon_thread.daemon = True
    icon_thread.start()

    # Lancer l'application Tkinter
    root.mainloop()
