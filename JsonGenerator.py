import json


def generateJsonDatei(Aufgabentyp,Aufgabe,Loesungen,Tipp,Schritte = None):

    i = 0
    Loesung = []
    while(len(Loesungen) > i):
        Loesung.append(str(Loesungen[i]))
        i = i + 1
    
    return {"Physik_Pendel" :
            json.dumps({'Aufgabentyp': Aufgabentyp,'Aufgabe': Aufgabe,'Tipp': Tipp,'Loesung': Loesung}),
            
            "Polynom_Nullstellen" :
            json.dumps({'Aufgabentyp': Aufgabentyp,'Aufgabe': Aufgabe,'Tipp': Tipp,'Schritte': Schritte,'Loesung': Loesung})}.get(Aufgabentyp)
     

print(generateJsonDatei("Polynom_Nullstellen","Aufgabe",[1,2,3],"Tipp"))
 
