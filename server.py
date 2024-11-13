from flask import Flask, request, flash
from utils import CryptoManager
from database import DatabaseManager

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
keyFile = "key.key"
uuidFile = "uuid.txt"
dataFile = "data.json"

@app.route("/", methods=["GET", "POST"])
def index():
    html = """
    <html>
        <head>
            <title>UUID Manager</title>
        </head>
        <body>
            <h1>UUID Manager</h1>
            <form method="POST">
                <input type="submit" name="uuid" value="Show UUID">
                <input type="submit" name="data" value="Show Data">
            </form>
            <br>
            <p>{}</p>
        </body>
    """
    cm = CryptoManager()
    db = DatabaseManager()
    decrypted_uuid = None
    if request.method == "POST":
        if "uuid" in request.form:
            decrypted_uuid = cm.decrypt_uuid()
        elif "data" in request.form:
            decrypted_uuid = db.get_site_names(cm.decrypt_uuid())
    return html.format(decrypted_uuid)

def start_server():
    app.run(debug=True, use_reloader=False)
