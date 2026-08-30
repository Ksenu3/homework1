ktunnus = 'python'
salasana = 'rules'
kerrat = 0

while kerrat < 5:

    ktunnus1 = input('Käyttäjätunnus:')
    salasana1 = input('Salasana:')
    kerrat = kerrat +1

    if ktunnus1 == ktunnus and salasana1 == salasana:
        print('Tervetuloa')
        break

    print('Väärin.')
    if kerrat == 5:
        print('Pääsy evätty.')
#while < kuin arvo,jotta py;rii
#kerrat = kerrat + 1
#

