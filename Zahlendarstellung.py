from random import randint
import JsonGenerator

Aufgabentyp = "Zahlendarstellung"
Aufgabe = "";
Tipp = "Modulo hilft immer.";
Loesung = "";
Schritte = None;

Dezimal = randint(1,100)
Basis = randint(1, 9)

def erstelleAufgabe(dezimal, basis):
    return {1 : ("Stellen sie die Zahl " + str(dezimal) + " zur Basis " + str(basis) + " dar.")}.get(1)

def loeseAufgabe(dezimal, basis):
    Ergebnis = "";
    ZahlArray = []

    while(dezimal >= basis):
        ZahlArray.append(dezimal % basis)
        dezimal = (dezimal-(dezimal % basis))/basis
        
    ZahlArray.append(dezimal % basis)

    ZahlArray.reverse()
    i = 0

    while(i < len(ZahlArray)):
        Ergebnis += str(ZahlArray[i])
        i+=1

    return int(Ergebnis)

def erzeugeSchritte(dezimal, basis):
    SchritteArray = []
    while(dezimal >= basis):
        ZahlArray.append(dezimal % basis)
        dezimal = (dezimal-(dezimal % basis))/basis
        
def anJson(Aufgabentyp, Aufgabe, Loesung, Tipp):
    return JsonGenerator.generateJsonDatei(Aufgabentyp, Aufgabe, [Loesung], Tipp)


Aufgabe = erstelleAufgabe(Dezimal, Basis)
Loesung = loeseAufgabe(Dezimal, Basis)

print(anJson(Aufgabentyp, Aufgabe, Loesung, Tipp))



print(Aufgabe, Dezimal, Basis, Loesung)
