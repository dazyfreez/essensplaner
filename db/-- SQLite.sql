-- SQLite
CREATE TABLE essensplaner_db (
    name TEXT PRIMARY KEY NOT NULL,
    date TEXT,
    time TEXT,
    description TEXT,
    category TEXT,
    priority TEXT,
    status TEXT,
);