import sqlite3

def create_connection(db_file):
    """Erstellt eine Datenbankverbindung zu einer SQLite-Datenbank"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Verbunden mit SQLite-Version: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Erstellt eine Tabelle in der SQLite-Datenbank"""
    try:
        sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        age INTEGER NOT NULL
                                    ); """
        c = conn.cursor()
        c.execute(sql_create_users_table)
        print("Tabelle 'users' wurde erfolgreich erstellt.")
    except sqlite3.Error as e:
        print(e)

def main():
    database = "my_database.db"

    # Verbindung zur Datenbank herstellen
    conn = create_connection(database)

    # Tabelle erstellen
    if conn is not None:
        create_table(conn)
    else:
        print("Fehler! Keine Verbindung zur Datenbank.")

    # Verbindung schließen
    if conn:
        conn.close()

if __name__ == '__main__':
    main()
