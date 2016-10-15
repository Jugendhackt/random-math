import json


def generateJsonDatei(Aufgabentyp,Aufgabe,Tipp,Loesung):
    information = {
        'Aufgbentyp': Aufgabentyp,
        'Aufgbe': Aufgabe,
        'Tipp': Tipp,
        'Loesung': Loesung,
    }

    with open('data.json', 'w') as outfile:
        json.dump(information, outfile);


generateJsonDatei("Typ", "Aufgabe", "Tipp", 42);
