import base64
from flask import Flask, flash, json, jsonify, render_template, request, redirect, session, url_for
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

file_path = os.path.join(BASE_DIR, 'static', 'json', 'countries_de_to_en.json')
with open(file_path, 'r', encoding='utf-8') as file:
    country_translations = json.load(file)

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

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

#User-Infos abrufen

def get_user_id():
    user = session.get('user_id')
    if not user:
        flash('Please log in to have access.')
        return redirect(url_for('index'))
    return user

def get_user_info(user_id):
    try:
        db = get_db()
        user = db.execute('SELECT username, bio, profile_picture FROM users WHERE id = ?', (user_id,)).fetchone()
        return user
    except sqlite3.Error as e:
        flash(f"Database error: {e}")

def get_user_name(user_id):
    user = get_user_info(user_id)
    if user:
        return user['username']
    else:
        return None
    
def get_user_bio(user_id):
    user = get_user_info(user_id)
    if user:
        return user['bio']
    else:
        return None

def get_user_profile_picture(user_id):
    user = get_user_info(user_id)
    if user and user['profile_picture']:
        return user['profile_picture']
    else:
        return '/static/profile_pictures/profilbild1.PNG'


#Reise speichern

@app.route('/reise-speichern', methods=['POST'])
def reise_speichern():
    user_id = get_user_id()
    reise = request.form['reise']
    stadt = request.form['stadt']
    land = request.form['land']
    startdatum = request.form['startdatum']
    enddatum = request.form['enddatum']
    bericht = request.form['bericht']
    files = request.files.getlist('bild')
    if not files:
        flash('Please upload at least one image.')
    try:
        db = get_db()
        db.execute('INSERT INTO trips (name, city, country, start_date, end_date, report, user_id) VALUES (?, ?, ?, ?, ?, ?, ?)', (reise, stadt, land, startdatum, enddatum, bericht, user_id))
        db.commit()
        trip_row = db.execute('SELECT id FROM trips WHERE name = ?', (reise,)).fetchone()
        db.commit()
        for file in files:
            if file.filename !='' :
                file_blob = file.read()
                db.execute('INSERT INTO images (trip_id, image) VALUES (?, ?)', (trip_row['id'], file_blob))
                db.commit()     
        trip_id=trip_row['id']
        return redirect(url_for('reise_page', trip_id=trip_id))
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            flash("Fehler: Der Name der Reise muss einzigartig sein. Bitte ändern Sie den Namen der Reise.")
            name=get_user_name(user_id)
            bio=get_user_bio(user_id)
            trips=get_trip_id_name_list()
            return render_template('reise_hinzufuegen.html', name=name, bio=bio, trips=trips, stadt=stadt, land=land, startdatum=startdatum, enddatum=enddatum, bericht=bericht)
        else:
            flash(f"Datenbankfehler: {e}")
            return redirect(url_for('reise_hinzufuegen_page'))
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return redirect(url_for('reise_hinzufuegen_page'))
    

#Reise ändern

@app.route('/reise-aendern', methods=['GET', 'POST'])
def reise_aendern():
    user_id = get_user_id()
    trip_id = request.form.get('trip_id')
    reise = request.form['reise']
    stadt = request.form['stadt']
    land = request.form['land']
    startdatum = request.form['startdatum']
    enddatum = request.form['enddatum']
    bericht = request.form['bericht']
    try:
        db = get_db()
        db.execute('''
            UPDATE trips 
                set name = ?, city = ?, country = ?, start_date = ?, end_date = ?, report = ?
                WHERE id = ?
            ''', 
            (reise, stadt, land, startdatum, enddatum, bericht, trip_id))
        db.commit()
        return redirect(url_for('reise_page', trip_id=trip_id))
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            flash("Fehler: Der Name der Reise muss einzigartig sein. Bitte ändern Sie den Namen der Reise.")
            name=get_user_name(user_id)
            bio=get_user_bio(user_id)
            trips=get_trip_id_name_list()
            return render_template('reise_bearbeiten.html', name=name, bio=bio, trips=trips, stadt=stadt, land=land, startdatum=startdatum, enddatum=enddatum, bericht=bericht)
        else:
            flash(f"Datenbankfehler: {e}")
            return redirect(url_for('reise_bearbeiten_page'))
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return redirect(url_for('reise_bearbeiten_page'))
    

#Reise-Inhalte aus der Datenbank abrufen

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

#Liste der Bilder einer Reise
def get_trip_images(trip_id):
    try:
        db = get_db()
        image_blob_list = db.execute('SELECT image FROM images WHERE trip_id = ?', (trip_id,)).fetchall()
        # image_blob_list enthält eine Liste von Zeilen, wobei jede Zeile ein Bild ist (sqlite3.Row-Objekte)
        images = [base64.b64encode(image['image']).decode('utf-8') for image in image_blob_list]
        return images
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
    
