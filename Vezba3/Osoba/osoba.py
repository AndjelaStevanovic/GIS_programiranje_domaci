# -*- coding: utf-8 -*-

from datetime import date

class Osoba:

    def __init__(self, ime, prezime, y, m, d, adresa):
        self.ime = ime
        self.prezime = prezime
        self.datum = date(y,m,d)
        self.adresa = adresa


class Djak(Osoba):

    def __init__(self, ime, prezime, y, m, d, adresa, skola, odd, godina):
        Osoba.__init__(self, ime, prezime, y, m, d, adresa)
        self.skola = skola
        self.odd = odd
        self.godina = godina

    def info(self):
        print "\nĐak", self.ime, self.prezime, "datum rođenja", self.datum, "kućna adresa", self.adresa,\
            "upisao je", self.godina, "godinu u odeljenju", self.odd, "u školi", self.skola
        return ""

    def odeljenje(self):
        return self.odd

    def obnovio(self):
        if self.godina > 1:
            print "Djak idu u razred", self.odd, "po ", self.godina, "put"
        else:
            return 0


class Zaposlen(Osoba):
    dani = []

    def __init__(self, ime, prezime, y, m, d, adresa, kompanija, department):
        Osoba.__init__(self, ime, prezime, y, m, d, adresa)
        self.kompanija = kompanija
        self.department = department

    @classmethod
    def radi(cls, y, m, d, y1, m1, d1):
        radio = []
        cls.poceo = date(y,m,d)
        cls.prekinuo = date(y1,m1,d1)
        radio.append(cls.poceo)
        radio.append(cls.prekinuo)
        ukupno = (cls.prekinuo - cls.poceo).days + 1
        radio.append(ukupno)
        Zaposlen.dani.append(ukupno)
        print "Zaposleni je bio u radnom odnosu u periodu od", radio

    def staz(self):
        dani = self.dani
        self.meseci = float(sum(dani) / 30.0)
        print "Zaposleni ima staz:", (self.meseci), "meseci"

    def info(self):                             # Informacije o zaposlen
        print "\nZaposleni", self.ime, self.prezime, "datum rođenja", self.datum, "kućna adresa", self.adresa, \
            "radi u", self.kompanija, "department", self.department, "\n"
        return ""