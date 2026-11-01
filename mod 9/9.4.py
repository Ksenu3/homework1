import random

class Auto:
    def __init__(self, rtunnus, huippunopeus):
        self.rtunnus = rtunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kmatka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kmatka += self.nopeus * tunnit


autot = []

for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100, 200))
    autot.append(auto)


kilpailu = True

while kilpailu:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

        if auto.kmatka >= 10000:
            kilpailu = False


print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<18}{'Nopeus':<15}{'Matka':<15}")

for auto in autot:
    print(f"{auto.rtunnus:<18}{auto.huippunopeus:<18}{auto.nopeus:<15}{auto.kmatka:<15}")