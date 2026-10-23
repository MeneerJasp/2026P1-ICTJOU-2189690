import sqlite3
import hashlib
import os
import csv

DATABASE = "niveau3/oefen-questcomposer/db/questcomposer.db"

# Configuratievariabelen (constanten)
STANDAARD_TRANSPORTKOSTEN = 0.00
STANDAARD_SCENARIOBUDGET = 100.00

# Globale variabelen om statistieken bij te houden
sessiestatistieken = {
    'toegevoegd': 0,
    'verwijderd': 0,
}


# ==== Functies voor het hoofdmenu en de hoofdfunctie ====


def main():
    """Hoofdfunctie die toegang controleert, de database verbindt en het hoofdmenu afhandelt. UC8 wordt uitgevoerd wanneer optie 8 gekozen wordt."""
    if not controleer_toegangscode():
        return

    verbinding = maak_verbinding()
    if not verbinding:
        return

    while True:
        keuze = toon_menu()
        if keuze == '1':
            voeg_onderdeel_toe(verbinding)
        elif keuze == '2':
            pas_onderdeelprijs_aan(verbinding)
        elif keuze == '3':
            verwijder_onderdeel(verbinding)
        elif keuze == '4':
            pas_scenariobudget_aan(verbinding)
        elif keuze == '5':
            toon_onderdelen_binnen_budget(verbinding)
        elif keuze == '6':
            bereken_spaarplan(verbinding)
        elif keuze == '7':
            toon_overzicht_per_scenario(verbinding)
        elif keuze == '8':
            # Use Case 8: Afsluiten van de sessie
            print("Ontwerpsessie afgerond. Succes met prototyping!")
            print("Sessiestatistieken:")
            print("Onderdelen toegevoegd:", sessiestatistieken['toegevoegd'])
            print("Onderdelen verwijderd:", sessiestatistieken['verwijderd'])
            break
        elif keuze == '9':
            importeer_csv(verbinding)
        else:
            print("Ongeldige keuze.")


def toon_menu():
    """Toont het hoofdmenu en vraagt de gebruiker om een keuze te maken."""
    print('--- QuestComposer ---')
    print('1. Registreer nieuw puzzelonderdeel')
    print('2. Herbereken kostprijs van onderdeel')
    print('3. Schrap onderdeel uit build')
    print('4. Stel scenariobudget bij')
    print('5. Zoek alternatieven binnen restbudget')
    print('6. Maak inkoopritme voor sleutelonderdeel')
    print('7. Toon haalbaarheidsoverzicht per scenario')
    print('8. Sluit ontwerpsessie af')
    print('9. Importeer intakebestand uit CSV')
    return input('Maak een keuze: ')


# ==== Use Case functies ====


def voeg_onderdeel_toe(verbinding):
    """UC1: Voegt een nieuw onderdeel toe aan een scenario. Controleert of de opgegeven leverancier en het scenario bestaan voordat het onderdeel wordt toegevoegd."""
    scenarionaam = kies_scenario(verbinding)
    if scenarionaam is None:
        return

    titel = input("Naam van het onderdeel: ")
    prijs = float(input("Prijs van het onderdeel: ").replace(",", "."))
    leveranciernaam = input("Leverancier: ")
    if not check_leverancier_bestaat(verbinding, leveranciernaam):
        print("FOUT: Leverancier bestaat niet.")
        return
    prio = int(input("Prioriteit (1-3): "))
    prio = max(1, min(prio, 3))
    voeg_onderdeel_toe_aan_db(verbinding, titel, prijs, leveranciernaam, scenarionaam, prio)
    sessiestatistieken['toegevoegd'] += 1
    print(f"Puzzelonderdeel succesvol geregistreerd! (totaal deze sessie: {sessiestatistieken['toegevoegd']})")


