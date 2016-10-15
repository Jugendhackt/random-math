import json


def generateJsonDatei(Aufgabentyp,Aufgabe,Tipp,Loesung):
    information = {
        'Aufgabentyp': Aufgabentyp,
        'Aufgabe': Aufgabe,
        'Tipp': Tipp,
        'Loesung': Loesung,
    }

    return json.dumps(information)


generateJsonDatei("Typ", "Aufgabe", "Tipp", 42)