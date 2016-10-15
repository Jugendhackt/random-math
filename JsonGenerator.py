import json


def generateJsonDatei(Aufgabentyp,Aufgabe,Loesung,Tipp,Schritte = None):
    
    return {"Physik_Pendel" : json.dumps({'Aufgabentyp': Aufgabentyp,'Aufgabe': Aufgabe,'Tipp': Tipp,'Loesung': Loesung}),
            "Polynom_Nullstellen" : json.dumps({'Aufgabentyp': Aufgabentyp,'Aufgabe': Aufgabe,'Tipp': Tipp,'Schritte': Schritte,'Loesung': Loesung})}.get(Aufgabentyp)
     
