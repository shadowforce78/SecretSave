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


# Page principale
@app.route("/", methods=["GET", "POST"])
def index():
    html_template = """
    <html>
        <head>
            <title>UUID Manager</title>
            <style>
                h1 {{
                    text-align: center;
                }}
                form {{
                    text-align: center;
                }}
                select {{
                    width: 200px;
                    margin-bottom: 10px;
                }}
                p {{
                    text-align: center;
                }}
                .modal {{
                    display: none;
                    position: fixed;
                    z-index: 1;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    overflow: auto;
                    background-color: rgb(0,0,0);
                    background-color: rgba(0,0,0,0.4);
                    padding-top: 60px;
                }}
                .modal-content {{
                    background-color: #fefefe;
                    margin: 5% auto;
                    padding: 20px;
                    border: 1px solid #888;
                    width: 80%;
                }}
                .close {{
                    color: #aaa;
                    float: right;
                    font-size: 28px;
                    font-weight: bold;
                }}
                .close:hover,
                .close:focus {{
                    color: black;
                    text-decoration: none;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <h1>UUID Manager</h1>
            <form method="POST">
                <select name="site">
                    {}
                </select>
                <input type="submit" name="site_info" value="Show Site Info">
                <input type="submit" name="refresh" value="Refresh">
            <br>
            </form>
            <button id="addSiteBtn">Add New Site</button>
            <div id="addSiteModal" class="modal">
                <div class="modal-content">
                    <span class="close">&times;</span>
                    <form method="POST">
                        <label for="site_name">Site Name:</label><br>
                        <input type="text" id="site_name" name="site_name"><br>
                        <label for="url">URL:</label><br>
                        <input type="text" id="url" name="url"><br>
                        <label for="mail_username">Email/Username:</label><br>
                        <input type="text" id="mail_username" name="mail_username"><br>
                        <label for="password">Password:</label><br>
                        <input type="text" id="password" name="password"><br><br>
                        <input type="submit" name="add_site" value="Add Site">
                    </form>
                </div>
            </div>
            <script>
                var modal = document.getElementById("addSiteModal");
                var btn = document.getElementById("addSiteBtn");
                var span = document.getElementsByClassName("close")[0];

                btn.onclick = function() {{
                    modal.style.display = "block";
                }}

                span.onclick = function() {{
                    modal.style.display = "none";
                }}

                window.onclick = function(event) {{
                    if (event.target == modal) {{
                        modal.style.display = "none";
                    }}
                }}
            </script>
            <br>
            <p>{}</p>
        </body>
    </html>
    """

    # Initialiser le gestionnaire de crypto et la base de données
    cm = CryptoManager()
    db = DatabaseManager()

    # Charger l'UUID déchiffré
    decrypted_uuid = cm.decrypt_uuid()

    # Obtenir les noms de sites et préparer les options pour le dropdown
    site_names = db.get_site_names(decrypted_uuid)
    dropdown_options = "".join([f"<option>{name}</option>" for name in site_names])

    # Définir `site_info` comme vide au début
    site_info = ""

    # Si une soumission a été faite pour ajouter un nouveau site
    if request.method == "POST" and "add_site" in request.form:
        site_name = request.form["site_name"]
        url = request.form["url"]
        mail_username = request.form["mail_username"]
        password = request.form["password"]
        info = site_name,url,mail_username,password
        db.add_data(info, decrypted_uuid)
        # Rafraîchir les données de la base de données
        db.refresh_data()
        # Retourner le HTML formaté avec les options du dropdown sans les infos du site
        return html_template.format(dropdown_options, site_info)

    # Si une soumission a été faite
    if request.method == "POST" and "site_info" in request.form:
        site_name = request.form["site"]
        site_info_data = db.get_site_info(site_name)

        # Vérifier si `site_info_data` est une liste, et dans ce cas, accéder au premier élément
        if isinstance(site_info_data, list) and len(site_info_data) > 0:
            site_info_data = site_info_data[0]

        # Assurer que `site_info_data` est bien un dictionnaire avant de l'afficher
        if isinstance(site_info_data, dict):
            site_info = f"URL: <a href=\"https://{site_info_data.get('url', '')}\" target=\"_blank\">{site_info_data.get('url', 'N/A')}</a><br>Email/Username: {site_info_data.get('mail_username', 'N/A')}<br>Password: {site_info_data.get('password', 'N/A')}"
        else:
            site_info = (
                "Erreur : Les informations du site sont introuvables ou incorrectes."
            )
        # Retourner le HTML formaté avec les options et les infos du site
        return html_template.format(dropdown_options, site_info)
    if request.method == "POST" and "refresh" in request.form:
        # Rafraîchir les données de la base de données
        db.refresh_data()
        # Retourner le HTML formaté avec les options du dropdown sans les infos du site
        return html_template.format(dropdown_options, site_info)
    else:
        # Retourner le HTML formaté avec les options du dropdown sans les infos du site
        return html_template.format(dropdown_options, site_info)


# Fonction pour démarrer le serveur
def start_server():
    app.run(debug=True, use_reloader=False)
