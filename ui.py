# ui.py - User interface class using CustomTkinter
import customtkinter as ctk


class UserInterface:
    def __init__(self, root):
        self.root = root

    def main_menu(self, login_callback, register_callback, exit_callback):
        # Effacer l'écran
        self.clear_screen()

        # Titre
        title_label = ctk.CTkLabel(self.root, text="Main Menu", font=("Arial", 20))
        title_label.pack(pady=20)

        # Boutons du menu principal
        login_button = ctk.CTkButton(self.root, text="Login", command=login_callback)
        login_button.pack(pady=10)

        register_button = ctk.CTkButton(
            self.root, text="Register", command=register_callback
        )
        register_button.pack(pady=10)

        exit_button = ctk.CTkButton(self.root, text="Exit", command=exit_callback)
        exit_button.pack(pady=10)

    def login_menu(self, login_submit_callback, back_callback):
        # Effacer l'écran
        self.clear_screen()

        # Titre
        title_label = ctk.CTkLabel(self.root, text="Login Menu", font=("Arial", 20))
        title_label.pack(pady=20)

        # Entrée de mot de passe
        password_entry = ctk.CTkEntry(
            self.root, placeholder_text="Enter your password", show="*"
        )
        password_entry.pack(pady=10)

        # Bouton de soumission
        submit_button = ctk.CTkButton(
            self.root,
            text="Login",
            command=lambda: login_submit_callback(password_entry.get()),
        )
        submit_button.pack(pady=10)

        # Bouton retour
        back_button = ctk.CTkButton(self.root, text="Back", command=back_callback)
        back_button.pack(pady=10)

    def register_menu(self, register_submit_callback, back_callback):
        # Effacer l'écran
        self.clear_screen()

        # Titre
        title_label = ctk.CTkLabel(self.root, text="Register Menu", font=("Arial", 20))
        title_label.pack(pady=20)

        # Entrée de mot de passe
        password_entry = ctk.CTkEntry(
            self.root, placeholder_text="Set a password", show="*"
        )
        password_entry.pack(pady=10)

        # Bouton de soumission
        submit_button = ctk.CTkButton(
            self.root,
            text="Register",
            command=lambda: register_submit_callback(password_entry.get()),
        )
        submit_button.pack(pady=10)

        # Bouton retour
        back_button = ctk.CTkButton(self.root, text="Back", command=back_callback)
        back_button.pack(pady=10)

    def logged_menu(
        self,
        show_sites_callback,
        add_site_callback,
        delete_site_callback,
        logout_callback,
    ):
        # Effacer l'écran
        self.clear_screen()

        # Titre
        title_label = ctk.CTkLabel(self.root, text="Logged in Menu", font=("Arial", 20))
        title_label.pack(pady=20)

        # Boutons de menu
        show_sites_button = ctk.CTkButton(
            self.root, text="Show Sites", command=show_sites_callback
        )
        show_sites_button.pack(pady=10)

        add_site_button = ctk.CTkButton(
            self.root, text="Add Site", command=add_site_callback
        )
        add_site_button.pack(pady=10)

        delete_site_button = ctk.CTkButton(
            self.root, text="Delete Site", command=delete_site_callback
        )
        delete_site_button.pack(pady=10)

        logout_button = ctk.CTkButton(self.root, text="Logout", command=logout_callback)
        logout_button.pack(pady=10)

    def show_sites_menu(self, site_names, site_select_callback, back_callback):
        # Effacer l'écran
        self.clear_screen()

        # Titre
        title_label = ctk.CTkLabel(self.root, text="Your Sites", font=("Arial", 20))
        title_label.pack(pady=20)

        # Liste des sites
        for site in site_names:
            site_button = ctk.CTkButton(
                self.root, text=site, command=lambda s=site: site_select_callback(s)
            )
            site_button.pack(pady=5)

        # Bouton retour
        back_button = ctk.CTkButton(self.root, text="Back", command=back_callback)
        back_button.pack(pady=10)

    def show_site_info(self, site_name, site_info, back_callback):
        # Effacer l'écran
        self.clear_screen()

        # Affichage des informations du site
        title_label = ctk.CTkLabel(
            self.root, text=f"Site: {site_name}", font=("Arial", 20)
        )
        title_label.pack(pady=20)

        for info in site_info:
            url_label = ctk.CTkLabel(self.root, text=f"URL: {info.get('url', 'N/A')}")
            url_label.pack(pady=5)

            username_label = ctk.CTkLabel(
                self.root, text=f"Username: {info.get('mail_username', 'N/A')}"
            )
            username_label.pack(pady=5)

            password_label = ctk.CTkLabel(
                self.root, text=f"Password: {info.get('password', 'N/A')}"
            )
            password_label.pack(pady=5)

        # Bouton retour
        back_button = ctk.CTkButton(self.root, text="Back", command=back_callback)
        back_button.pack(pady=10)

    def add_site(self, submit_callback, back_callback):
        # Effacer l'écran
        self.clear_screen()

        # Titre
        title_label = ctk.CTkLabel(self.root, text="Add New Site", font=("Arial", 20))
        title_label.pack(pady=20)

        # Champs de formulaire
        site_name_entry = ctk.CTkEntry(self.root, placeholder_text="Site Name")
        site_name_entry.pack(pady=5)

        url_entry = ctk.CTkEntry(self.root, placeholder_text="Site URL")
        url_entry.pack(pady=5)

        username_entry = ctk.CTkEntry(self.root, placeholder_text="Email/Username")
        username_entry.pack(pady=5)

        password_entry = ctk.CTkEntry(self.root, placeholder_text="Password", show="*")
        password_entry.pack(pady=5)

        # Bouton de soumission
        submit_button = ctk.CTkButton(
            self.root,
            text="Save",
            command=lambda: submit_callback(
                site_name_entry.get(),
                url_entry.get(),
                username_entry.get(),
                password_entry.get(),
            ),
        )
        submit_button.pack(pady=10)

        # Bouton retour
        back_button = ctk.CTkButton(self.root, text="Back", command=back_callback)
        back_button.pack(pady=10)

    def delete_site(self, site_names, delete_callback, back_callback):
        # Effacer l'écran
        self.clear_screen()

        # Titre
        title_label = ctk.CTkLabel(self.root, text="Delete Site", font=("Arial", 20))
        title_label.pack(pady=20)

        # Boutons de choix des sites
        for site in site_names:
            site_button = ctk.CTkButton(
                self.root, text=site, command=lambda s=site: delete_callback(s)
            )
            site_button.pack(pady=5)

        # Bouton retour
        back_button = ctk.CTkButton(self.root, text="Back", command=back_callback)
        back_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
