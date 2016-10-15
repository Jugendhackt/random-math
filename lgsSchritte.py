import random
from copy import deepcopy

class LGSSchritte(object):
    def __init__(self, matrix, loesungen):
        self.matrix = matrix
        self.loesungen = loesungen
        self.matrixSpeichern = []
        self.veraenderungSpeichern = []
        self.gl_1Speichern = []
        self.gl_2Speichern = []
        self.aufgabe = []

    def verkomplizieren(self, Lmatrix):
        for x in range(3):
            self.matrixSpeichern.append(deepcopy(Lmatrix))
            while True:
                aendern = random.randint(0, 2)
                aendern_2 = random.randint(0, 2)
                gl_1 = Lmatrix[aendern]
                gl_2 = Lmatrix[aendern_2]

                if gl_1 != gl_2:
                    break
            self.gl_1Speichern.append(aendern)
            self.gl_2Speichern.append(aendern_2)

            i = random.randint(1, 5)
            self.veraenderungSpeichern.append(i)

            for x in range(4):
                gl_1[x] *= i
            for x in range(4):
                gl_1[x] += gl_2[x]
            Lmatrix[aendern] = gl_1
            self.matrixSpeichern.append(deepcopy(Lmatrix))
            self.aufgabe = deepcopy(Lmatrix)

            self.aufgabe = self.aufgabeSchoen()

    def aufgabeSchoen(self):
        antwort = "Gegeben sind die Gleichungen: \n"
        for gleichung in self.aufgabe:
            antwort += "%d * a + %d * b + %d * c = %d \n"%(gleichung[0], gleichung[1], gleichung[2], gleichung[3])
        antwort += "Berechne a, b und c"
        return antwort

    def rueckwaerts(self):
        gesamtantwort = []
        antwort = ""
        c = len(self.gl_1Speichern) - 1

        self.matrixSpeichern.reverse()
        self.gl_1Speichern.reverse()
        self.gl_2Speichern.reverse()
        self.veraenderungSpeichern.reverse()

        a = 1

        for matrix in self.matrixSpeichern:
            antwort += str(matrix)
            if a == 1:
                antwort += "    Gleichung Nummer %d von Gleichung %d abziehen und das Ergebnis durch %d teilen \n"\
                           %(self.gl_1Speichern[c] + 1, self.gl_2Speichern[c] + 1, self.veraenderungSpeichern[c])
                c = c-1
            if a == -1:
                antwort += "    folgt daraus. \n"
                gesamtantwort.append(antwort)
                antwort = ""
            a = a*-1
        antwort += "Achtung!!, dies ist kein effizienter Loesungsweg"
        return gesamtantwort




