-- SQLite
CREATE TABLE essensplaner_db (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    time TEXT,
    description TEXT,
    category TEXT,
    priority TEXT,
    status TEXT,
    user TEXT
);