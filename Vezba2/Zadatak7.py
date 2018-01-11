#Zadatak 7 - Vezba 2

# -*- coding: utf-8 -*-

import random
a=int(random.uniform(0,51))

def deli(karte,listaRandom):
    i=0
    while i==0:
        r = int(random.uniform(0, 51))
        a = listaRandom.count(r)
        if a==0:
            i=1
        else:
            i=0
    pov=[]
    pov.append(karte[r])
    pov.append(r)
    return pov

def vrednost(lista,spil):
    i = 0
    igrac = 0
    b=0
    while i < len(lista):
        if int(spil[lista[i]])!=1:
            igrac = igrac + int(spil[lista[i]])
        else:
            b+=1
        i += 1
    j=0
    while j<b:
        if igrac>=12:
            igrac=igrac+1
        else:
            igrac=igrac+10
        j+=1

    return igrac

def stampa(lista):
    i=0
    while i<len(lista):
        print lista[i]
        i+=1

def uslov1(racunar,igrac):
    if (racunar<21 and igrac<21):
        return 1
    else:
        return 0

karte=['Srce As','Srce 2','Srce 3','Srce 4','Srce 5','Srce 6','Srce 7','Srce 8','Srce 9','Srce 10','Srce Zandar','Srce Dama','Srce Kralj',
       'Kocka As', 'Kocka 2', 'Kocka 3', 'Kocka 4', 'Kocka 5', 'Kocka 6', 'Kocka 7', 'Kocka 8', 'Kocka 9', 'Kocka 10', 'Kocka Zandar', 'Kocka Dama', 'Kocka Kralj'
       'Tref As', 'Tref 2', 'Tref 3', 'Tref 4', 'Tref 5', 'Tref 6', 'Tref 7', 'Tref 8', 'Tref 9', 'Tref 10','Tref Zandar', 'Tref Dama', 'Tref Kralj',
       'Pik As', 'Pik 2', 'Pik 3', 'Pik 4', 'Pik 5', 'Pik 6', 'Pik 7', 'Pik 8', 'Pik 9', 'Pik 10','Pik Zandar', 'Pik Dama', 'Pik Kralj']

spil = dict([('Srce As',1), ('Srce 2',2),('Srce 3',3), ('Srce 4',4),('Srce 5',5), ('Srce 6',6),('Srce 7',7), ('Srce 8',8),('Srce 9',9), ('Srce 10',10),('Srce Zandar',10), ('Srce Dama',10),('Srce Kralj',10),
            ('Kocka As', 1), ('Kocka 2', 2), ('Kocka 3', 3), ('Kocka 4', 4), ('Kocka 5', 5), ('Kocka 6', 6), ('Kocka 7', 7),('Kocka 8', 8), ('Kocka 9', 9), ('Kocka 10', 10), ('Kocka Zandar', 10), ('Kocka Dama', 10), ('Kocka Kralj', 10),
             ('Tref As', 1), ('Tref 2', 2), ('Tref 3', 3), ('Tref 4', 4), ('Tref 5', 5), ('Tref 6', 6), ('Tref 7', 7),('Tref 8', 8), ('Tref 9', 9), ('Tref 10', 10), ('Tref Zandar', 10), ('Tref Dama', 10), ('Tref Kralj', 10),
             ('Pik As', 1), ('Pik 2', 2), ('Pik 3', 3), ('Pik 4', 4), ('Pik 5', 5), ('Pik 6', 6), ('Pik 7', 7),('Pik 8', 8), ('Pik 9', 9), ('Pik 10', 10), ('Pik Zandar', 10), ('Pik Dama', 10), ('Pik Kralj', 10)])

ime=raw_input("Uneti ime:  ")
listaIgrac=[]
listaRacunar=[]
listaRandom=[]

i=0
while i<2:
    pdi=[]
    pdi=deli(karte,listaRandom)
    listaIgrac.append(pdi[0])
    listaRandom.append(pdi[1])
    i+=1
ra=0
while ra<2:
    pdr=[]
    pdr=deli(karte,listaRandom)
    listaRandom.append(pdr[1])
    listaRacunar.append(pdr[0])
    ra+=1

racunar=vrednost(listaRacunar,spil)
igrac=vrednost(listaIgrac,spil)
stampa(listaIgrac)
provera=int(uslov1(racunar,igrac))
while provera==1:
    no = raw_input("Zelite i da nastavite igru? (DA ili NE) ")
    if no == "DA":
        a=deli(karte,listaRandom)
        listaIgrac.append(a[0])
        listaRandom.append(a[1])
        ra=deli(karte,listaRandom)
        listaRacunar.append(ra[0])
        listaRandom.append(ra[1])
        print "Nova karta je:  ",a[0]
        racunar=vrednost(listaRacunar, spil)
        igrac=vrednost(listaIgrac, spil)
        provera=int(uslov1(racunar,igrac))
    else:
        print "Igrac je odustao"
        provera=0
        igrac=igrac+20

if racunar==21:
    print "Pobednik je racunar i vrednost osvojenih bodova je 21!"
elif igrac==21:
    print "Cestitamo! Pobednik je ",ime," i broj vrednost osvojenih bodova je 21!"
elif igrac<21:
    print "Cestitamo! Pobednik je ",ime," i broj vrednost osvojenih bodova je: " ,vrednost(listaIgrac,spil)
elif racunar<21:
    print "Pobednik je racunar i vrednost osvojenih bodova je: ",vrednost(listaRacunar,spil)
elif  igrac>21 and igrac>racunar:
    print "Zao nam je. Igrac ",ime," je izgubio i broj vrednost osvojenih bodova je:  ", vrednost(listaIgrac,spil)
elif racunar>21 and racunar>igrac:
    print "Racunar je izgubio i broj vrednost osvojenih bodova je: ", vrednost(listaRacunar,spil)
elif racunar==igrac:
    print "Nema pobednika"

if no=="DA":
    print "Vrednost igraca je  ",vrednost(listaIgrac,spil)
 karte_protiv=raw_input("Zelite li da vidite karte protivnika? (DA ili NE) ")
if karte_protiv=="DA":
    print "Karte koje je imao racunar"
    stampa(listaRacunar)
    print "Vrednost racunara je ", vrednost(listaRacunar,spil)