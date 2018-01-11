#Zadatak 4 - Vezba 2

# -*- coding: utf-8 -*-

def main():
    niz1 = raw_input("Uneti elemente prvog niza : ")
    niz2 = raw_input("Uneti elemente drugog niza : ")
    n1 = niz1.split(",")
    n2 = niz2.split(",")
    op = raw_input("p - prvo element prvog niza, d - prvo element drugog niza ")
    if op == 'p':
        o = True
    else:
        o = False
    print (naizmenicno(n1, n2, o))

def naizmenicno(niz1, niz2, o):
    i = 0
    r = list()
    if len(niz1) > len(niz2):
        d = len(niz1)
    else:
        d = len(niz2)
    while i < d:
        if o:
            r.append(int(niz1[i]))
            r.append(int(niz2[i]))
        else:
            r.append(int(niz2[i]))
            r.append(int(niz1[i]))
        i+=1
    return r

main()