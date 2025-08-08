import os
import sqlite3

DB_NAME = 'database.db'

def check_db():
    if not os.path.exists(DB_NAME):
        print("Database not found.")
        return False

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Check if at least one table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print("✅ Database loaded. Tables found:")
            for table in tables:
                print(f" - {table[0]}")
            return True
        else:
            print("⚠️ Database file exists, but no tables found.")
            return False

    except Exception as e:
        print(f"❌ Error connecting to database: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    check_db()