#Liste der IDs und Namen und erstes Bild der Reisen
def get_trip_id_name_list():
    trips = get_trip_list(get_user_id())
    trip_id_name_image_list = []
    for trip in trips:
        trip_id=trip['id']
        trip_name=trip['name']
        trip_images = get_trip_images(trip_id)
        first_image = None
        if trip_images:
            first_image = f"data:image/jpeg;base64,{trip_images[0]}"  
        else:
            first_image = url_for('static', filename='images/logo.png')
        trip_id_name_image_list.append({'id': trip_id, 'name': trip_name, 'image': first_image})
    if trips is not None:
        return trip_id_name_image_list
 
#Liste der Länder der Reisen
def get_trip_country_list():
    trips = get_trip_list(get_user_id())
    if trips is not None:
        countries = list({trip['country']: {'country': trip['country']} for trip in trips}.values())
        return countries

#Liste der Länder in Englisch für Vergleich mit der geojson-Datei
def get_trip_country_list_english():
    trips = get_trip_country_list() 
    uebersetzungen = []
    for trip in trips:
        german_country = trip['country']
        # Übersetzung aus der JSON-Datei verwenden
        translated_country = country_translations.get(german_country, german_country)
        uebersetzungen.append({'country': translated_country})
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
    user_id = get_user_id()
    name=get_user_name(user_id)
    bio=get_user_bio(user_id)
    profile_picture = get_user_profile_picture(user_id)  
    country_list = get_trip_country_list_english()
    progress = get_progress()
    trips =get_trip_id_name_list()
    return render_template('home.html', name=name, bio=bio, profile_picture=profile_picture, country_list=country_list, progress=progress,trips=trips)

@app.route('/reisen', methods=['GET', 'POST'])
def reisen_page():
    user_id = get_user_id()
    name=get_user_name(user_id)
    bio=get_user_bio(user_id)
    profile_picture = get_user_profile_picture(user_id)
    progress=get_progress()
    trips=get_trip_id_name_list()
    return render_template('reisen.html', name=name, bio=bio, profile_picture=profile_picture, progress=progress, trips=trips)

@app.route('/reise', methods=['GET', 'POST'])
def reise_page():
    user_id = get_user_id()
    if request.method == 'GET':
        trip_id = request.args.get('trip_id')
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
    name=get_user_name(user_id)
    bio=get_user_bio(user_id)
    profile_picture = get_user_profile_picture(user_id)
    trips = get_trip_id_name_list()
    trip_bilder=get_trip_images(trip_id)
    return render_template('reise.html', name=name, bio=bio, reise=reise, profile_picture=profile_picture, stadt=stadt, land=land, startdatum=startdatum, enddatum=enddatum, bericht=bericht, trip_bilder=trip_bilder, trip_id=trip_id, trips=trips)

@app.route('/reise_bearbeiten', methods=['GET', 'POST'])
def reise_bearbeiten_page():
    user_id = get_user_id()
    trip_id = request.form.get('trip_id')
    if not trip_id:
        flash("Trip ID is missing")
        return render_template('reise.html')  
    trip_details = get_trip(trip_id)
    if trip_details is None:
        flash("Trip not found")
        return render_template('reise.html')
    reise, stadt, land, startdatum, enddatum, bericht = trip_details
    name=get_user_name(user_id)
    bio=get_user_bio(user_id)
    profile_picture = get_user_profile_picture(user_id)
    trips = get_trip_id_name_list()
    trip_bilder=get_trip_images(trip_id)
    return render_template('reise_bearbeiten.html', name=name, bio=bio, profile_picture=profile_picture, trips=trips, reise=reise, stadt=stadt, land=land, startdatum=startdatum, enddatum=enddatum, bericht=bericht, trip_id=trip_id, trip_bilder=trip_bilder)

@app.route('/reise_hinzufuegen', methods=['GET', 'POST'])
def reise_hinzufuegen_page():
    user_id = get_user_id()
    name=get_user_name(user_id)
    bio=get_user_bio(user_id)
    profile_picture = get_user_profile_picture(user_id)
    trips = get_trip_id_name_list()
    return render_template('reise_hinzufuegen.html', name=name, bio=bio, trips=trips, profile_picture=profile_picture)

@app.route('/profil', methods=['GET','POST'])
def profil_page():
    user_id = get_user_id()
    name=get_user_name(user_id)
    bio=get_user_bio(user_id)
    profile_picture = get_user_profile_picture(user_id)
    trips=get_trip_id_name_list()
    return render_template('profil.html', name=name, bio=bio, profile_picture=profile_picture, trips=trips)


# Profil-Funktionalitäten 

