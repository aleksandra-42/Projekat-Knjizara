import json
datoteka ='./datoteka/knjige.json'

def sacuvaj_knjige(knjige):
    with open(datoteka,"w") as f:
        json.dump(knjige, f)

def ucitaj_knjige(datoteka):
    with open(datoteka) as f:
        return json.load(f)