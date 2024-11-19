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


# Testataan luokkaa
def main():
    # Luodaan hissi, joka liikkuu kerroksissa 1-5
    hissi = Hissi(1, 5)

    # Siirretään hissi kerrokseen 5
    print("Siirretään hissi kerrokseen 5:")
    hissi.siirry_kerrokseen(5)

    # Siirretään hissi takaisin alimpaan kerrokseen
    print("\nSiirretään hissi takaisin alimpaan kerrokseen:")
    hissi.siirry_kerrokseen(1)


# Ajetaan pääohjelma
if __name__ == "__main__":
    main()
