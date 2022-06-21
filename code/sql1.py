from re import I
import mysql
import mysql.connector

print("dieses skript soll mit der datenbank kommunizieren") 
print("soll das skript ausgeführt werden")
print("ja oder nein")
eingabe = input()
if eingabe == "ja":
    print("wollen sie das menü öffnen")
    print("ja oder nein")
    eingabe = input()
    if eingabe == "ja":
        