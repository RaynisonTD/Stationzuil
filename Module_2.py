import csv
import os.path
import psycopg2
import tkinter as tk
from tkinter import messagebox

class AuthenticatieGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Moderator Authenticatie")

        self.moderator_email_label = tk.Label(root, text="Moderator Email:")
        self.moderator_email_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.moderator_email_entry = tk.Entry(root)
        self.moderator_email_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.moderator_naam_label = tk.Label(root, text="Moderator Naam:")
        self.moderator_naam_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.moderator_naam_entry = tk.Entry(root)
        self.moderator_naam_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.authenticatie_button = tk.Button(root, text="Authenticeer", command=self.authenticatie)
        self.authenticatie_button.grid(row=2, column=0, columnspan=2, pady=20)

    def authenticatie(self):
        email = self.moderator_email_entry.get()
        naam = self.moderator_naam_entry.get()

        if not email or not naam:
            messagebox.showerror("Ontbrekende gegevens", "Vul alstublieft zowel de moderator email als naam in.")
            return

        resultaat = self.moderator_authenticeren(email, naam)

        if resultaat is not None:
            self.root.destroy()
            self.open_moderatie_gui(resultaat)
        else:
            messagebox.showerror("Authenticatie Mislukt", "Authenticatie is mislukt. Probeer het opnieuw.")

    def moderator_authenticeren(self, email, naam):
        if email == "moderator@mail.nl" and naam != '':
            return naam, email
        else:
            return None

    def open_moderatie_gui(self, resultaat):
        moderatie_root = tk.Tk()
        moderatie_root.title("Moderatie Berichten")

        moderatie_gui = ModeratieGUI(moderatie_root, resultaat)
        moderatie_root.mainloop()


class ModeratieGUI:
    def __init__(self, root, authenticatie_resultaat):
        self.root = root
        self.resultaat = authenticatie_resultaat

        self.root.title("Moderatie Berichten")

        self.csv_file = 'berichten.csv'
        self.gekeurde_berichten = []

        with open(self.csv_file, "r") as file:
            header = next(file)
            is_leeg = not any(line.strip() for line in file)

        if is_leeg:
            messagebox.showinfo("Leeg CSV Bestand", f"Het CSV-bestand {self.csv_file} is leeg.")
            self.root.destroy()
        else:
            with open(self.csv_file, mode='r+', newline='') as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames

                for i, rij in enumerate(reader):
                    print(f"Bericht {i + 1}:")
                    print(f"Naam: {rij['naam']}")
                    print(f"Bericht: {rij['bericht']}")
                    print("Opties:")
                    print("2. Afkeuren")
                    print("1. Goedkeuren")

                    keuze = input('Wordt dit bericht goedgekeurd (j) of afgekeurd (n)? (j/n): ')
                    goedgekeurd = "Ja" if keuze == "j" else "Nee"

                    if goedgekeurd == 'Ja':
                        rij["goedgekeurd"] = goedgekeurd
                        rij['gekeurd_door'] = self.resultaat[0]
                        rij['moderator_email'] = self.resultaat[1]
                        self.gekeurde_berichten.append(rij)

                with open(self.csv_file, mode='w', newline='') as write_file:
                    writer = csv.DictWriter(write_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.gekeurde_berichten)

            if self.gekeurde_berichten:
                print('Bestanden zijn bijgewerkt in {csv_bestand}')

                try:
                    conn = psycopg2.connect(host="20.160.159.26", dbname="Station-Zuil", user="postgres",
                                            password="Obioma-Claudette1973", port=5432)
                    cur = conn.cursor()

                    project_directory = os.getcwd()
                    csv_file = os.path.join(project_directory, 'berichten.csv')
                    my_table = "berichten"

                    with open(csv_file, 'r') as f:
                        cur.copy_expert(sql=f"COPY {my_table} FROM STDIN WITH CSV HEADER DELIMITER ','", file=f)

                    conn.commit()

                except Exception as error:
                    messagebox.showerror("Database Fout", f"Fout bij het versturen van berichten naar de database:\n{error}")

                finally:
                    if cur is not None:
                        cur.close()

                        header = None
                        with open(csv_file, "r") as file:
                            header = next(file)

                        with open(csv_file, "w", newline='') as file:
                            file.write(header)

                    if conn is not None:
                        conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    authenticatie_gui = AuthenticatieGUI(root)
    root.mainloop()
