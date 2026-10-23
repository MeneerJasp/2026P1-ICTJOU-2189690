# ==== Use Case functies ====

def pas_lijstbudget_aan(verbinding):
    """UC3: Past het budgetlimiet van een lijst aan op basis van de gebruikersinvoer."""
    lijsten = haal_lijsten_op(verbinding)
    if len(lijsten) == 0:
        print("Fout: Er zijn geen lijsten beschikbaar.")
        return

    print("Beschikbare verlanglijsten:")
    for volgnummer, lijst in enumerate(lijsten, start=1):
        print(f"{volgnummer}. {lijst['naam']} (Huidig budget: EUR {lijst['budget_limiet']:.2f})")

    keuze = int(input("Kies een lijst (nummer): "))
    if keuze < 1 or keuze > len(lijsten):
        print("Ongeldige keuze.")
        return

    gekozen_lijst = lijsten[keuze - 1]["naam"]
    nieuw_budget = float(input("Voer het nieuwe budget in: ").replace(",", "."))
    if nieuw_budget < 0:
        print("Ongeldig budget.")
        return

    update_lijstbudget(verbinding, gekozen_lijst, nieuw_budget)
    print("Lijstbudget succesvol bijgewerkt!")


def bereken_spaarplan(verbinding):
    """UC6: Bereken een persoonlijk spaarplan voor een gekozen item op basis van de prijs en het aantal maanden dat de gebruiker wil sparen."""
    items = haal_verlanglijst_op(verbinding)
    if len(items) == 0:
        print("Fout: Er zijn geen items beschikbaar.")
        return

    for volgnummer, item in enumerate(items, start=1):
        print(f"{volgnummer}. [{item['lijstnaam']}] {item['titel']} - EUR {item['prijs']:.2f}")

    keuze = int(input("Voor welk item wil je een spaarplan? (nummer): "))
    if keuze < 1 or keuze > len(items):
        print("Ongeldige keuze.")
        return

    gekozen_item = items[keuze - 1]
    prijs = float(gekozen_item["prijs"])

    maanden = int(input("Over hoeveel maanden wil je dit kopen? "))
    if maanden <= 0:
        print("Ongeldig aantal maanden.")
        return

    print(f"Spaarplan voor {gekozen_item['titel']} ({gekozen_item['lijstnaam']}):")
    for maand in range(1, maanden + 1):
        gespaard = prijs * maand / maanden
        print(f"Maand {maand}: Totaal gespaard: EUR {gespaard:.2f}")


def toon_overzicht_per_lijst(verbinding):
    """UC7: Toont een overzicht van items per lijst inclusief statistieken en waarschuwt als het totaalbedrag het budget overschrijdt."""
    lijststatistieken = haal_lijststatistieken_op(verbinding)
    if not lijststatistieken:
        print("Er zijn geen items beschikbaar voor overzicht per lijst.")
        return

    for rij in lijststatistieken:
        lijstnaam = rij["lijstnaam"]
        budget_limiet = rij["budget_limiet"]
        aantal_items = rij["aantal_items"]
        goedkoopste_item = rij["goedkoopste_item"]
        duurste_item = rij["duurste_item"]
        gemiddelde_prijs = rij["gemiddelde_prijs"]
        totaalbedrag_items = rij["totaalbedrag_items"]
        totaalbedrag_inclusief_verzending = rij["totaalbedrag_inclusief_verzending"]

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

def haal_lijsten_op(verbinding):
    """Haalt alle lijsten op inclusief hun budgetlimiet."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam, budget_limiet FROM Lijst ORDER BY naam")
    return cursor.fetchall()


def update_lijstbudget(verbinding, lijstnaam, nieuw_budget):
    """Update het budgetlimiet van een lijst."""
    cursor = verbinding.cursor()
    cursor.execute(
        "UPDATE Lijst SET budget_limiet = ? WHERE naam = ?",
        (nieuw_budget, lijstnaam)
    )


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


def haal_lijststatistieken_op(verbinding):
    """Haalt alle UC7-statistieken per lijst op via een geaggregeerde query over drie tabellen."""
    cursor = verbinding.cursor()
    # INNER JOIN over Lijst, Item en Winkel met GROUP BY per lijst.
    query = """
        SELECT
            l.naam AS lijstnaam,
            l.budget_limiet,
            COUNT(i.titel) AS aantal_items,
            MIN(i.prijs) AS goedkoopste_item,
            MAX(i.prijs) AS duurste_item,
            AVG(i.prijs) AS gemiddelde_prijs,
            SUM(i.prijs) AS totaalbedrag_items,
            SUM(i.prijs + w.verzendkosten) AS totaalbedrag_inclusief_verzending
        FROM Lijst l
        INNER JOIN Item i ON i.lijst = l.naam
        INNER JOIN Winkel w ON w.naam = i.winkel
        GROUP BY l.naam, l.budget_limiet
        ORDER BY l.naam
    """
    cursor.execute(query)
    return cursor.fetchall()