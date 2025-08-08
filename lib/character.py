import sqlite3
from lib import CONN, CURSOR

class Character:

    all = []

    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self.id = None

    def __repr__(self):
        return f"Character name is [{self.name}] from [{self.name}] with character_id# [{self.id}]"
    
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
        CONN.commit()
        return cls._from_db_row(row) if row else None
    


