# -*- coding: utf-8 -*-

import math
import copy

class Tacka:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return copy.deepcopy(self)

    def pomeraj(self, x_pomeraj, y_pomeraj):
        self.x = x_pomeraj + self.x
        self.y = y_pomeraj + self.y
        tacka = Tacka(self.x, self.y)
        return tacka

    def rastojanje(self):
        x = self.x
        y = self.y
        self.rastojanje = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
        return (self.rastojanje)



class Duz:
    tacka1 = Tacka(Tacka.x, Tacka.y)
    tacka2 = Tacka(Tacka.x, Tacka.y)

    @classmethod
    def duz(cls, tacka1, tacka2):
        cls.tacka1 = tacka1
        cls.tacka2 = tacka2
        return (cls(tacka1.x, tacka1.y, tacka2.x, tacka2.y))

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def duzina(self):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        self.duzina = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return (self.duzina)