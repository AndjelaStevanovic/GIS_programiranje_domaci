# -*- coding: utf-8 -*-

from python import *

def main():

    c = int(input("Broj tacaka je: "))
    p = Povrs(c)
    print "\nBroj tacaka je: ", p.br()
    print "Poligon: ", p.povrs, "ima povrsinu od: ", p.areaPoligona()
    print "\nSredina poligona je:", p.centroid()
    print "\nMaksimalne vrednosti koordinata tačaka površi:", p.max()
    print "Minimalne vrednosti koordinata tačaka površi:", p.min()
    print "\nTacke sa odgovarajim indeksom kao Id:\n", p.index()
    print "\nDve najbliže tacke su", p.minPar(), "a rastojanje među njima je", p.minRastojanje()
    print "Elevacija između dve tacke, najniža i najviša", p.maxPar(), "je", p.maxElevacija()
    print "\nOperator: ", p.metadataO

if __name__ == '__main__':
    main()