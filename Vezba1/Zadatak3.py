# Zadatak 3 - Vezba 1

# -*- coding: utf-8 -*-

def rezultat(p1, p2):
    razp = p1 - p2
    razMinuti = ((razp - int(razp)) * 60)
    razSekunde = ((razMinuti - int(razMinuti)) * 60)
    rez = []
    rez.append(int(razp))
    rez.append(int(razMinuti))
    rez.append(int(round(razSekunde,0)))
    return rez

def uglovi():
    a = raw_input('Uneti prvi ugao u formatu xx xx xx : ')
    (stepeni, minuti, sekunde) = map(float, a.split(' '))

    b = raw_input('Uneti drugi ugao u formatu xx xx xx : ')
    (stepeni2, minuti2, sekunde2) = map(float, b.split(' '))

    p1 = stepeni + minuti / 60 + sekunde / 3600
    p2 = stepeni2 + minuti2 / 60 + sekunde2 / 3600

    (stepeni3, minuti3, sekunde3) = rezultat(p1,p2)

    print '\nRazlika dva uglova: ',int(stepeni),'°', int(minuti),"'", int(sekunde),'"', " i ", int(stepeni2),'°', int(minuti2),"'", int(sekunde2),'"',\
        'je:', int(stepeni3),'°', int(minuti3),"'", int(sekunde3),'"'

uglovi()