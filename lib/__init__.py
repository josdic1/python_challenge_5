import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(os.path.dirname(__file__), 'database.db')
SCHEMA_FILE = os.path.join(os.path.dirname(__file__), 'schema.sql')

def setup_database():
    """Initializes the database by creating tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        with open(SCHEMA_FILE, 'r') as file:
            sql_script = file.read()
            cursor.executescript(sql_script)
        print("Database tables created successfully!")
    except FileNotFoundError:
        print(f"Error: '{SCHEMA_FILE}' file not found. Database not set up.")
    finally:
        conn.commit()
        conn.close()


if not os.path.exists(DB_NAME):
    setup_database()
    

CONN = sqlite3.connect(DB_NAME)
CURSOR = CONN.cursor()