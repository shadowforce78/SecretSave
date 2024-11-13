# server.py - Flask server to manage UUIDs and site information
from flask import Flask, request
from utils import CryptoManager
from database import DatabaseManager

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Initialisation des chemins de fichiers
keyFile = "key.key"
uuidFile = "uuid.txt"
dataFile = "data.json"

# Initialiser le gestionnaire de crypto et la base de données
crypto_manager = CryptoManager()
database_manager = DatabaseManager()

def get_html_template():
    """Template HTML principal pour la page."""
    return """
    <html>
        <head>
            <title>UUID Manager</title>
            <style>
                h1 {{ text-align: center; }}
                form, p {{ text-align: center; }}
                select {{ width: 200px; margin-bottom: 10px; }}
                .modal {{
                    display: none;
                    position: fixed;
                    z-index: 1;
                    left: 0; top: 0;
                    width: 100%; height: 100%;
                    overflow: auto; background-color: rgba(0,0,0,0.4);
                    padding-top: 60px;
                }}
                .modal-content {{ background-color: #fefefe; margin: 5% auto; padding: 20px; border: 1px solid #888; width: 80%; }}
                .close {{ color: #aaa; float: right; font-size: 28px; font-weight: bold; cursor: pointer; }}
                .close:hover {{ color: black; }}
            </style>
        </head>
        <body>
            <h1>UUID Manager</h1>
            <form method="POST">
                <select name="site">{}</select>
                <input type="submit" name="site_info" value="Show Site Info">
                <input type="submit" name="refresh" value="Refresh">
            </form>
            <button id="addSiteBtn">Add New Site</button>
            <div id="addSiteModal" class="modal">
                <div class="modal-content">
                    <span class="close">&times;</span>
                    <form method="POST">
                        <label for="site_name">Site Name:</label><input type="text" id="site_name" name="site_name"><br>
                        <label for="url">URL:</label><input type="text" id="url" name="url"><br>
                        <label for="mail_username">Email/Username:</label><input type="text" id="mail_username" name="mail_username"><br>
                        <label for="password">Password:</label><input type="text" id="password" name="password"><br><br>
                        <input type="submit" name="add_site" value="Add Site">
                    </form>
                </div>
            </div>
            <script>
                document.getElementById("addSiteBtn").onclick = function() {{ document.getElementById("addSiteModal").style.display = "block"; }};
                document.getElementsByClassName("close")[0].onclick = function() {{ document.getElementById("addSiteModal").style.display = "none"; }};
                window.onclick = function(event) {{ if (event.target == document.getElementById("addSiteModal")) {{ document.getElementById("addSiteModal").style.display = "none"; }} }}
            </script>
            <br>
            <p>{}</p>
        </body>
    </html>
    """

def render_html(site_options, site_info=""):
    """Renvoie le HTML complet en insérant les options de sites et les informations du site."""
    return get_html_template().format(site_options, site_info)

def get_dropdown_options():
    """Récupère les options pour le dropdown des sites."""
    decrypted_uuid = crypto_manager.decrypt_uuid()
    site_names = database_manager.get_site_names(decrypted_uuid)
    return "".join([f"<option>{name}</option>" for name in site_names])

def add_site(request_form):
    """Ajoute un nouveau site avec les informations fournies."""
    site_name = request_form["site_name"]
    url = request_form["url"]
    mail_username = request_form["mail_username"]
    password = request_form["password"]
    decrypted_uuid = crypto_manager.decrypt_uuid()
    database_manager.add_data((site_name, url, mail_username, password), decrypted_uuid)
    database_manager.refresh_data()

def get_site_info_html(site_name):
    """Renvoie les informations du site au format HTML."""
    site_info_data = database_manager.get_site_info(site_name)
    if isinstance(site_info_data, list) and len(site_info_data) > 0:
        site_info_data = site_info_data[0]
    if isinstance(site_info_data, dict):
        return (
            f"URL: <a href=\"https://{site_info_data.get('url', '')}\" target=\"_blank\">{site_info_data.get('url', 'N/A')}</a><br>"
            f"Email/Username: {site_info_data.get('mail_username', 'N/A')}<br>"
            f"Password: {site_info_data.get('password', 'N/A')}"
        )
    return "Erreur : Les informations du site sont introuvables ou incorrectes."

@app.route("/", methods=["GET", "POST"])
def index():
    dropdown_options = get_dropdown_options()
    site_info = ""

    # Gérer l'ajout d'un nouveau site
    if request.method == "POST" and "add_site" in request.form:
        add_site(request.form)
        dropdown_options = get_dropdown_options()  # Mettre à jour les options

    # Gérer la demande d'affichage d'informations d'un site
    elif request.method == "POST" and "site_info" in request.form:
        site_name = request.form["site"]
        site_info = get_site_info_html(site_name)

    # Rafraîchir les données
    elif request.method == "POST" and "refresh" in request.form:
        database_manager.refresh_data()
        dropdown_options = get_dropdown_options()

    return render_html(dropdown_options, site_info)

# Fonction pour démarrer le serveur
def start_server():
    app.run(debug=True, use_reloader=False)
