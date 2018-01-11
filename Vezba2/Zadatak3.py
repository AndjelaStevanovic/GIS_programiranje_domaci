#Zadatak 3 - Vezba 2

# -*- coding: utf-8 -*-


def proizvodElemenata(lista):
    proizvod = 1
    for i in lista:
        proizvod = proizvod * i
    return proizvod

def main():
    unos = raw_input('Uneti niz brojeva : ')
    lista = map(int, unos.split(','))
    print lista

    proizvod = proizvodElemenata(lista)

    print "Proizvod brojeva u nizu je:",proizvod

main()