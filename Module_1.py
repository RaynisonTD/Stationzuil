import random
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

stations = ["Utrecht", "Den Haag", "Amsterdam"]

def gebruikerInput():
    naam = naam_entry.get()
    if len(naam) == 0:
        naam = 'anoniem'

    # vraag vervolgens om een leeftijd
    leeftijd = leeftijd_entry.get()
    while not leeftijd.isdigit() or int(leeftijd) < 0:
        messagebox.showerror("Ongeldige waarde", "Voer alsjeblieft een geldige leeftijd in.")
        return

    # vraag om het bericht
    bericht = bericht_entry.get()
    if len(bericht) > 140:
        messagebox.showerror("Te lang bericht", "Het bericht is te lang (maximaal 140 tekens).")
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

        # check of de headers al bestaan en maak ze aan als dat niet het geval is
        if file.tell() == 0:
            writer.writerow(fieldnames)

        # voer de gegevens in
        writer.writerow([naam, leeftijd, bericht, willekeurig_station, datum_tijd])

    messagebox.showinfo("Bericht verzonden", "Je bericht is succesvol verzonden!")

# GUI opzetten
root = tk.Tk()
root.title("Bericht versturen")

# Naam invoerveld
naam_label = tk.Label(root, text="Naam:")
naam_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
naam_entry = tk.Entry(root)
naam_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Leeftijd invoerveld
leeftijd_label = tk.Label(root, text="Leeftijd:")
leeftijd_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
leeftijd_entry = tk.Entry(root)
leeftijd_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Bericht invoerveld
bericht_label = tk.Label(root, text="Bericht:")
bericht_label.grid(row=2, column=0, padx=10, pady=10, sticky="ne")
bericht_entry = tk.Entry(root, width=50)
bericht_entry.grid(row=2, column=1, padx=10, pady=10, sticky="nw")

# Verzendknop
verzend_button = tk.Button(root, text="Verzend", command=gebruikerInput)
verzend_button.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
