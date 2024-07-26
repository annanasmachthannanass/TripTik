import sqlite3

DATABASE = 'triptik_database.db'

def create_tables():
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # SQL-Befehle zum Erstellen der Tabellen
    create_users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        reise_id INTEGER,
        FOREIGN KEY (reise_id) REFERENCES reisen(id)
    )
    '''

    create_reisen_table = '''
    CREATE TABLE IF NOT EXISTS reisen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country TEXT NOT NULL,
        city TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    '''

    try:
        # Tabellen erstellen
        c.execute(create_users_table)
        c.execute(create_reisen_table)
        print("Tabellen wurden erfolgreich erstellt.")
    except sqlite3.Error as e:
        print(f"Fehler beim Erstellen der Tabellen: {e}")
    finally:
        # Verbindung schließen
        conn.commit()
        conn.close()

if __name__ == '__main__':
    create_tables()
