-- SQLite
CREATE TABLE MEAL (gerichtname TEXT NOT NULL PRIMARY KEY , zutaten TEXT , zeit TEXT , beschreibung TEXT , kategorie TEXT ,);
INSERT INTO meal (gerichtname, zutaten, zeit, beschreibung, kategorie) 
VALUES ('Pizza', 'Tomatensauce, Mozzarella, Basilikum, Salami', '20:00', 'Pizza mit Tomatensauce, Mozzarella, Basilikum, Salami', 'Pizza');
