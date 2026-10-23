import csv
import os

# Configuratievariabelen (constanten)
STANDAARD_TRANSPORTKOSTEN = 0.00
STANDAARD_SCENARIOBUDGET = 100.00


# ==== Use Case functies ====

def importeer_csv(verbinding):
    """UC9: Importeert onderdelen vanuit een CSV-bestand en voegt deze toe aan de database. Voegt benodigde leveranciers en scenario's toe indien deze nog niet bestaan."""
    bestandsnaam = input("Voer de naam van het CSV-bestand in: ")
    if len(bestandsnaam) < 4:
        print("Ongeldige bestandsnaam.")
        return

    # Controleer met os of het bestand bestaat (ook als je vanuit de hoofdmap van de repo werkt).
    if not os.path.exists(bestandsnaam):
        pad_in_project = "niveau3/oefen-questcomposer/" + bestandsnaam
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
            leveranciernaam = rij["leverancier"]
            scenarionaam = rij["scenario"]
            prioriteit = int(rij["prioriteit"])

            if not check_leverancier_bestaat(verbinding, leveranciernaam):
                voeg_leverancier_toe(verbinding, leveranciernaam, STANDAARD_TRANSPORTKOSTEN)

            if not scenario_bestaat(verbinding, scenarionaam):
                voeg_scenario_toe(verbinding, scenarionaam, STANDAARD_SCENARIOBUDGET)

            voeg_onderdeel_toe_aan_db(verbinding, titel, prijs, leveranciernaam, scenarionaam, prioriteit)

    print("Intakebestand succesvol geimporteerd!")


# ==== Databasefuncties ====

def check_leverancier_bestaat(verbinding, leveranciernaam):
    """Controleert of een leverancier al bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam FROM Leverancier WHERE naam = ?", (leveranciernaam,))
    return cursor.fetchone() is not None


def scenario_bestaat(verbinding, scenarionaam):
    """Controleert of een scenario al bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam FROM Scenario WHERE naam = ?", (scenarionaam,))
    return cursor.fetchone() is not None


def voeg_leverancier_toe(verbinding, leveranciernaam, transportkosten):
    """Voegt een nieuwe leverancier toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute(
        "INSERT INTO Leverancier (naam, transportkosten) VALUES (?, ?)",
        (leveranciernaam, transportkosten)
    )


def voeg_scenario_toe(verbinding, scenarionaam, budget_limiet):
    """Voegt een nieuw scenario toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute(
        "INSERT INTO Scenario (naam, budget_limiet) VALUES (?, ?)",
        (scenarionaam, budget_limiet)
    )


def voeg_onderdeel_toe_aan_db(verbinding, titel, prijs, leverancier_naam, scenario_naam, prio):
    """Voegt een nieuw onderdeel toe aan de database."""
    cursor = verbinding.cursor()
    query = """
        INSERT INTO Onderdeel (scenario, titel, prijs, leverancier, prioriteit)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (scenario_naam, titel, prijs, leverancier_naam, prio))