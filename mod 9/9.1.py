class Auto:
    def __init__(self, rtunnus, huippunopeus):
        self.rtunnus = rtunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kmatka = 0


auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rtunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Nopeus:", auto.nopeus, "km/h")
print("Kuljettu matka:", auto.kmatka, "km")