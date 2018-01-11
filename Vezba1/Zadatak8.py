#Zadatak 8 - Vezba 1

# -*- coding: utf-8 -*-


import random
broj_pogadjanja = 0

print('Zdravo! Kako se zoves?')
ime = raw_input()

broj = random.randint(0, 100)


while broj_pogadjanja < 10:

  print('Uneti broj:')
  pogadjanje = input()
  pogadjanje = int(pogadjanje)

  broj_pogadjanja = broj_pogadjanja + 1

  if pogadjanje < broj:
     print('Uneti broj je manji od zamisljenog broj.')


  if pogadjanje > broj:
     print('Broj je veci od zamisljenog broja.')


  if pogadjanje == broj:
     break



if pogadjanje == broj:
   broj_pogadjanja = str(broj_pogadjanja)
   print('Bravo, ' + ime + '! Pogodili ste broj iz  ' + broj_pogadjanja + ' pokusaja!')


if pogadjanje!= broj:
   broj = str(broj)
   print('Pogresili ste. Zamisljeni broj je: ' + broj)