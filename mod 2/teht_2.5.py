le = float(input('Anna leiviskät:'))
na = float(input('Anna naulat:'))
lu = float(input('Anna luodit:'))

lu1 = 13.3 * lu
na1 = 32 * 13.3 *  na
le1 = 32 * 13.3 * 20 * le

grammat = lu1 + na1 + le1
kilot = int(grammat // 1000)
loput = grammat % 1000

print(f'Massa nykymittojen mukaan:\n{kilot} kilogrammaa ja {loput:.1f} grammaa.')