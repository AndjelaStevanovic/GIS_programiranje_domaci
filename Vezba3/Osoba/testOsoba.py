# -*- coding: utf-8 -*-

from osoba import *

def main():
    D = Djak("Anđela", "Stevanović", 2003, 2, 14, "ul. Crnogorska br. 6", "Dragomir Marković", "5", 4)
    D2 = Dzak("Milena", "Vasiljević", 2003, 4, 24 , "ul. Kninska br. 14", "Dragomir Marković", "7", 3)

    Z = Zaposlen("Kristina", "Radičević", 1984, 3, 11 , "ul. Šajkaška br. 4" , "Top Geo" , None)

    D.info()
    D.odelenje()
    D.obnovio()
    D2.info()
    D2.obnovio()

    Z.info()
    Z.radi(2013,6,5,2013,12,5)
    Z.radi(2015,10,12,2016,10,28)
    Z.staz()


    print "\nKreiranje novog zaposlenog"
    i = raw_input("Ime: ")
    p = raw_input("Prezme: ")
    y = int(input("Godina rođenja: "))
    m = int(input("Mesec rođenja: "))
    d = int(input("Dan rođenja: "))
    a = raw_input("Adresa: ")
    k = raw_input("Kompanija: ")
    dep = raw_input("Department: ")

    o = Zaposlen(i, p, y, m, d, a, k, dep)
    o.info()

if __name__ == '__main__':
    main()