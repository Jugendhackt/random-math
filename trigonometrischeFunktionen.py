#Aufgabe: momentane Auslenkung berechnen bei gegebener Fraquenz, Zeit, max. Auslenkung
import random
import math
import JsonGenerator

class TrigonometriePendel(object):
    typ = None

    def __init__(self):
        self.typ = "Physik_Pendel"
        self.phase = 0
        self.frequenz = 0
        self.amplitude = 0
        self.tipp = "Die Formel = s(t) = amplitude * sin(2 * pi * frequenz + phase)"

    def aufgabenText(self):
        return "Berechne die momentane Auslenkung des Fadenpendels bei einer Sekunde, max. Auslenkung: %d, Frequenz %d, Phase %d"\
            %(self.amplitude, self.frequenz, self.phase)

    def aufgabeErstellen(self):
        self.phase = random.randrange(0, 6)
        self.frequenz = random.randrange(1, 4)
        self.amplitude = random.randrange(2, 5)

    def tipp(self):
        return self.tipp


    def loesung(self):
        return round(self.amplitude * math.sin(2 * math.pi * self.frequenz + self.phase), 2)

    def anJson(self):
        self.aufgabeErstellen()
        return JsonGenerator.generateJsonDatei(self.typ, self.aufgabenText(), [self.loesung()], self.tipp)