def pas_onderdeelprijs_aan(verbinding):
    """UC2: Past de prijs van een bestaand onderdeel aan op basis van een gekozen scenario en titel."""
    scenarionaam = kies_scenario(verbinding)
    if scenarionaam is None:
        return

    onderdelen = haal_onderdelen_van_scenario_op(verbinding, scenarionaam)
    if not onderdelen:
        print("Er zijn geen onderdelen in dit scenario om aan te passen.")
        return

    print("Kies een puzzelonderdeel:")
    for volgnummer, onderdeel in enumerate(onderdelen, start=1):
        print(f"{volgnummer}. [{onderdeel['scenarionaam']}] {onderdeel['titel']} - EUR {onderdeel['prijs']:.2f}")

    keuze = int(input("Voer het nummer van het onderdeel in: "))
    if keuze < 1 or keuze > len(onderdelen):
        print("Ongeldige keuze.")
        return

    gekozen_onderdeel = onderdelen[keuze - 1]
    nieuwe_prijs = float(input("Voer de nieuwe prijs in: ").replace(",", "."))
    update_prijs(verbinding, gekozen_onderdeel['scenarionaam'], gekozen_onderdeel['titel'], nieuwe_prijs)
    print("Kostprijs succesvol bijgewerkt!")


def pas_scenariobudget_aan(verbinding):
    """UC3: Past het budgetlimiet van een scenario aan op basis van de gebruikersinvoer."""
    scenarios = toon_beschikbare_scenarios(verbinding)
    if not scenarios:
        return

    keuze = int(input("Kies een scenario (nummer): "))
    if keuze < 1 or keuze > len(scenarios):
        print("Ongeldige keuze.")
        return

    scenarionaam = scenarios[keuze - 1]['naam']
    nieuw_budget = float(input("Voer het nieuwe budget in: ").replace(",", "."))

    update_scenariobudget(verbinding, scenarionaam, nieuw_budget)
    print("Scenariobudget succesvol bijgewerkt!")


def verwijder_onderdeel(verbinding):
    """UC4: Verwijdert een onderdeel uit de build op basis van een gekozen scenario en titel."""
    scenarionaam = kies_scenario(verbinding)
    if scenarionaam is None:
        return

    onderdelen = haal_onderdelen_van_scenario_op(verbinding, scenarionaam)
    if not onderdelen:
        print("Er zijn geen onderdelen in dit scenario om te verwijderen.")
        return

    print("Kies een puzzelonderdeel:")
    for volgnummer, onderdeel in enumerate(onderdelen, start=1):
        print(f"{volgnummer}. [{onderdeel['scenarionaam']}] {onderdeel['titel']} - EUR {onderdeel['prijs']:.2f}")

    keuze = int(input("Voer het nummer van het onderdeel in: "))
    if keuze < 1 or keuze > len(onderdelen):
        print("Ongeldige keuze.")
        return

    gekozen_onderdeel = onderdelen[keuze - 1]
    verwijder_onderdeel_uit_db(verbinding, gekozen_onderdeel['scenarionaam'], gekozen_onderdeel['titel'])

    sessiestatistieken['verwijderd'] += 1
    print(f"Puzzelonderdeel succesvol verwijderd! (totaal deze sessie: {sessiestatistieken['verwijderd']})")


def toon_onderdelen_binnen_budget(verbinding):
    """UC5: Toont onderdelen waarvan de prijs tussen twee opgegeven budgetgrenzen ligt."""
    pass


def bereken_spaarplan(verbinding):
    """UC6: Bereken een inkoopritme voor een gekozen sleutelonderdeel op basis van de prijs en het aantal maanden."""
    pass


def toon_overzicht_per_scenario(verbinding):
    """UC7: Toont een overzicht van onderdelen per scenario inclusief statistieken, totaalbedrag, transportkosten en budgetcontrole."""
    scenariostatistieken = haal_scenariostatistieken_op(verbinding)
    pass


def importeer_csv(verbinding):
    """UC9: Importeert onderdelen vanuit een CSV-bestand en voegt deze toe aan de database. Voegt benodigde leveranciers en scenario's toe indien deze nog niet bestaan."""
    bestandsnaam = input("Voer de naam van het CSV-bestand in: ")
    pass


def controleer_toegangscode():
    """UC10: Controleert of de ingevoerde toegangscode klopt."""
    # Wordt in increment 3 geprogrammeerd.
    return True


