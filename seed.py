import sqlite3
import os

DB_NAME = 'database.db'
SCHEMA_FILE = 'schema.sql'

# Connect to the database, creating it if it doesn't exist
CONN = sqlite3.connect(DB_NAME)
CURSOR = CONN.cursor()

# Run the schema script to create tables
with open(SCHEMA_FILE, 'r') as f:
    CURSOR.executescript(f.read())


CONN.commit()
CONN.close()

print("✅ database.db initialized and populated with seed data")