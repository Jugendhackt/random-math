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

    def verkomplizieren(self, Lmatrix):
        for x in range(3):
            print(Lmatrix)
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

    def rueckwaerts(self):
        antwort = "Die Schritte: \n"
        antwort += "x1: %d, x2: %d, x3: %d \n"%(self.loesungen[0], self.loesungen[1], self.loesungen[2])

        c = len(self.gl_1Speichern) - 1

        self.matrixSpeichern.reverse()
        self.gl_1Speichern.reverse()
        self.gl_2Speichern.reverse()
        self.veraenderungSpeichern.reverse()

        a = 1

        for matrix in self.matrixSpeichern:
            print("m")
            print(matrix)
            antwort += str(matrix)
            if a == 1:
                antwort += "    Gleichung Nummer %d von Gleichung %d abziehen und das Ergebnis durch %d teilen \n"\
                           %(self.gl_1Speichern[c] + 1, self.gl_2Speichern[c] + 1, self.veraenderungSpeichern[c])
                c = c-1
            if a == -1:
                antwort += "    folgt daraus. \n"
            a = a*-1
        antwort += "Achtung!!, dies ist kein effizienter Loesungsweg"
        return antwort




