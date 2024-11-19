class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        """Alustaa hissin, joka on aina alimmassa kerroksessa."""
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros
        print(f"Hissi on alimmassa kerroksessa: {self.kerros}")

    def siirry_kerrokseen(self, tavoite_kerros):
        """Siirtää hissin haluttuun kerrokseen kutsumalla kerros_ylös tai kerros_alas."""
        while self.kerros < tavoite_kerros:
            self.kerros_ylös()
        while self.kerros > tavoite_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        """Siirtää hissiä yhden kerroksen ylöspäin."""
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa, ei voi siirtyä ylöspäin.")

    def kerros_alas(self):
        """Siirtää hissiä yhden kerroksen alaspäin."""
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi on kerroksessa {self.kerros}")
        else:
            print("Hissi on jo alimassa kerroksessa, ei voi siirtyä alaspäin.")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        """Alustaa talon, jossa luodaan tarvittavat hissit."""
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []

        # Luodaan hissit
        for _ in range(hissien_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        """Ajaa halutun hissin haluttuun kerrokseen."""
        if 0 <= hissin_numero < len(self.hissit):
            print(f"\nAjetaan hissi {hissin_numero + 1} kerrokseen {kohde_kerros}:")
            self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virheellinen hissin numero.")


# Testataan Talo-luokkaa
def main():
    # Luodaan talo, jossa on 3 hissiä ja kerrokset 1-5
    talo = Talo(1, 5, 3)

    # Ajetaan ensimmäinen hissi kerrokseen 4
    talo.aja_hissiä(0, 4)

    # Ajetaan toinen hissi kerrokseen 5
    talo.aja_hissiä(1, 5)

    # Ajetaan kolmas hissi kerrokseen 2
    talo.aja_hissiä(2, 2)

    # Ajetaan ensimmäinen hissi takaisin alimpaan kerrokseen
    talo.aja_hissiä(0, 1)


# Ajetaan pääohjelma
if __name__ == "__main__":
    main()
