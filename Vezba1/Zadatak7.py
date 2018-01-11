# Zadatak 7 - Vezba 1

# -*- coding: utf-8 -*-

import math

import math

def rastojanje(a1, b1, a2, b2):
    duzina = math.sqrt((a1 - a2)**2 + (b1 - b2)**2)
    return duzina

xa = int(input('Uneti x koordinatu za tacku A: '))
ya = int(input('Uneti y koordinatu za tacku A: '))
xb = int(input('Uneti x koordinatu za tacku B: '))
yb = int(input('Uneti y koordinatu za tacku B: '))
xc = int(input('Uneti x koordinatu za tacku C: '))
yc = int(input('Uneti y koordinatu za tacku C: '))

x = int(input('Uneti x koordinatu za tacku M: '))
y = int(input('Uneti y koordinatu za tacku M: '))

AB = rastojanje(xa, ya, xb, yb)
BC = rastojanje(xb, yb, xc, yc)
AC = rastojanje(xa, ya, xc, yc)

EA = rastojanje(x, y, xa, ya)
EB = rastojanje(x, y, xb, yb)
EC = rastojanje(x, y, xc, yc)

AEB = math.acos((EA * EA + EB * EB - AB * AB) / (2 * EA * EB))
BEC = math.acos((EB * EB + EC * EC - BC * BC) / (2 * EB * EC))
CEA = math.acos((EA * EA + EC * EC - AC * AC) / (2 * EA * EC))

ugao = math.degrees(AEB) + math.degrees(BEC) + math.degrees(CEA)

print round(ugao, 1)

if (round(ugao, 1) == 360.0):
    print "\nDA"
else:
    print "\nNE"