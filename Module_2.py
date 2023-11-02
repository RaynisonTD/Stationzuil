import csv


def moderatorAunthentificeren():
    email = input('voer je moderator email in: ')
    naam = input('voer je naam in : ')
    while True:
    # check of de moderator de juiste gegevens invoerd
        if '@' in email and naam != '':
            return naam, email

        else:
            print("authentificatie mislukt, probeer het nog eens")
            return None



# moderatie van de berichten
def moderatie():
    # als de moderator is ingelogd
    moderator_naam = moderatorAunthentificeren()
    moderator_email = moderatorAunthentificeren()

    if moderator_naam and moderator_email:
        csv_file = 'berichten.csv'

        # creer een tijdelijk lijst met alle berichten
        gekeurde_berichten = []

        with open(csv_file, mode='r+', newline='') as file:
            # maak van elke regel in het csv bestand een dictionary
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames

            # laat het bericht zien voor goedkeuring
            for i, rij in enumerate(reader):

                if rij.get('goedgekeurd?') and rij.get("gekeurd door:") and rij.get('moderator e-mail'):

                    gekeurde_berichten.append(rij)
                    continue

                else:

                    print(f"bericht {i + 1}:")
                    print(f"naam: {rij['naam']}")
                    print(f"bericht: {rij['bericht']}")
                    print("opties:")
                    print("2. afkeuren")
                    print("1. goedkeuren")

                keuze = input('word dit berichten goedgekeurd (j) of afgekeurd (n)? (j/n): ')
                goedgekeurd = "Ja" if keuze == "j" else "Nee"

                # voeg de goedkeuring en de moderator naam toe aan de tabel
                if goedgekeurd == 'Ja' or goedgekeurd == 'Nee':
                    rij["goedgekeurd?"] = goedgekeurd
                    rij['gekeurd door:'] = moderator_naam
                    rij['moderator e-mail'] = moderator_email

                gekeurde_berichten.append(rij)

            # heropen het bestand en vul de 2 moderator kolommen
            with open(csv_file, mode='w', newline='') as write_file:
                writer = csv.DictWriter(write_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(gekeurde_berichten)

        print('bestanden zijn bijgewerkt in {csv_bestand}')




moderatie()