@app.route('/profil_bearbeiten', methods=['GET', 'POST'])
def profil_bearbeiten_page():
    user_id = get_user_id()
    try:
        db = get_db()
        if request.method == 'POST':
            neuer_name = request.form.get('nickname','')
            neue_bio = request.form.get('bio','')
            if not neuer_name:
                flash('Der Benutzername darf nicht leer sein.')
                return redirect(url_for('profil_bearbeiten_page'))
            db.execute('UPDATE users SET username = ?, bio = ? WHERE id = ?', (neuer_name, neue_bio, user_id))
            db.commit()
            flash('Profil erfolgreich aktualisiert!')
            return redirect(url_for('profil_page'))
        name=get_user_name(user_id)
        bio=get_user_bio(user_id)
        profile_picture = get_user_profile_picture(user_id)
        trips=get_trip_id_name_list()
        return render_template('profil_bearbeiten.html', name=name, bio=bio, profile_picture=profile_picture, trips=trips)
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            flash("Fehler: Der Benutzername muss einzigartig sein. Bitte wählen Sie einen anderen Benutzernamen.")
            name=get_user_name(user_id)
            bio=get_user_bio(user_id)
            trips=get_trip_id_name_list()
            return render_template('profil_bearbeiten.html', name=name, bio=bio, trips=trips)
        else:
            flash(f"Datenbankfehler: {e}")
            return redirect(url_for('profil_bearbeiten_page'))
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return render_template('profil_bearbeiten.html')
    
@app.route('/profilbilder', methods=['GET'])
def profilbilder_page():
    user_id = get_user_id()
    name=get_user_name(user_id)
    bio=get_user_bio(user_id)
    profile_picture=get_user_profile_picture(user_id)
    trips=get_trip_id_name_list()
    return render_template('profilbilder.html', name=name, bio=bio, profile_picture=profile_picture, trips=trips)

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
    user_id = session.get('user_id')
    if not user_id:
        flash('Please log in to update your profile picture.')
        return redirect(url_for('index'))
    
    new_profile_picture = request.form.get('profile_picture')
    if not new_profile_picture:
        flash('No profile picture selected.')
        return redirect(url_for('profilbilder_page'))

    try:
        db = get_db()
        db.execute('UPDATE users SET profile_picture = ? WHERE id = ?', (new_profile_picture, user_id))
        db.commit()
        flash('Profile picture updated successfully.')
        return redirect(url_for('profil_bearbeiten_page'))
    except sqlite3.Error as e:
        flash(f"Database error: {e}")
        return redirect(url_for('profilbilder_page'))
    

#Bucketlist-Funktionalitäten    

@app.route('/bucketlist', methods=['GET', 'POST'])
def bucketlist_clicked():
    user_id = get_user_id()
    name = get_user_name(user_id)
    bio = get_user_bio(user_id)
    profile_picture = get_user_profile_picture(user_id)
    trips = get_trip_id_name_list()
    try:
        db = get_db()
        bucketlist_items = db.execute('SELECT id, description, checked FROM bucketlist_items WHERE user_id = ?', (user_id,)).fetchall()
    except sqlite3.Error as e:
        flash(f"Datenbankfehler: {e}")
        bucketlist_items = []
    return render_template('bucketlist.html', 
                           name=name, 
                           bio=bio, 
                           profile_picture=profile_picture, 
                           trips=trips, 
                           bucketlist_items=bucketlist_items)

@app.route('/add_bucketlist_item', methods=['POST'])
def add_bucketlist_item():
    user_id = get_user_id()
    
    description = request.form.get('description')
    if not description:
        flash('Bitte gib eine Beschreibung ein.')
        return redirect(url_for('bucketlist_clicked'))
    try:
        db = get_db()
        db.execute('INSERT INTO bucketlist_items (user_id, description) VALUES (?, ?)', (user_id, description))
        db.commit()
        flash('Bucketlist-Punkt hinzugefügt.')
    except sqlite3.Error as e:
        flash(f"Datenbankfehler: {e}")
    return redirect(url_for('bucketlist_clicked'))

@app.route('/update_bucketlist_item/<int:item_id>', methods=['POST'])
def update_bucketlist_item(item_id):
    user_id = get_user_id()
    checked = request.form.get('checked') == 'true'
    try:
        db = get_db()
        db.execute('UPDATE bucketlist_items SET checked = ? WHERE id = ? AND user_id = ?', (checked, item_id, user_id))
        db.commit()
        return jsonify({'status': 'success'})  # JSON-Antwort zurückgeben
    except sqlite3.Error as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500  
    
@app.route('/delete_bucketlist_item/<int:item_id>', methods=['POST'])
def delete_bucketlist_item(item_id):
    user_id = get_user_id()
    try:
        db = get_db()
        db.execute('DELETE FROM bucketlist_items WHERE id = ? AND user_id = ?', (item_id, user_id))
        db.commit()
        flash('Bucketlist-Punkt gelöscht.')
    except sqlite3.Error as e:
        flash(f"Datenbankfehler: {e}")
    return redirect(url_for('bucketlist_clicked'))


# Error-Handler für 404-Fehler

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    print(f"Current working directory: {os.getcwd()}")
    print(f"Contents of the current directory: {os.listdir()}")
    check_db_connection()
    app.run(debug=True)