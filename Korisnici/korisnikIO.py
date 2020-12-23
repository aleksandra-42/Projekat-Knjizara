import json
datoteka ='./datoteka/korisnici.json'

def sacuvaj_korisnike(korisnici):
    with open(datoteka,"w") as f:
        json.dump(korisnici, f)

def ucitaj_korisnike(datoteka):
    with open(datoteka) as f:
        return json.load(f)
