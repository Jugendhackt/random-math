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
    check = True
    while(check):
        check = False;
        Ergebnis = "";
        ZahlArray = []
        c = 0;
        while(dezimal >= basis):
            ZahlArray.append(dezimal % basis)
            dezimal = (dezimal-(dezimal % basis))/basis
            if c > 10:
                check = True
                break
        ZahlArray.append(dezimal % basis)
        
    ZahlArray.reverse()
    i = 0
    while(i < len(ZahlArray)):
        Ergebnis += str(ZahlArray[i])
        i+=1
    return int(Ergebnis)

def erzeugeSchritte(dezimal, basis):
    check = True
    while(check):
        modulo = 0;
        check = False;
        SchritteArray = []
        c = 0;
        while(dezimal >= basis):
            oldDezimal = dezimal
            modulo = dezimal % basis
            dezimal = (dezimal-(dezimal % basis))/basis
            SchritteArray.append(str(oldDezimal) + " % " + str(basis) + " = " + str(dezimal) + " Rest: " + str(modulo))
            if c > 10:
                check = True
                break
        oldDezimal = dezimal
        modulo = dezimal % basis
        SchritteArray.append(str(oldDezimal) + " % " + str(basis) + " = " + str(dezimal) + " Rest: " + str(modulo))
    return SchritteArray
        
def anJson(Aufgabentyp, Aufgabe, Loesung, Tipp, Schritte):
    return JsonGenerator.generateJsonDatei(Aufgabentyp, Aufgabe, [Loesung], Tipp, Schritte)


Aufgabe = erstelleAufgabe(Dezimal, Basis)
Loesung = loeseAufgabe(Dezimal, Basis)
Schritte = erzeugeSchritte(Dezimal, Basis)

print(anJson(Aufgabentyp, Aufgabe, Loesung, Tipp, Schritte))



print(Aufgabe, Dezimal, Basis, Loesung)
