# -*- coding: utf-8 -*-

class Sfera:
    broj = 0

    @classmethod
    def jedinicna(cls):
        cls.poluprecnik = 1.00
        jedinicna = Sfera(cls.poluprecnik, 0 , 0 , 0)
        return jedinicna

    @classmethod
    def sfxyz(cs, x, y, z):
        cs.poluprecnik = 1.00
        cs.xCentar = x
        cs.yCentar = y
        cs.zCentar = z
        sf = Sfera(cs.poluprecnik, x, y, z)
        return sf

    def __init__(self, r, x, y, z):
        self.poluprecnik = r
        self.xCentar = x
        self.yCentar = y
        self.zCentar = z
        Sfera.broj += 1

    def zapremina(self):
        if (self.poluprecnik == 1):
            self.volume = 1.3333333333 * 3.14
            return (self.volume)
        else:
            r = self.poluprecnik
            self.volume = 1.3333333333 * 3.14 * (r * r * r)
            return (self.volume)

    @staticmethod
    def brojKreiranihObjekata():
        return Sfera.broj