# === Helper functies ===


def toon_beschikbare_scenarios(verbinding):
    """Toont alle beschikbare scenario's en geeft ze terug."""
    scenarios = haal_scenarios_op(verbinding)
    if not scenarios:
        print("Er zijn geen scenario's beschikbaar.")
        return []

    print("Beschikbare scenario's:")
    for volgnummer, scenario in enumerate(scenarios, start=1):
        print(f"{volgnummer}. {scenario['naam']} - Budget: EUR {scenario['budget_limiet']}")
    return scenarios


def kies_scenario(verbinding):
    """Vraagt de gebruiker om eerst een scenario te kiezen."""
    scenarios = toon_beschikbare_scenarios(verbinding)
    if not scenarios:
        return None

    keuze = int(input("Kies een scenario (nummer): "))
    if keuze < 1 or keuze > len(scenarios):
        print("Ongeldige keuze.")
        return None

    return scenarios[keuze - 1]['naam']


def toon_onderdelenlijst(verbinding):
    """Toont de volledige onderdelenlijst inclusief de totaalkosten (prijs + transportkosten) voor elk onderdeel."""
    onderdelen = haal_alle_onderdelen_op(verbinding)
    print(f"{'Scenario':<15} | {'Puzzelonderdeel':<20} | {'Leverancier':<15} | {'Totale kost':<12} | {'Urgentie'}")
    print("-----------------------------------------------------------------------------------")
    for row in onderdelen:
        totaal = float(row['prijs']) + float(row['transportkosten'])
        print(f"{row['scenarionaam']:<15} | {row['titel']:<20} | {row['leveranciernaam']:<15} | EUR {totaal:<8} | {row['prioriteit']}")


def lees_toegangscode_hash():
    """Leest de hash van de toegangscode uit het .env-bestand."""
    bestand = open('.env', mode='r', encoding='utf-8-sig')

    for regel in bestand:
        regel = regel.strip()
        if regel.startswith('TOEGANGSCODE_HASH='):
            bestand.close()
            return regel.replace('TOEGANGSCODE_HASH=', '')

    bestand.close()

    return None


# ==== Databasefuncties ====


def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect(DATABASE)
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding


def haal_alle_onderdelen_op(verbinding):
    """Haalt onderdelen op inclusief leverancier- en scenarionaam."""
    cursor = verbinding.cursor()
    query = """
        SELECT Onderdeel.scenario as scenarionaam, Onderdeel.titel, Onderdeel.prijs, Leverancier.naam as leveranciernaam, Leverancier.transportkosten, Onderdeel.prioriteit
        FROM Onderdeel
        JOIN Leverancier ON Onderdeel.leverancier = Leverancier.naam
    """
    cursor.execute(query)
    return cursor.fetchall()


def haal_onderdelen_van_scenario_op(verbinding, scenarionaam):
    """Haalt alleen de onderdelen op die bij een gekozen scenario horen."""
    cursor = verbinding.cursor()
    query = """
        SELECT Onderdeel.scenario as scenarionaam, Onderdeel.titel, Onderdeel.prijs, Leverancier.naam as leveranciernaam, Leverancier.transportkosten, Onderdeel.prioriteit
        FROM Onderdeel
        JOIN Leverancier ON Onderdeel.leverancier = Leverancier.naam
        WHERE Onderdeel.scenario = ?
    """
    cursor.execute(query, (scenarionaam,))
    return cursor.fetchall()


