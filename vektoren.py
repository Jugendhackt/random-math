import random
import math

class Vektoren(object):
    def __init__(self):
        self.vektor_1 = [0, 0, 0]
        self.vektor_2 = [0, 0, 0]


    def vektorErstellen(self):
        for i in range(3):
            self.vektor_1[i] = random.randint(1, 5)
            self.vektor_2[i] = random.randint(1, 5)

    def laenge_vektor(self, vektor):
        return math.sqrt(math.pow(vektor, 2)+ math.pow(vektor, 2) + math.pow(vektor, 2))

    def winkelVektoren(self):
        oben = self.vektor_1[0] * self.vektor_2[0] + self.vektor_1[1] * self.vektor_2[1] + self.vektor_1[2] * self.vektor_2[2]
        unten = math.sqrt(self.laenge_vektor(self.vektor_1) * self.laenge_vektor(self.vektor_2))
        return math.acos(oben / unten)

    def anJson(self):

        wahl = random.randint(0, 1)
        if wahl == 0:
            aufgabe = "Berechne den Betrag des Vektors: x1: %d, x2: %d, x3: %d"%(self.vektor_1[0], self.vektor_1[1], self.vektor_1[2])
            antwort = self.laenge_vektor(self.vektor_1)
            anJson = ["Vektoren", aufgabe, antwort, "tipp fehlt", "keine Schritte"]
        else:
            aufgabe = "Welchen Winkel schliessen die beiden Vektoren ein? Vektor 1: x1: %d, x2: %d, x3: %d"%(self.vektor_1[0], self.vektor_1[1], self.vektor_1[2])
            aufgabe += " Vektor 2: x1: %d, x2: %d, x3: %d"%(self.vektor_2[0], self.vektor_2[1], self.vektor_2[2])
            antwort = self.winkelVektoren()
            anJson = ["Vektoren", aufgabe, antwort, "tipp fehlt", "keine Schritte"]
        return anJson










