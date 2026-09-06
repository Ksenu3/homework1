lentoasemat = {}

while True:
    toiminto = input("Haluatko syöttää uuden lentoaseman, hakea lentoaseman vai lopettaa?")

    if toiminto == "syöttää":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi:")
        lentoasemat[icao] = nimi

    elif toiminto == "hakea":
        icao = input("Anna ICAO-koodi: ")
        print(lentoasemat[icao])

    elif toiminto == "lopettaa":
        break
