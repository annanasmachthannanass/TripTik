from flask import Flask, flash, render_template, request, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'triptik-database.db')

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

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('anmeldung.html')

@app.route('/create_users_table')
def create_users_table():
    db = get_db()
    try:
        db.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        db.execute('''
            CREATE TABLE reisen (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                city TEXT,
                country TEXT,
                start_date TEXT,
                end_date TEXT,
                bereich TEXT,
                images BLOB,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        db.commit()
        return "Tabelle 'users' wurde erfolgreich erstellt."
    except sqlite3.Error as e:
        return f"Datenbankfehler: {e}"
    
@app.route('/create_trips_table')
def create_trips_table():
    db = get_db()
    try:
        db.execute('''
            CREATE TABLE trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                city TEXT,
                country TEXT,
                start_date DATE,
                end_date DATE,
                report TEXT,
                images BLOB,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        db.commit()
        return "Tabelle 'trips' wurde erfolgreich erstellt."
    except sqlite3.Error as e:
        return f"Datenbankfehler: {e}"
    
@app.route('/drop_reisen_table')
def drop_reisen_table():
    db = get_db()
    try:
        db.execute('''
            DROP TABLE reisen
        ''')
        db.commit()
        return "Tabelle 'reisen' wurde erfolgreich gelöscht."
    except sqlite3.Error as e:
        return f"Datenbankfehler: {e}"
    
@app.route('/add_bio_column')
def add_bio_column():
    db = get_db()
    try:
        db.execute('''
            ALTER TABLE users
            ADD COLUMN bio TEXT
        ''')
        db.commit()
        return "Spalte 'bio' wurde erfolgreich zur Tabelle 'users' hinzugefügt."
    except sqlite3.Error as e:
        return f"Datenbankfehler: {e}"
    
@app.route('/add_images_table')
def add_images_table():
    db = get_db()
    try:
        db.execute('''
            CREATE TABLE images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image BLOB,
                trip_id INTEGER,
                FOREIGN KEY(trip_id) REFERENCES trips(id)
            )
        ''')
        db.commit()
        return "Tabelle 'images' wurde erfolgreich erstellt."
    except sqlite3.Error as e:
        return f"Datenbankfehler: {e}"

if __name__ == '__main__':
    print(f"Aktueller Arbeitsordner: {os.getcwd()}")
    print(f"Inhalt des aktuellen Ordners: {os.listdir()}")
    check_db_connection()
    app.run(debug=True)
