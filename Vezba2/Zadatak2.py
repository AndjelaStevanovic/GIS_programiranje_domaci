#Zadatak 2 - Vezba 2

# -*- coding: utf-8 -*-

def sumaElemenata(lista):
    zbir = 0
    for i in lista:
        zbir = zbir + i
    return zbir

def main():
    unos = raw_input('Uneti niz brojeva : ')
    lista = map(int, unos.split(','))
    print lista

    suma = sumaElemenata(lista)

    print "Suma brojeva u nizu je:",suma

main()