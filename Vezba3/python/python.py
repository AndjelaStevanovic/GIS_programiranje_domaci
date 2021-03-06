# -*- coding: utf-8 -*-

import random
import math
import itertools

class Povrs:

    ime = raw_input("Ime operatera: ")
    prezime = raw_input("Prezime operatera: ")
    mail = raw_input("e-mail operatera: ")

    metadataO = []
    metadataO.append(ime)
    metadataO.append(prezime)
    metadataO.append(mail)

    def __init__(self, c):
        self.c = c
        self.i = 0
        self.povrs = []
        while (self.i < self.c):
            self.x = random.randint(0, 100)
            self.y = random.randint(0, 100)
            self.z = random.randint(0, 100)
            self.tacka = (self.x, self.y, self.z)
            self.povrs.append(self.tacka)
            self.i = self.i + 1

    def br(self):
        return self.i

    def areaPoligona(self):
        n = len(self.povrs)
        self.area = 0.0
        for i in range(n):
            j = (i + 1) % n
            self.area += self.povrs[i][0] * self.povrs[j][1]
            self.area -= self.povrs[j][0] * self.povrs[i][1]
        self.area = abs(self.area) / 2.0
        return self.area

    def centroid(self):                                         # Sredina poligona
        self.centroide = ((sum(d[0] for d in self.povrs)) / len(self.povrs), (sum(d[1] for d in self.povrs)) / len(self.povrs))
        return self.centroide

    def max(self):                                              # Maksimalna tačka
        self.maksimalnu = max(self.povrs, key=lambda item: item[0:1])
        return self.maksimalnu

    def min(self):                                              # Minimalna tačka
        self.minimalnu = min(self.povrs, key=lambda item: item[0:1])
        return self.minimalnu

    def index(self):                                 
        self.metadata = [(ix, self.povrs[ix]) for ix in range(len(self.povrs))]
        return self.metadata

    def rastojanje(self):
        p0 = self.povrs
        p1 = self.povrs
        return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

    def minPar(self):
        self.minP = min(itertools.combinations(self.povrs, 2))
        return self.minP

    def minRastojanje(self):
        p0 = self.minP[0]
        p1 = self.minP[1]
        return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

    def elevacija(self):
        p0, p1 = self.povrs
        return (p0[2] - p1[2])

    def maxPar(self):
        self.maxP = max(itertools.combinations(self.povrs, 2))
        return self.maxP

    def maxElevacija(self):
        p0 = self.maxP[0]
        p1 = self.maxP[1]
        return (p0[2] - p1[2])

