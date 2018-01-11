# Zadatak 2 - Vezba 1

# -*- coding: utf-8 -*-

x = float(input("Uneti prvi broj: "))
y = float(input("Uneti drugi broj: "))

print("Vrednost za x je: ") + str(x)
print("Vrednost za y je: ") + str(y)
print str(x) + (" + ") + str(y) + (" = ") + str(x + y)
print str(x) + (" - ") + str(y) + (" = ") + str(x - y)
print str(x) + (" * ") + str(y) + (" = ") + str(x * y)
a = (x/y)
print str(x) + (" / ") + str(y) + (" = ") + ("%.2f" %a)
print("Ceo broj delenja x sa y je: ") + str(x // y)
print("Ostatak delenja x sa y je: ") + str(x % y)