# -*- coding: utf-8 -*-

class Inzenjer():
    def __init__(self, ime, prezime, jmbg, licenca):
        self._ime = ime
        self._prezime = prezime
        self._jmbg = jmbg
        self._licenca = licenca

    @property
    def ime(self):
        return self._ime

    @property
    def prezime(self):
        return self._prezime

    @property
    def jmbg(self):
        return self._jmbg

    @property
    def licenca(self):
        return self._licenca

    @ime.setter
    def ime(self, ime):
        self._ime = ime

    @prezime.setter
    def prezime(self, prezime):
        self._prezime = prezime

    @jmbg.setter
    def jmbg(self, jmbg):
        self._jmbg = jmbg

    @licenca.setter
    def licenca(self, licenca):
        self._licenca = licenca

    def info(self):
        print "Inženjer:", self.ime, self.prezime, ", JMBG:", self.jmbg
        return ""

class GeodetskiInzenjer(Inzenjer):
    def __init__(self,ime, prezime, jmbg, licenca, staz):
        Inzenjer.__init__(self, ime, prezime, jmbg, licenca)
        self._staz = staz

    @property
    def staz(self):
        return self._staz

    @staz.setter
    def staz(self, staz):
        self._staz = staz

    def info2(self):
        print self.info() + "Broj godina radnog staža je:", self.staz
        return ""

    def imaLicencu(self):
        if self.licenca is not None:
            print "Broj licence je: ", self.licenca
        else:
            print "Inženjer nema licencu"
        return ""

class ElektroInzenjer(Inzenjer):
    def __init__(self, ime, prezime, jmbg, licenca, projekti):
        Inzenjer.__init__(self, ime, prezime, jmbg, licenca)
        self._projekti = projekti

    @property
    def projekti(self):
        return self._projekti

    @projekte.setter
    def projekte(self, projekti):
        self._projekti = projekti

    def info2(self):
        print self.info() + "Broj projekata na kojima je do sada radio je:", self.projekti
        return ""

    def imaLicencu(self):
        if self.licenca is not None:
            print "Broj licence je: ", self.licenca
        else:
            print "Inženjer nema licencu"
        return ""

