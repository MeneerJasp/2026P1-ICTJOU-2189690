# Globale variabelen om statistieken bij te houden
sessiestatistieken = {
    "toegevoegd": 0,
    "verwijderd": 0,
}


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
    sessiestatistieken["toegevoegd"] += 1
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
    if nieuwe_prijs < 0:
        print("Ongeldige prijs.")
        return

    update_prijs(verbinding, gekozen_onderdeel["scenarionaam"], gekozen_onderdeel["titel"], nieuwe_prijs)
    print("Kostprijs succesvol bijgewerkt!")


def verwijder_onderdeel(verbinding):
    """UC4: Verwijdert een onderdeel uit de build op basis van een gekozen scenario en titel."""
    scenarionaam = kies_scenario(verbinding)
    if scenarionaam is None:
        return

    onderdelen = haal_onderdelen_van_scenario_op(verbinding, scenarionaam)
    if not onderdelen:
        print("Er zijn geen onderdelen in dit scenario.")
        return

    for volgnummer, onderdeel in enumerate(onderdelen, start=1):
        print(f"{volgnummer}. {onderdeel['titel']} - EUR {onderdeel['prijs']:.2f}")

    keuze = int(input("Welk onderdeel wil je verwijderen? (nummer): "))
    if keuze < 1 or keuze > len(onderdelen):
        print("Ongeldige keuze.")
        return

    titel = onderdelen[keuze - 1]["titel"]
    verwijder_onderdeel_uit_db(verbinding, scenarionaam, titel)
    sessiestatistieken["verwijderd"] += 1
    print("Onderdeel succesvol verwijderd!")


def toon_onderdelen_binnen_budget(verbinding):
    """UC5: Toont onderdelen waarvan de prijs tussen twee opgegeven budgetgrenzen ligt."""
    grens1 = float(input("Voer de eerste budgetgrens in: ").replace(",", "."))
    grens2 = float(input("Voer de tweede budgetgrens in: ").replace(",", "."))

    min_budget = min(grens1, grens2)
    max_budget = max(grens1, grens2)

    onderdelen = haal_onderdelen_binnen_budget(verbinding, min_budget, max_budget)
    if not onderdelen:
        print("Er zijn geen onderdelen binnen het opgegeven budgetbereik.")
        return

    print(f"Onderdelen tussen EUR {min_budget} en EUR {max_budget}:")
    for onderdeel in onderdelen:
        print(f"{onderdeel['titel']} - EUR {onderdeel['prijs']}")


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

    return scenarios[keuze - 1]["naam"]


def toon_onderdelenlijst(verbinding):
    """Toont de volledige onderdelenlijst inclusief de totaalkosten (prijs + transportkosten) voor elk onderdeel."""
    onderdelen = haal_alle_onderdelen_op(verbinding)
    print(f"{'Scenario':<15} | {'Puzzelonderdeel':<20} | {'Leverancier':<15} | {'Totale kost':<12} | {'Urgentie'}")
    print("-----------------------------------------------------------------------------------")
    for row in onderdelen:
        totaal = float(row["prijs"]) + float(row["transportkosten"])
        print(f"{row['scenarionaam']:<15} | {row['titel']:<20} | {row['leveranciernaam']:<15} | EUR {totaal:<8} | {row['prioriteit']}")


# ==== Databasefuncties ====

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