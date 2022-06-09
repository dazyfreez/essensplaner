-- SQLite
CREATE TABLE essensplaner_db (
  gerichtname TEXT NOT NULL PRIMARY KEY ,
  zutaten TEXT NOT NULL,
  zeit TEXT NOT NULL,
  beschreibung TEXT NOT NULL,
  kategorie TEXT NOT NULL,
);
INSERT INTO essensplaner_db (gerichtname, zutaten, zeit, beschreibung, kategorie) 
VALUES ('Pizza', 'Tomatensauce, Mozzarella, Basilikum, Salami', '20:00', 'Pizza mit Tomatensauce, Mozzarella, Basilikum, Salami', 'Pizza');