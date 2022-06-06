-- SQLite
CREATE TABLE essensplaner_db (
  gerichtname TEXT PRIMARY KEY NOT NULL,
  zutaten TEXT,
  timee TEXT,
  descriptione TEXT,
  category TEXT,
);
INSERT INTO essensplaner_db (gerichtname, zutaten, timee, descriptione, category) VALUES ('Pizza', 'Tomatensauce, Mozzarella, Basilikum, Salami', '20:00', 'Pizza mit Tomatensauce, Mozzarella, Basilikum, Salami', 'Pizza');