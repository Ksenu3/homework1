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


auto = Auto("ABC-123", 142)

auto.kiihdytä(60)
auto.kulje(1.5)

print("Kuljettu matka:", auto.kmatka, "km")