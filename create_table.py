import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'triptik-database.db')

def create_tables():
    db = get_db()
    try:
        db.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                bio TEXT
            )
        ''')
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
        return "Tabelle 'users' wurde erfolgreich erstellt."
    except sqlite3.Error as e:
        return f"Datenbankfehler: {e}"

if __name__ == '__main__':
    create_tables()
