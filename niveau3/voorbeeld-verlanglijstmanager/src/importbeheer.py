import csv
import os

# Configuratievariabelen (constanten)
STANDAARD_VERZENDKOSTEN = 0.00
STANDAARD_LIJSTBUDGET = 100.00


# ==== Use Case functies ====

def importeer_csv(verbinding):
    """UC9: Importeert items vanuit een CSV-bestand en voegt deze toe aan de database. Voegt benodigde winkels en lijsten toe indien deze nog niet bestaan."""
    bestandsnaam = input("Voer de naam van het CSV-bestand in: ")
    if len(bestandsnaam) < 4:
        print("Ongeldige bestandsnaam.")
        return

    # Controleer met os of het bestand bestaat (ook als je vanuit de hoofdmap van de repo werkt).
    if not os.path.exists(bestandsnaam):
        pad_in_project = "niveau3/voorbeeld-verlanglijstmanager/" + bestandsnaam
        if os.path.exists(pad_in_project):
            bestandsnaam = pad_in_project
        else:
            print("Bestand niet gevonden.")
            return

    with open(bestandsnaam, mode="r", encoding="utf-8") as bestand:
        lezer = csv.DictReader(bestand)
        for rij in lezer:
            titel = rij["titel"]
            prijs = float(rij["prijs"])
            winkelnaam = rij["winkel"]
            lijstnaam = rij["lijst"]
            prioriteit = int(rij["prioriteit"])

            if not check_winkel_bestaat(verbinding, winkelnaam):
                voeg_winkel_toe(verbinding, winkelnaam, STANDAARD_VERZENDKOSTEN)

            if not lijst_bestaat(verbinding, lijstnaam):
                voeg_lijst_toe(verbinding, lijstnaam, STANDAARD_LIJSTBUDGET)

            voeg_item_toe_aan_db(verbinding, titel, prijs, winkelnaam, lijstnaam, prioriteit)

    print("CSV succesvol geimporteerd!")


# ==== Databasefuncties ====

def check_winkel_bestaat(verbinding, winkelnaam):
    """Controleert of een winkel al bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam FROM Winkel WHERE naam = ?", (winkelnaam,))
    return cursor.fetchone() is not None


def lijst_bestaat(verbinding, lijstnaam):
    """Controleert of een lijst al bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam FROM Lijst WHERE naam = ?", (lijstnaam,))
    return cursor.fetchone() is not None


def voeg_winkel_toe(verbinding, winkelnaam, verzendkosten):
    """Voegt een nieuwe winkel toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute(
        "INSERT INTO Winkel (naam, verzendkosten) VALUES (?, ?)",
        (winkelnaam, verzendkosten)
    )


def voeg_lijst_toe(verbinding, lijstnaam, budget_limiet):
    """Voegt een nieuwe lijst toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute(
        "INSERT INTO Lijst (naam, budget_limiet) VALUES (?, ?)",
        (lijstnaam, budget_limiet)
    )


def voeg_item_toe_aan_db(verbinding, titel, prijs, winkel_naam, lijst_naam, prio):
    """Voegt een nieuw item toe aan de database."""
    cursor = verbinding.cursor()
    query = """
        INSERT INTO Item (lijst, titel, prijs, winkel, prioriteit)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (lijst_naam, titel, prijs, winkel_naam, prio))