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


auto = Auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print("Auton nopeus:", auto.nopeus, "km/h")

auto.kiihdytä(-200)

print("Hätäjarrutuksen jälkeen:", auto.nopeus, "km/h")