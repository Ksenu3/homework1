import random

maara = int(input("Arpakuutioiden lukumäärä: "))

summa = 0

for i in range(maara):
    noppa = random.randint(1, 6)
    summa = summa + noppa

print(f"Silmälukujen summa: {summa}")