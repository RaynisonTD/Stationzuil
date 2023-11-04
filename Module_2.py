import csv
import os.path

import psycopg2


def moderatorAunthentificeren():
    while True:
        email = input('voer je moderator email in: ')

        naam = input('voer je naam in : ')

        # check of de moderator de juiste gegevens invoerd
        if email == "moderator@mail.nl" and naam != '':
            return naam, email

        else:
            print("authentificatie mislukt, probeer het nog eens")


# moderatie van de berichten
def moderatie():
    # als de moderator is ingelogd
    # connectie variabelen
    cur = None
    conn = None

    resultaat = moderatorAunthentificeren()

    if resultaat is not None:
        naam, email = resultaat
        csv_file = 'berichten.csv'

        # creer een tijdelijk lijst met alle berichten
        gekeurde_berichten = []

        #geef aan dat het bestand leeg is als de moderator het opent zonder dat er berichten inzitten
        with open(csv_file, "r") as file:
            # lees de eerste regel
            header = next(file)

            # check of er geen berichten zin
            is_leeg = not any(line.strip() for line in file)

        if is_leeg:
            print(f"The CSV bestand {csv_file} is leeg.")
        else:

            with open(csv_file, mode='r+', newline='') as file:
                # maak van elke regel in het csv bestand een dictionary
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames

                # laat het bericht zien voor goedkeuring
                for i, rij in enumerate(reader):

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
                        rij["goedgekeurd"] = goedgekeurd
                        rij['gekeurd_door'] = naam
                        rij['moderator_email'] = email

                    gekeurde_berichten.append(rij)

                # heropen het bestand en vul de 2 moderator kolommen
                with open(csv_file, mode='w', newline='') as write_file:
                    writer = csv.DictWriter(write_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(gekeurde_berichten)

            # nadat de berichten gekeurd zijn, stuur ze dan naar de gewenste database
            print('bestanden zijn bijgewerkt in {csv_bestand}')


            try:
                conn = psycopg2.connect(host="localhost", dbname="Stationzuil", user="postgres",
                                        password="Obioma-Claudette1973", port=5432)

                cur = conn.cursor()

                # defineer het csv bestand en de datababase tabel waar de gegevens naartoe moeten
                project_directory = os.getcwd()
                csv_file = os.path.join(project_directory, 'berichten.csv')
                my_table = "berichten"

                # gebruik de copy command om alle berichten over te kopieren naar de database
                copy_table = f"COPY {my_table} FROM '{csv_file}' DELIMITER ',' CSV HEADER;"
                cur.execute(copy_table)
                conn.commit()







            except Exception as error:
                print(error)

            finally:
                # sluit de connectie en maak het csv bestand leeg
                if cur is not None:
                    cur.close()

                    header = None
                    with open(csv_file, "r") as file:
                        header = next(file)

                    # Reopen the file in write mode and write back the header
                    with open(csv_file, "w", newline='') as file:
                        file.write(header)

                if conn is not None:
                    conn.close()










if __name__ == "__main__":
    moderatie()

    # laat het bericht zien voor goedkeuring
