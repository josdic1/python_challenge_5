import sqlite3
from lib import CONN, CURSOR
from lib.special_move import SpecialMove

class Combo:
    def __init__(self, pattern):
        self.pattern = pattern
        self.id = None

    def __repr__(self):
        return f"Combo has the pattern {self.pattern} with the ID# {self.id}"
    
    @property
    def pattern(self):
        return self._pattern
    
    @pattern.setter
    def pattern(self, value):
        if isinstance(value, str) and value.strip():
            self._pattern = value
        else:
            raise ValueError("Pattern is invalid")
        
    @classmethod
    def _from_db_row(cls, row):
        combo = cls(row[1])
        combo.id = row[0]
        return combo
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM combos WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def find_by_pattern(cls, pattern):
        CURSOR.execute("SELECT * FROM combos WHERE pattern = ?", (pattern,))
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM combos")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def get_characters(cls):
        moves = SpecialMove.get_all()
        print(moves)

    
    @classmethod
    def add_new(cls, pattern):
        existing = cls.find_by_pattern(pattern)
        if existing:
            return existing[0]
        combo = cls(pattern)
        combo.save()
        combo.id = CURSOR.lastrowid
        return combo
    
    def update(self):
        CURSOR.execute("UPDATE combos SET pattern  = ? WHERE id = ?",(self._pattern, self.id,))
        CONN.commit()


    def delete(self):
        CURSOR.execute("DELETE FROM combos WHERE id =?", (self.id,))
        CONN.commit()
    
    def save(self):
        try:
            CURSOR.execute("INSERT INTO combos (pattern) VALUES (?)", (self._pattern,))
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Error: A combo with this pattern may already exist.")
            
            