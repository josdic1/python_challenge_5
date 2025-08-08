import sqlite3
import os

DB_NAME = 'database.db'


if not os.path.exists(DB_NAME):
    raise FileNotFoundError(f"Database file '{DB_NAME}' not found. Please run seed.py first.")

CONN = sqlite3.connect(DB_NAME)
CURSOR = CONN.cursor()