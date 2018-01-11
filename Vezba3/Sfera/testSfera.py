# -*- coding: utf-8 -*-

from sfera import *

def main():
    print "Broj kreiranih objekata je: ", Sfera.brojKreiranihObjekata()

    # Kreiranje objekata
    sfera = Sfera(4.00, 0, 0, 0)
    globus = Sfera(12, 1.0, 1.0, 1.0)
    bilijarska_lopta = Sfera.sfxyz(10.0, 10.0, 0.0)
    jedinicna_sfera = Sfera.jedinicna()

    print "\nBroj kreiranih objekata je: ", Sfera.brojKreiranihObjekata()
    print "\nZapremina sfere je: ", sfera.zapremina()
    print "Zapremina globusa je: ", globus.zapremina()
    print "Zapremina biljarske lopte je: ", bilijarska_lopta.zapremina()
    print "Zapremina jedinicne sfere je: ", jedinicna_sfera.zapremina()


if __name__ == '__main__':
    main()