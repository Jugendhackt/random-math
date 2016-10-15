import random
import math
import lgsSchritte

class LGS(object):
    def __init__(self):
        self.loesungen = [0, 0, 0]
        self.typ = "Lineares Gleichungssytem"
        self.tipp = ""
        self.lgs = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



    def anJson(self):
        fakListe = []
        for x in range(3):
            print(x)
            self.loesungen[x] = random.randint(1, 5)

        for faktor in range(6):
            fakListe.append(random.randint(1,10))

        nummer = 1
        for gleichung in self.lgs:
            for x in range(nummer):
                gleichung[x] = self.zufall1_15()
            nummer += 1
            ergebnis = 0

            ergebnis = gleichung[0] * self.loesungen[0] + gleichung[1] * self.loesungen[1] + gleichung[2] * self.loesungen[2]
            gleichung[3] = ergebnis

        lgs_schritte = lgsSchritte.LGSSchritte(self.lgs, self.loesungen)
        lgs_schritte.verkomplizieren(lgs_schritte.matrix)
        schritte = lgs_schritte.rueckwaerts()

        anJson = [self.typ, lgs_schritte.aufgabe , self.loesungen, "Believe in Yourself!" , schritte]
        return anJson

        """erg_1 = fakListe[0] * self.x1
        self.tipp += "%d = %d * x1 \n"%(erg_1, fakListe[0])
        erg_2 = fakListe[1] *self.x1 + fakListe[2] * self.x2
        self.tipp += "%d = %d * x1 + %d * x2 \n"%(erg_2, fakListe[1], fakListe[2])
        erg_3 = fakListe[3] * self.x1 + fakListe[4] * self.x2 + fakListe[5] * self.x3
        self.tipp += "%d = %d * x1 + %d * x2 + %d * x3"%(erg_3, fakListe[3], fakListe[4], fakListe[5])"""

    def zufall1_15(self):
        return random.randint(1, 15)

"""
lgs = LGS()
lgs.anJson()


"""
