# Zadatak 4 - Vezba 1

# -*- coding: utf-8 -*-

broj1 = int(input("Uneti prvi  broj: "))
broj2 = int(input("Uneti drugi broj: "))

zbir = 0

while (broj2 > 0):
    n = broj2 % 10
    zbir = zbir + n
    broj2 = broj2 // 10

print("\n Suma cifara drugog  broja je : %d" % zbir)

cifre = []

while broj1> 0:
    cifre.append(broj1%10)
    broj1 //= 10

s = 0
p = 0
i = 0
for cifra in reversed(cifre):
    if i%2 == 0:
        s += cifra
    else:
        p += cifra
    i += 1

print '\n Razlika zbira cifara prvog broja na parnim i neparnim pozicijama je: ', s-p