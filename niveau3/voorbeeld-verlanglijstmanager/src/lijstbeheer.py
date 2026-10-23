# ==== Use Case functies ====


def pas_lijstbudget_aan(verbinding):
    """UC3: Past het budgetlimiet van een lijst aan op basis van de gebruikersinvoer."""
    lijsten = haal_lijsten_op(verbinding)
    if not lijsten:
        print("Er zijn geen verlanglijsten.")
        return

    for volgnummer, lijst in enumerate(lijsten, start=1):
        print(f"{volgnummer}. {lijst['naam']} - Budget: €{lijst['budget_limiet']:.2f}")

    keuze = int(input("Welke verlanglijst kies je? (nummer): "))
    if keuze < 1 or keuze > len(lijsten):
        print("Ongeldige keuze.")
        return

    lijstnaam = lijsten[keuze - 1]['naam']
    nieuw_budget = float(input("Nieuw budget: ").replace(",", "."))

    update_lijstbudget(verbinding, lijstnaam, nieuw_budget)
    print("Lijstbudget succesvol bijgewerkt!")


def bereken_spaarplan(verbinding):
    """UC6: Bereken een persoonlijk spaarplan voor een gekozen item op basis van de prijs en het aantal maanden dat de gebruiker wil sparen."""

    # 2. Het systeem toont een genummerde lijst van alle items met hun huidige prijs:
    items = haal_verlanglijst_op(verbinding)
    if not items:
        print("Er zijn geen items beschikbaar voor een spaarplan.")
        return

    for volgnummer, item in enumerate(items, start=1):
        print(f"{volgnummer}. [{item['lijstnaam']}] {item['titel']} - €{item['prijs']:.2f}")

    # 3. De student voert het nummer (index) van het gewenste item in.
    keuze = int(input("Voor welk item wil je een spaarplan? (nummer): "))
    if not 1 <= keuze <= len(items):
        print("Ongeldige keuze.")
        return

    gekozen_item = items[keuze - 1]
    prijs = float(gekozen_item['prijs'])

    # 4. Het systeem vraagt over hoeveel maanden het item gekocht moet worden.
    maanden = int(input("Over hoeveel maanden wil je dit kopen? "))

    # 6. Het systeem toont voor elke maand het totale bedrag dat tot dan toe gespaard moet zijn.
    print(f"Spaarplan voor {gekozen_item['titel']} ({gekozen_item['lijstnaam']}):")

    for maand in range(1, maanden + 1):
        # 5. Het systeem berekent per maand het cumulatieve spaarbedrag.
        gespaard = prijs * maand / maanden
        print(f"Maand {maand}: Totaal gespaard: €{gespaard}")


def toon_overzicht_per_lijst(verbinding):
    """UC7: Toont een overzicht van items per lijst inclusief statistieken zoals aantal items, goedkoopste item, duurste item, gemiddelde prijs, totaalbedrag en budgetlimiet. Waarschuwt als het totaalbedrag het budget overschrijdt."""
    lijststatistieken = haal_lijststatistieken_op(verbinding)
    if not lijststatistieken:
        print("Er zijn geen items beschikbaar voor overzicht per lijst.")
        return

    for rij in lijststatistieken:
        lijstnaam = rij['lijstnaam']
        budget_limiet = rij['budget_limiet']
        aantal_items = rij['aantal_items']
        goedkoopste_item = rij['goedkoopste_item']
        duurste_item = rij['duurste_item']
        gemiddelde_prijs = rij['gemiddelde_prijs']
        totaalbedrag_items = rij['totaalbedrag_items']
        totaalbedrag_inclusief_verzending = rij['totaalbedrag_inclusief_verzending']
        print("\033[1m" + "=== " + lijstnaam + " ===" + "\033[0m")
        print("Aantal items: " + str(aantal_items))
        print("Goedkoopste item: " + str(goedkoopste_item))
        print("Duurste item: " + str(duurste_item))
        print("Gemiddelde prijs: " + str(gemiddelde_prijs))
        print("Totaalbedrag (items): " + str(totaalbedrag_items))
        print("Totaalbedrag (incl. verzending): " + str(totaalbedrag_inclusief_verzending))
        print("Budget: " + str(budget_limiet))
        if totaalbedrag_inclusief_verzending > budget_limiet:
            print("\033[91m" + "Je budget is overschreden!" + "\033[0m")


# ==== Databasefuncties ====


def haal_verlanglijst_op(verbinding):
    """Haalt items op inclusief winkel- en lijstnaam."""
    cursor = verbinding.cursor()
    query = """
        SELECT Item.lijst as lijstnaam, Item.titel, Item.prijs, Winkel.naam as winkelnaam, Winkel.verzendkosten, Item.prioriteit
        FROM Item
        INNER JOIN Winkel ON Item.winkel = Winkel.naam
    """
    cursor.execute(query)
    return cursor.fetchall()


def haal_lijsten_op(verbinding):
    """Haalt alle lijsten op inclusief hun budgetlimiet."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam, budget_limiet FROM Lijst ORDER BY naam")
    return cursor.fetchall()


def haal_lijststatistieken_op(verbinding):
    """Haalt alle UC7-statistieken per lijst op via een geaggregeerde query over drie tabellen."""
    pass # [Programmeer databasefunctie voor het ophalen van UC7-statistieken per lijst, gebruik een SQL-query met JOIN en GROUP BY]


def update_lijstbudget(verbinding, lijstnaam, nieuw_budget):
    """Update het budgetlimiet van een lijst."""
    cursor = verbinding.cursor()
    cursor.execute(
        "UPDATE Lijst SET budget_limiet = ? WHERE naam = ?",
        (nieuw_budget, lijstnaam)
    )