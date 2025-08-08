import sqlite3
from lib import CONN, CURSOR

class Character:

    all = []

    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self.id = None

    def __repr__(self):
        return f"Character name is [{self.name}] from [{self.hometown}] with character_id# [{self.id}]"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance (value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name is invalid")
    
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        if isinstance (value, str) and value.strip():
            self._hometown = value
        else:
            raise ValueError("Hometown is invalid")

    @classmethod
    def _from_db_row(cls, row):
        character = cls(row[1], row[2])
        character.id = row[0]
        return character
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM characters WHERE id = ?",(id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM characters WHERE name = ?",(name,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM characters")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, name, hometown):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        character = cls(name, hometown)
        character.save()
        character.id = CURSOR.lastrowid
        return character
    
    def update(self):
        CURSOR.execute("UPDATE characters SET name = ?, hometown = ? WHERE id =?",(self._name, self._hometown,self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM characters WHERE id =?", (self.id,))
        CONN.commit()

    def save(self):
        CURSOR.execute("INSERT INTO characters (name, hometown) VALUES (?,?)", (self._name, self._hometown,))
        CONN.commit()


    


