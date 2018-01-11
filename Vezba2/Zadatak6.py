#Zadatak 6 - Vezba 2

# -*- coding: utf-8 -*-
import numpy as np
br_tacaka=input("Uneti broj tacaka: ")
x=[]
y=[]

i=0
while i < br_tacaka:
    x.append(input("Uneti x koordinatu: "))
    y.append(input("Uneti y koordinatu: "))
    i=i+1

stepen=input("Uneti stepen polinoma: ")
koefcijent=np.polyfit(x,y,stepen)
fitovanje=np.poly1d(koefcijent)

print "Polinom :",fitovanje
