# flask run --reload zum starten des Servers
# mit --reload wird der Server bei Änderungen neu gestartet
# Ausnahme: bei DB oder Template Änderungen

# falls es nicht funktioniert, kann es sein, dass die Umgebungsvariable FLASK_APP nicht gesetzt ist
# dafür einfach set FLASK_APP=TirpTik/home.py setzen

# falls es bei rojin nicht funktioniert -> export FLASK_APP=home.py <- in dem Terminal eingeben
# zum aktualisieren -> git checkout main <- und danach -> git pull origin main <-
# flask run --reload

from flask import Flask, flash, json, render_template, request, redirect, session, url_for
import sqlite3
from textblob import TextBlob
from translate import Translator
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.secret_key = 'your_secret_key'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'triptik-database.db')
jsonfile = os.path.join(BASE_DIR, 'static', 'geojson', 'world-administrative-boundaries.geojson')

#Datenbankverbindung erstellen

def get_db():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def check_db_connection():
    try:
        db = get_db()
        if db is not None:
            db.execute('SELECT 1 FROM users LIMIT 1')
            print("Database connection successful")
        else:
            print("Failed to establish database connection")
    except sqlite3.OperationalError as e:
        print(f"Database connection error: {e}")
        raise e


#Registrierung und Anmeldung

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    hashed_password = generate_password_hash(password)

    try:
        db = get_db()
        if db is not None:
            db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            db.commit()
        else:
            flash('Database connection error. Please try again later.')
            return redirect(url_for('register_page'))
    except sqlite3.IntegrityError:
        flash('Username is already taken!')
        return redirect(url_for('register_page'))
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return redirect(url_for('register_page'))
    
    flash('Registration successful! Please log in.')
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    try:
        db = get_db()
        cursor = db.execute('SELECT password FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        if row and check_password_hash(row[0], password):
            user_row = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
            if user_row:
                session['user_id'] = user_row['id']
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('index'))
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return redirect(url_for('index'))


#Reise speichern

@app.route('/reise-speichern', methods=['POST'])
def reise_speichern():
    reise = request.form['reise']
    stadt = request.form['stadt']
    land = request.form['land']
    startdatum = request.form['startdatum']
    enddatum = request.form['enddatum']
    bericht = request.form['bericht']

    user = session.get('user_id')
    if not user:
        flash('Please log in to save your trip.')
        return redirect(url_for('login'))
    
    try:
        db = get_db()
        db.execute('INSERT INTO trips (name, city, country, start_date, end_date, report, user_id) VALUES (?, ?, ?, ?, ?, ?, ?)', (reise, stadt, land, startdatum, enddatum, bericht, user))
        db.commit()
        trip_row = db.execute('SELECT id FROM trips WHERE name = ?', (reise,)).fetchone()
        db.commit()
        trip_id=trip_row['id']
        return redirect(url_for('reise_page', id=trip_id))
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return redirect(url_for('reise_hinzufuegen_page'))
    

#Reise anzeigen

def get_trip(trip_id):
    try:
        db = get_db()
        trip = db.execute('SELECT * FROM trips WHERE id = ?', (trip_id,)).fetchone()
        reise = trip['name']
        stadt = trip['city']
        land = trip['country']
        startdatum = trip['start_date']
        enddatum = trip['end_date']
        bericht = trip['report']
        return reise, stadt, land, startdatum, enddatum, bericht
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return None


#Liste der Reisen vom Benutzer

def get_trip_list(user_id):
    try:
        db = get_db()
        trips = db.execute('SELECT * FROM trips WHERE user_id = ?', (user_id,)).fetchall()
        # trips enthält eine Liste von Zeilen, wobei jede Zeile ein Trip ist (sqlite3.Row-Objekte)
        return trips
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return None
    
#Liste der IDs und Namen der Reisen
def get_trip_id_name_list():
    trips = get_trip_list(session.get('user_id'))
    if trips is not None:
        return [{'id': trip['id'], 'name': trip['name']} for trip in trips]
    
#Liste der Länder der Reisen
def get_trip_country_list():
    trips = get_trip_list(session.get('user_id'))
    if trips is not None:
        countries = list({trip['country']: {'country': trip['country']} for trip in trips}.values())
        return countries

#Liste der Länder in Englisch für Vergleich mit der geojson-Datei
def get_trip_country_list_english():
    trips = get_trip_country_list()
    translator = Translator(to_lang='en', from_lang='de')
    uebersetzungen = []
    for trip in trips:
        translated = translator.translate(trip['country'])
        uebersetzungen.append({'country': translated})
    return uebersetzungen


#Prozent der bereisten Ländern berechnen

#Anzahl der Länder in der geojson-Datei zählen
def get_country_count():
    with open(jsonfile) as file:
        data = json.load(file)
    countries = set()
    for feature in data['features']:
        country = feature['properties']['name']
        if country:
            countries.add(country)
    return len(countries)

#Prozentberechnung
def get_progress():
    countries = get_trip_country_list()
    count = len(countries)
    num_countries = get_country_count()
    progress = count/num_countries*100
    return progress


#Routen zu den einzelnen Seiten

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('anmeldung.html')

@app.route('/register-page', methods=['GET', 'POST'])
def register_page():
    return render_template('registrierung.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    country_list=get_trip_country_list_english()
    progress=get_progress()
    return render_template('home.html', country_list=country_list, progress=progress)

@app.route('/reisen', methods=['GET', 'POST'])
def reisen_page():
    progress=get_progress()
    return render_template('reisen.html', progress=progress, trips=get_trip_id_name_list())

@app.route('/reise', methods=['GET', 'POST'])
def reise_page():
    if request.method == 'GET':
        trip_id = request.args.get('id')
    elif request.method == 'POST':
        trip_id = request.form.get('trip_id')

    if not trip_id:
        flash("Trip ID is missing")
        return render_template('reise.html')
    
    trip_details = get_trip(trip_id)
    if trip_details is None:
        flash("Trip not found")
        return render_template('reise.html')
    
    reise, stadt, land, startdatum, enddatum, bericht = trip_details
    
    return render_template('reise.html', reise=reise, stadt=stadt, land=land, startdatum=startdatum, enddatum=enddatum, bericht=bericht)

@app.route('/profil', methods=['POST'])
def profil_page():
    return render_template('profil.html')

@app.route('/profil_bearbeiten', methods=['GET', 'POST'])
def profil_bearbeiten_page():
    return render_template('profil_bearbeiten.html')

@app.route('/profilbilder', methods=['GET'])
def profilbilder_page():
    return render_template('profilbilder.html')

@app.route('/reise_bearbeiten', methods=['POST'])
def reise_bearbeiten_page():
    return render_template('reise_bearbeiten.html')

@app.route('/reise_hinzufuegen', methods=['GET', 'POST'])
def reise_hinzufuegen_page():
    return render_template('reise_hinzufuegen.html')

# Route zur sidebar... checke nichts mehr

#@app.route('/sidebar')
#def sidebar():
    user_id = session.get('user_id')
    if not user_id:
        flash('Please log in to view your profile.')
        return redirect(url_for('login'))
    
    try:
        db = get_db()
        user = db.execute('SELECT username, bio FROM users WHERE id = ?', (user_id,)).fetchone()
        if user:
            return render_template('sidebar.html', name=user['username'], bio_content=user['bio'])
        else:
            flash('User not found.')
            return redirect(url_for('home'))
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return redirect(url_for('home'))

# Error-Handler für 404-Fehler

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    print(f"Current working directory: {os.getcwd()}")
    print(f"Contents of the current directory: {os.listdir()}")
    check_db_connection()
    app.run(debug=True)