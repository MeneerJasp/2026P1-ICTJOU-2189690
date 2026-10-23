# ==== Use Case functies ====


def pas_scenariobudget_aan(verbinding):
    """UC3: Past het budgetlimiet van een scenario aan op basis van de gebruikersinvoer."""
    scenarios = haal_scenarios_op(verbinding)
    if not scenarios:
        print("Er zijn geen scenario's beschikbaar.")
        return

    print("Beschikbare scenario's:")
    for volgnummer, scenario in enumerate(scenarios, start=1):
        print(f"{volgnummer}. {scenario['naam']} - Budget: EUR {scenario['budget_limiet']}")

    keuze = int(input("Kies een scenario (nummer): "))
    if keuze < 1 or keuze > len(scenarios):
        print("Ongeldige keuze.")
        return

    scenarionaam = scenarios[keuze - 1]['naam']
    nieuw_budget = float(input("Voer het nieuwe budget in: ").replace(",", "."))

    update_scenariobudget(verbinding, scenarionaam, nieuw_budget)
    print("Scenariobudget succesvol bijgewerkt!")


def bereken_spaarplan(verbinding):
    """UC6: Bereken een inkoopritme voor een gekozen sleutelonderdeel op basis van de prijs en het aantal maanden."""
    onderdelen = haal_alle_onderdelen_op(verbinding)
    if not onderdelen:
        print("Er zijn geen onderdelen beschikbaar voor een inkoopritme.")
        return

    for volgnummer, onderdeel in enumerate(onderdelen, start=1):
        print(f"{volgnummer}. [{onderdeel['scenarionaam']}] {onderdeel['titel']} - EUR {onderdeel['prijs']:.2f}")

    keuze = int(input("Voor welk sleutelonderdeel wil je een inkoopritme? (nummer): "))
    if keuze < 1 or keuze > len(onderdelen):
        print("Ongeldige keuze.")
        return

    gekozen_onderdeel = onderdelen[keuze - 1]
    prijs = float(gekozen_onderdeel['prijs'])

    maanden = int(input("Over hoeveel maanden wil je dit onderdeel operationeel hebben? "))

    print(f"Inkoopritme voor {gekozen_onderdeel['titel']} ({gekozen_onderdeel['scenarionaam']}):")
    for maand in range(1, maanden + 1):
        gespaard = (prijs / maanden) * maand
        print(f"Maand {maand}: Opgebouwd budget: EUR {gespaard:.2f}")


def toon_overzicht_per_scenario(verbinding):
    """UC7: Toont een overzicht van onderdelen per scenario inclusief statistieken, totaalbedrag, transportkosten en budgetcontrole."""
    scenariostatistieken = haal_scenariostatistieken_op(verbinding)
    pass


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


def haal_scenarios_op(verbinding):
    """Haalt alle scenario's op inclusief hun budgetlimiet."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam, budget_limiet FROM Scenario")
    return cursor.fetchall()


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