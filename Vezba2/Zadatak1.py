#Zadatak 1 - Vezba 2

# -*- coding: utf-8 -*-
def sums(lista):
    total = 0
    for i in lista:
        if i % 2 == 0:
            total += i
    return total

def main():
    unos = raw_input('Uneti niz brojeva: ')
    lista = map(int, unos.split(','))
    print lista
    s = sums(lista)
    print 'Suma parnih elemenata u nizu je: ', s

main()