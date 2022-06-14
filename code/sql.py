import mysql.connector
Servername = 'localhost' # Rechnername (localhost ist dein eigener Rechner)
Benutzer   = 'webterra'
Passwort   = 'pwd'
Datenbank  = 'terra'

# Verbindung mit der Datenbank
con = mysql.connector.connect(host=Servername)
con.cmd_change_user(username = Benutzer, password = Passwort)
con.database = Datenbank


# SQL-Befehl ausführen
cursor = con.cursor()
SQLBefehl = 'SELECT Name, Einwohner FROM kontinent'
cursor.execute(SQLBefehl)


# Durchlaufen der Ergebnisse
row=cursor.fetchone()
while (row!=None):
  print(row[0], row[1])
  row = cursor.fetchone()

# Ende der Verarbeitung
cursor.close()
# Abmelden
con.disconnect()  