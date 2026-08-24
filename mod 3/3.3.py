sp = input('Sukupuoli:')
a = int(input('Hemoglobiiniarvo:'))

if sp == 'nainen':
    if a >= 117 and a <= 175:
        print('Hemoglobiiniarvo on normaali')

    elif a < 117:
        print('Hemoglobiiniarvo on alhainen')

    else:
        print('Hemoglobiiniarvo on korkea')

elif sp == 'mies':
    if a >= 134 and a <= 195:
        print('Hemoglobiiniarvo on normaali')

    elif a < 134:
        print('Hemoglobiiniarvo on alhainen')

    elif a > 195:
        print('Hemoglobiiniarvo on korkea')
