
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin_kerros or kohde > self.ylin_kerros:
            print("Kerros ei ole sallittu!")
            return

        while self.nykyinen_kerros < kohde:
            self.kerros_ylös()

        while self.nykyinen_kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []

        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        print(f"Hissi {hissin_numero} liikkuu:")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)



talo = Talo(1, 10, 3)

talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)
talo.aja_hissiä(3, 4)
talo.aja_hissiä(1, 1)
