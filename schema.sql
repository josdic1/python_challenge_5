IF NOT EXISTS CREATE TABLE characters (
    id INTEGER PRIMARY KEY,
    name TEXT,
    hometown TEXT
);

IF NOT EXISTS CREATE TABLE special_moves (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    character_id INTEGER,
    combo_id INTEGER,
    FOREIGN KEY (character_id) REFERENCES characters (id),
    FOREIGN KEY (combo_id) REFERENCES combos (id)
);

