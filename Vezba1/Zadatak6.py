# Zadatak 6 - Vezba 1

# -*- coding: utf-8 -*-

x = unicode(raw_input('Uneti pet karaktera: '))

cifre = sum(c.isdigit() for c in x)

print '\n Broj unetih cifara je: ' ,cifre