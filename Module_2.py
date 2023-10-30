import csv
from getpass import getpass
from datetime import datetime


def moderatorAunthentificeren():
    email = input('voer je moderator email in: ')
    wachtwoord = getpass('voer je wachtwoord in: ')

    # check of de moderator de juiste gegevens invoerd
    if email == 'moderator@mail.com' and wachtwoord == '12345678':
        return True
    else:
        return False


# moderatie van de berichten
def moderatie():
    # als de moderator is ingelogd
    if moderatorAunthentificeren():
        csv_file = 'gebruiker_info.csv'

        # lees het csv bestand in en ga de berichten na
        berichtLijst = []
        with open(csv_file, mode='r', newline='') as file:
            # maak van elke regel in het csv bestand een dictionary
            reader = csv.DictReader()
            # itereer door de dictionary van berichten en voeg deze toe aan een niewue lijst
            for rij in csv.DictReader():
                berichtLijst.append(rij)

        moderatorNaam = input('moderator naam: ')
        moderatorEmail = input('moderator email: ')

        # maak de goedkeuringstabel(dit gebeurt maar een keer)

        # laat het bericht zien voor goedkeuring
