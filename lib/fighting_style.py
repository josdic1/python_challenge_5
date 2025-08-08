import sqlite3
from lib import CONN, CURSOR

class FightingStyle:

    all = []

    def __init__(self, style_name):
        self.style_name = style_name
        self.id = None

    def __repr__(self):
        return f"Fighting style is {self.style_name} with the ID# {self.id}"
    
    @property
    def style_name(self):
        return self._style_name
    
    @style_name.setter
    def style_name(self, value):
        if isinstance(value, str) and value.strip():
            self._style_name = value
        else:
            raise ValueError("Style Name is invalid")
        
    @classmethod
    def _from_db_row(cls, row):
        fighting_style = cls(row[1])
        fighting_style.id = row[0]
        return fighting_style
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM fighting_styles WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None

    @classmethod
    def find_by_style_name(cls, style_name):
        CURSOR.execute("SELECT * FROM fighting_styles WHERE style_name = ?", (style_name,))
        row = CURSOR.fetchone()
        return cls._from_db_row(row) if row else None
    
    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM fighting_styles")
        rows = CURSOR.fetchall()
        return [cls._from_db_row(row) for row in rows] if rows else []
    
    @classmethod
    def add_new(cls, style_name):
        existing = cls.find_by_style_name(style_name)
        if existing:
            return existing
        style = cls(style_name)
        style.save()
        style.id = CURSOR.lastrowid
        return style
    
    def update(self):
        CURSOR.execute("UPDATE fighting_styles SET style_name = ? WHERE id = ?", (self._style_name, self.id,))
        CONN.commit()


    def delete(self):
        CURSOR.execute("DELETE FROM fighting_styles WHERE id =?", (self.id,))
        CONN.commit()
    
    def save(self):
        try:
            CURSOR.execute("INSERT INTO fighting_styles (style_name) VALUES (?)", (self._style_name,))
            CONN.commit()
        except sqlite3.IntegrityError:
            print("Error: A fighting_style with this names may already exist.")
            
            