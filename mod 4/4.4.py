import random
noppa = random.randint(1, 10)

while True:
    luku = int(input('Arvaa luku:'))

    if luku < noppa:
        print('Liian pieni arvaus.')
    elif luku > noppa:
        print('Liian suuri arvaus.')
    else:
        print('Oikein!')
        break

#random.randint(a:1, b:10) → pitäisi olla random.randint(1, 10)
#luku pitää antaa arvo ennen while-ehtoa, tai käyttää while True
#noppa1 = noppa on turha, voit käyttää suoraan noppa-muuttujaa.