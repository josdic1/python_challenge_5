CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    hometown TEXT
);

CREATE TABLE IF NOT EXISTS fighting_styles (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS special_moves (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    character_id INTEGER,
    combo_id INTEGER,
    FOREIGN KEY (character_id) REFERENCES characters (id),
    FOREIGN KEY (combo_id) REFERENCES combos (id)
);

CREATE TABLE IF NOT EXISTS combos (
    id INTEGER PRIMARY KEY,
    name TEXT
);

