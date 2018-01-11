# -*- coding: utf-8 -*-

from inzenjer import *

def main():
    # Kreiranje objekata
    I = Inzenjer("Andjela", "Stevanovic", "1205994786045", "2")
    G = GeodetskiInzenjer("Dzeneta", "Kozica", "2506994568024", None , 2)
    E = ElektroInzenjer("Milena", "Simic", "0204993459120", "23", 3)

    print I.ime, I.prezime
    print (I.info())
    print (G.info2())
    print (G.imaLicencu())
    G.licenca = 999
    print (G.imaLicencu())
    print (E.ime)
    print (E.licenca)
    print (E.info2())


if __name__ == '__main__':
    main()