def haal_scenarios_op(verbinding):
    """Haalt alle scenario's op inclusief hun budgetlimiet."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam, budget_limiet FROM Scenario")
    return cursor.fetchall()


def update_prijs(verbinding, scenarionaam, titel, nieuwe_prijs):
    """Update de prijs van een onderdeel op basis van scenarionaam en titel."""
    cursor = verbinding.cursor()
    cursor.execute(
        "UPDATE Onderdeel SET prijs = ? WHERE scenario = ? AND titel = ?",
        (nieuwe_prijs, scenarionaam, titel)
    )
    return cursor.rowcount


def verwijder_onderdeel_uit_db(verbinding, scenarionaam, titel):
    """Verwijdert een onderdeel op basis van scenarionaam en titel."""
    cursor = verbinding.cursor()
    cursor.execute("DELETE FROM Onderdeel WHERE scenario = ? AND titel = ?", (scenarionaam, titel))
    return cursor.rowcount


def voeg_onderdeel_toe_aan_db(verbinding, titel, prijs, leverancier_naam, scenario_naam, prio):
    """Voegt een nieuw onderdeel toe aan de database."""
    cursor = verbinding.cursor()
    query = """
        INSERT INTO Onderdeel (scenario, titel, prijs, leverancier, prioriteit)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (scenario_naam, titel, prijs, leverancier_naam, prio))


def haal_onderdelen_binnen_budget(verbinding, min_budget, max_budget):
    """Haal onderdelen op waarvan de prijs tussen min_budget en max_budget ligt."""
    cursor = verbinding.cursor()
    query = "SELECT titel, prijs FROM Onderdeel WHERE prijs BETWEEN ? AND ?"
    cursor.execute(query, (min_budget, max_budget))
    return cursor.fetchall()


def check_leverancier_bestaat(verbinding, leveranciernaam):
    """Controleert of een leverancier al bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam FROM Leverancier WHERE naam = ?", (leveranciernaam,))
    if cursor.fetchone() is not None:
        return True
    else:
        return False


def haal_scenariostatistieken_op(verbinding):
    """Haalt alle UC7-statistieken per scenario op via een geaggregeerde query over drie tabellen."""
    cursor = verbinding.cursor()
    query = """
        SELECT
            s.naam AS scenarionaam,
            s.budget_limiet,
            COUNT(o.titel) AS aantal_onderdelen,
            MIN(o.prijs) AS goedkoopste_onderdeel,
            MAX(o.prijs) AS duurste_onderdeel,
            AVG(o.prijs) AS gemiddelde_prijs,
            SUM(o.prijs) AS totaalbedrag_onderdelen,
            SUM(o.prijs + l.transportkosten) AS totaalbedrag_inclusief_transportkosten
        FROM Scenario s
        INNER JOIN Onderdeel o ON o.scenario = s.naam
        INNER JOIN Leverancier l ON l.naam = o.leverancier
        GROUP BY s.naam, s.budget_limiet
        ORDER BY s.naam
    """
    cursor.execute(query)
    return cursor.fetchall()


def scenario_bestaat(verbinding, scenarionaam):
    """Controleert of een scenario bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam FROM Scenario WHERE naam = ?", (scenarionaam,))
    return cursor.fetchone() is not None


def haal_kosten_op_van_scenario(verbinding, scenarionaam):
    """Haalt prijzen en transportkosten op van onderdelen binnen een specifiek scenario."""
    cursor = verbinding.cursor()
    query = """
        SELECT Onderdeel.prijs, Leverancier.transportkosten
        FROM Onderdeel
        JOIN Leverancier ON Onderdeel.leverancier = Leverancier.naam
        WHERE Onderdeel.scenario = ?
    """
    cursor.execute(query, (scenarionaam,))
    return cursor.fetchall()


def update_scenariobudget(verbinding, scenarionaam, nieuw_budget):
    """Update het budgetlimiet van een scenario."""
    cursor = verbinding.cursor()
    cursor.execute("UPDATE Scenario SET budget_limiet = ? WHERE naam = ?", (nieuw_budget, scenarionaam))


def voeg_leverancier_toe(verbinding, leveranciernaam, transportkosten):
    """Voegt een nieuwe leverancier toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute("INSERT INTO Leverancier (naam, transportkosten) VALUES (?, ?)", (leveranciernaam, transportkosten))


def voeg_scenario_toe(verbinding, scenarionaam, budget_limiet):
    """Voegt een nieuw scenario toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute("INSERT INTO Scenario (naam, budget_limiet) VALUES (?, ?)", (scenarionaam, budget_limiet))


# ==== Applicatie startpunt ====

if __name__ == "__main__":
    main()