from Korisnici.korisnikiIO import ucitaj_korisnike


def prijava()
    korisnici = ucitaj_korisnike()

    korisnicko_ime = input("Unesite korisničko ime:")
    lozinka = input ("Unesite lozinku:")

    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik ['lozinka'] == lozinka:
            return korisnik
    return None

