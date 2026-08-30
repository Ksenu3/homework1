luvut = []
luku = input('Anna ensimmäinen luku, tyhjä lopettaa:')
while luku != '':
    luvut.append(int(luku))
    luku = input('Anna seuraava luku, tyhjä lopettaa:')
luvut.sort()
print(luvut)

#Käyttäjä kirjoittaa esimerkiksi 5 → luku on ensin merkkijono "5".
#Koska se ei ole tyhjä, int(luku) muuttaa sen kokonaisluvuksi.
#Tyhjä syöte '' lopettaa while-silmukan. != ,eri kuin
#luvut.sort() järjestää luvut pienimmästä suurimpaan.