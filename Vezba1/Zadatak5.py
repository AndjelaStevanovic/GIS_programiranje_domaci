# Zadatak 5 - Vezba 1

# -*- coding: utf-8 -*-

x = int(input("Uneti petocifreni broj: "))

max = -1

for b in str(x):
    i = int(b)
    if i > max:
        max = i

print "\n Najveća cifra u petocifrenom broju je: ", max,
