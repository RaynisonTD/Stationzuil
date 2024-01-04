import random
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

stations = ["Utrecht", "Den Haag", "Amsterdam"]

def gebruikerInput():
    # haal de waarden uit de entry widgets
    naam = naam_entry.get() or 'anoniem'
    leeftijd = leeftijd_entry.get()
    bericht = bericht_entry.get()

    # valideer de waarden
    try:
        leeftijd = int(leeftijd)
        assert leeftijd >= 0, "onbevoegde waarde, voer alsjeblieft een leeftijd in"
        assert len(bericht) <= 140, 'het bericht is te lang'
    except (ValueError, AssertionError) as e:
        # toon een foutmelding als de waarden ongeldig zijn
        messagebox.showerror("Fout", str(e))
        return

    # selecteer willekeurig een station
    willekeurig_station = random.choice(stations)

    # pak de datum en tijd van schrijven
    datum_tijd = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # maak het CSV bestand aan
    csv_file = 'berichten.csv'

    # maak het bestand klaar voor bewerking
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        fieldnames = ['naam', 'leeftijd', 'bericht', 'station', 'tijd van publicatie', "goedgekeurd", "gekeurd_door","moderator_email"]

        # check of de headers al bestaan en maak ze aan als dat niet het geval is. Dit is om ter voorkomen dat oudere data overschreden wordt door nieuwe data
        if file.tell() == 0:
            writer.writerow(fieldnames)

        # voer de gegevens in
        writer.writerow([naam, leeftijd, bericht, willekeurig_station, datum_tijd])

    # toon een succesmelding als de gegevens zijn opgeslagen
    messagebox.showinfo("Succes", "Je bericht is opgeslagen in het CSV bestand")

# maak een tkinter window
window = tk.Tk()
window.title("Module 1")
window.geometry("400x300")

# maak een label voor de naam
naam_label = tk.Label(window, text="Voer je naam in:")
naam_label.grid(row=0, column=0, padx=10, pady=10)

# maak een entry voor de naam
naam_entry = tk.Entry(window)
naam_entry.grid(row=0, column=1, padx=10, pady=10)

# maak een label voor de leeftijd
leeftijd_label = tk.Label(window, text="Voer een leeftijd in:")
leeftijd_label.grid(row=1, column=0, padx=10, pady=10)

# maak een entry voor de leeftijd
leeftijd_entry = tk.Entry(window)
leeftijd_entry.grid(row=1, column=1, padx=10, pady=10)

# maak een label voor het bericht
bericht_label = tk.Label(window, text="Voer hier je bericht in (maximaal 140 tekens):")
bericht_label.grid(row=2, column=0, padx=10, pady=10)

# maak een entry voor het bericht
bericht_entry = tk.Entry(window)
bericht_entry.grid(row=2, column=1, padx=10, pady=10)

# maak een button om de gegevens op te slaan
opslaan_button = tk.Button(window, text="Opslaan", command=gebruikerInput)
opslaan_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# start de mainloop
window.mainloop()