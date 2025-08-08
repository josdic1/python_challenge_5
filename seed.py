import sqlite3

CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()

with open('schema.sql', 'r') as f:
    CURSOR.executescript(f.read())

CONN.commit()
CONN.close()

print("✅ database.db initialized from schema.sql")
