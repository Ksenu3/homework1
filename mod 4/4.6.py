import random

N = int(input("Kuinka monta pistettä arvotaan: "))
pisteet = N

n = 0

while N > 0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n = n + 1

    N = N - 1

pi = 4 * n / pisteet

print(f"Piin likiarvo: {pi}")