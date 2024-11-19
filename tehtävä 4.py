import random


class Auto:
    def __init__(self, nimi, nopeus, kuljettu_km=0):
        """Alustaa auton, jolla on nimi, alkuperäinen nopeus ja kuljettu kilometri."""
        self.nimi = nimi
        self.nopeus = nopeus
        self.kuljettu_km = kuljettu_km

    def kulje(self):
        """Simuloi auton matkaa tunnin ajan, lisätään kuljettua matkaa nopeuden mukaan."""
        self.kuljettu_km += self.nopeus
        print(f"{self.nimi} on ajanut {self.kuljettu_km:.1f} km.")

    def muuta_nopeutta(self):
        """Arpoo auton nopeuden muutoksen satunnaisesti (-5 km/h - +5 km/h)."""
        muutoksen_maara = random.randint(-5, 5)
        self.nopeus += muutoksen_maara
        if self.nopeus < 0:
            self.nopeus = 0  # Nopeus ei voi olla negatiivinen
        print(f"{self.nimi} nopeus muuttui: {muutoksen_maara} km/h, uusi nopeus: {self.nopeus} km/h.")


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        """Alustaa kilpailun, jossa on nimi, pituus ja lista autoista."""
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        """Simuloi tunnin kulumista: arpoo nopeuden muutokset ja ajaa autot."""
        for auto in self.autot:
            auto.muuta_nopeutta()  # Arvotaan auton nopeuden muutos
            auto.kulje()  # Ajetaan auto tunnin verran

    def tulosta_tilanne(self):
        """Tulostaa kilpailun tilanteen taulukkomuodossa."""
        print(f"\nKilpailu: {self.nimi}, Pituus: {self.pituus} km")
        print(f"{'Auto':<20}{'Nopeus (km/h)':<15}{'Kuljettu matka (km)'}")
        print("-" * 50)
        for auto in self.autot:
            print(f"{auto.nimi:<20}{auto.nopeus:<15}{auto.kuljettu_km:.1f}")

    def kilpailu_ohi(self):
        """Tarkistaa, onko kilpailu ohi (jos jokin autoista on ajanut koko matkan)."""
        for auto in self.autot:
            if auto.kuljettu_km >= self.pituus:
                return True
        return False


def main():
    # Luodaan kymmenen autoa
    autot = [
        Auto("Auto 1", random.randint(80, 120)),
        Auto("Auto 2", random.randint(80, 120)),
        Auto("Auto 3", random.randint(80, 120)),
        Auto("Auto 4", random.randint(80, 120)),
        Auto("Auto 5", random.randint(80, 120)),
        Auto("Auto 6", random.randint(80, 120)),
        Auto("Auto 7", random.randint(80, 120)),
        Auto("Auto 8", random.randint(80, 120)),
        Auto("Auto 9", random.randint(80, 120)),
        Auto("Auto 10", random.randint(80, 120)),
    ]

    # Luodaan kilpailu: "Suuri romuralli", pituus 8000 km
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    # Simuloidaan kilpailua
    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:  # Tulostetaan tilanne joka kymmenes tunti
            kilpailu.tulosta_tilanne()

    # Kilpailu on ohi, tulostetaan lopullinen tilanne
    print("\nKilpailu on ohi!")
    kilpailu.tulosta_tilanne()


if __name__ == "__main__":
    main()
