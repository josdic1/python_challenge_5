import sqlite3
from lib import CONN, CURSOR

class SpecialMove:

    all = []

    def __init__(self, name, category, character_id, combo_id):
        self.name = name
        self.category = category
        self.character_id = character_id
        self.combo_id = combo_id
        self.id = None

    def __repr__(self):
        return f"SpecialMove: {self.name} is a {self.category} with combo {self.combo_id}. Character: {self.character_id}"
    
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
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance (value, str) and value.strip():
            self._category = value
        else:
            raise ValueError("Category is invalid")
        
    @property
    def character_id(self):
        return self._character_id
    
    @character_id.setter
    def character_id(self, value):
        if isinstance (value, int) and value > 0:
            self._character_id = value
        else:
            raise ValueError("Character ID must be a positive integer")
    
    @property
    def combo_id(self):
        return self._combo_id
    
    @combo_id.setter
    def combo_id(self, value):
        if isinstance (value, int) and value > 0:
            self._combo_id = value
        else:
            raise ValueError("Combo ID must be a positive integer")

    @classmethod
    def _from_db_row(cls, row):
        special_move = cls(row[1], row[2], row[3], row[4])
        special_move.id = row[0]
        return special_move
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM special_moves WHERE id = ?",(id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM special_moves WHERE name = ?",(name,))
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM special_moves")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, name, category, character_id, combo_id):
        existing = cls.find_by_name(name)
        if existing:
            return existing
        special_move = cls(name, category, character_id, combo_id)
        special_move.save()
        special_move.id = CURSOR.lastrowid
        return special_move
    
    def update(self):
        CURSOR.execute("UPDATE special_moves SET name = ?, category = ?, character_id  = ?, combo_id  = ? WHERE id =?",(self._name, self._category, self._character_id, self._combo_id, self.id,))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM special_moves WHERE id =?", (self.id,))
        CONN.commit()

    def save(self):
        try:
            CURSOR.execute("INSERT INTO special_moves (name, category, character_id, combo_id) VALUES (?,?,?,?)", (self._name, self._category, self._character_id, self._combo_id))
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Error: A special move with this name may already exist.")