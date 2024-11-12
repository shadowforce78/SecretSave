from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'clé'  # Clé secrète pour la gestion des sessions Flask

# Page de connexion
@app.route('/', methods=['GET', 'POST'])
def login():
    from main import PasswordManager  # Importation retardée pour éviter les importations circulaires
    password_manager = PasswordManager(None)
    if request.method == 'POST':
        password = request.form['password']
        login_success, _ = password_manager.db.verify_login(password_manager.uuid, password)
        if login_success:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            flash("Identifiants incorrects!", "danger")
    return render_template('login.html')

# Tableau de bord après connexion
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    from main import PasswordManager
    password_manager = PasswordManager(None)
    site_names = password_manager.db.get_site_names(password_manager.uuid)
    return render_template('dashboard.html', sites=site_names)

# Ajouter un site
@app.route('/add_site', methods=['GET', 'POST'])
def add_site():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        site_name = request.form['site_name']
        url = request.form['url']
        mail_username = request.form['mail_username']
        password = request.form['password']
        from main import PasswordManager

        password_manager = PasswordManager(None)
        password_manager.add_site(site_name, url, mail_username, password)
        flash("Site ajouté avec succès!", "success")
        return redirect(url_for('dashboard'))
    return render_template('add_site.html')

# Supprimer un site
@app.route('/delete_site', methods=['POST'])
def delete_site():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    site_name = request.form['site_name']
    from main import PasswordManager
    password_manager = PasswordManager(None)
    password_manager.delete_site(site_name)
    flash("Site supprimé avec succès!", "success")
    return redirect(url_for('dashboard'))

# Déconnexion
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("Déconnecté avec succès.", "info")
    return redirect(url_for('login'))

def start_server():
    app.run(debug=True, use_reloader=False)
