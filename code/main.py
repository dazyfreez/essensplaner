print("das ist das mainscript") 
essen =  ["spagetti", "burger", "lasagne", "bestellen", "eier"]
print("das ist gut")
print("dieses skript ist ein essensplaner")
print("es soll zukünftig mit der datenbank zusammen arbeiten")
print("das ist eine teständerung")
print("möchten sie dies ausqühren")
print("ja oder nein")
eingabe = input()
if eingabe == "ja":
    print("1 führ eine andere reinfolge aus")
    print("2 führ einen neuen eintrag hinzu")
    print("3 lösche einen eintrag")
    print("4 ändere einen eintrag")
    print("5 speichere die ergebnisse in einer datei")
    print("6 beenden")
    eingabe = int(input())
    if eingabe == 1:
        essen.reverse()
        print(essen)
    elif eingabe == 2:
        neu = input("was möchten sie hinzufügen")
        essen.append(neu)
        print(essen)
    elif eingabe == 3:
        löschen = input("was möchten sie löschen")
        essen.remove(löschen)
        print(essen)
    elif eingabe == 4:
        ändern = input("was möchten sie ändern")
        essen.remove(ändern)
        neu = input("was möchten sie ändern")
        essen.append(neu)
        print(essen)
    elif eingabe == 5:
        print("speichere die ergebnisse in einer datei")
        datei = open("essenmain.txt", "w")
        datei.write(str(essen))
        datei.close()
        print("datei gespeichert")
        print("sie finden die datei unter dem ordner essensplaner")
    elif eingabe == 6:
        print("ende")
    else:
        print("falsche eingabe")
        print("wild")
elif eingabe == "nein":
    print("ende") 
    print("final")
else:
    print("falsche eingabe")
    print("wild")
    print("ende")
