import random
import csv
from datetime import datetime

stations = ["Utrecht", "Den Haag", "Amsterdam"]




def gebruikerInput():
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
        if len(bericht) <= 140:
            break
        else:
            print('het bericht is te lang')

    # selecteer willekeurig een station
    willekeurig_station = random.choice(stations)

    # pak de datum en tijd van schrijven
    datum_tijd = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # maak het CSV bestand aan
    csv_file = 'gebruiker_info.csv'

    # maak het bestand klaar voor bewerking
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # creer een header
        writer.writerow(['naam', 'leeftijd', 'bericht', 'station', 'tijd van publicatie'])

        # voer de gegevens in
        writer.writerow([naam, leeftijd, bericht, willekeurig_station, datum_tijd])


gebruikerInput()