stations = [
    "Apeldoorn",
    "Assen",
    "Amsterdam",
    "Boxtel",
    "Breda",
    "Dordrecht",
    "Delft",
    "Deventer",
    "Enschede",
    "Gouda",
    "Groningen",
    "Den Haag",
    "Hengelo",
    "Haarlem",
    "Helmond",
    "Hoorn",
    "Heerlen",
    "Den Bosch",
    "Hilversum",
    "Leiden",
    "Lelystad",
    "Leeuwarden",
    "Maastricht",
    "Nijmegen",
    "Oss",
    "Roermond",
    "Roosendaal",
    "Sittard",
    "Tilburg",
    "Utrecht",
    "Venlo",
    "Vlissingen",
    "Zaandam",
    "Zwolle",
    "Zutphen"]

"""
vraagt de gebruiker om naam leftijd en een bericht en slaat deze gegevens op in een .CSV bestand
"""
def GebruikerInput():
    naam = input('voer je naam in: ')
    if len(naam) == 0:
        naam = 'anoniem'

    # vraag vervolgens om een leeftijd
    while True:
        try:
            leeftijd = input("voer een leeftijd in: ")
            leeftijd_input = int(leeftijd)
            if leeftijd_input < 0:
                print("onbevoegde waarde, voer alsjebleft een leeftijd in")
            else:
                break
        except ValueError:
            print("onbevoegde waarde, voer alsjebleft een leeftijd in")
    while True:
        bericht = input('voer hier je bericht in(maximaal 140 tekens): ')
        if len(bericht) <= 10:
            break
        else:
            print('het bericht is te lang')

GebruikerInput()