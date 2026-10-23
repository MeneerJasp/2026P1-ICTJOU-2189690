# Globale variabelen om statistieken bij te houden
sessiestatistieken = {
    'toegevoegd': 0,
    'verwijderd': 0,
}


# ==== Use Case functies ====


def voeg_item_toe(verbinding):
    """UC1: Voegt een nieuw item toe aan de verlanglijst. Controleert of de opgegeven winkel en lijst bestaan voordat het item wordt toegevoegd."""
    lijstnaam = kies_verlanglijst(verbinding)
    if lijstnaam is None:
        return

    naam = input("Naam van het item: ")
    prijs = float(input("Prijs van het item: ").replace(",", "."))
    winkelnaam = input("Winkel waar je het wilt kopen: ")
    if not check_winkel_bestaat(verbinding, winkelnaam):
        print("FOUT: Winkel bestaat niet.")
        return
    prio = int(input("Prioriteit (1-3): "))
    prio = max(1, min(prio, 3))

    voeg_item_toe_aan_db(verbinding, naam, prijs, winkelnaam, lijstnaam, prio)

    # Voeg aan de globale sessiestatistieken toe dat er een item is toegevoegd:
    sessiestatistieken['toegevoegd'] += 1

    print(f"Item succesvol toegevoegd! (totaal deze sessie: {sessiestatistieken['toegevoegd']})")


def pas_itemprijs_aan(verbinding):
    """UC2: Past de prijs van een bestaand item aan op basis van een gekozen lijst en titel."""
    lijstnaam = kies_verlanglijst(verbinding)
    if lijstnaam is None:
        return

    items = haal_items_van_lijst_op(verbinding, lijstnaam)
    if not items:
        print("Er zijn geen items in deze verlanglijst.")
        return

    for volgnummer, item in enumerate(items, start=1):
        print(f"{volgnummer}. {item['titel']} - €{item['prijs']:.2f}")

    keuze = int(input("Welk item wil je aanpassen? (nummer): "))
    if keuze < 1 or keuze > len(items):
        print("Ongeldige keuze.")
        return

    nieuwe_prijs = float(input("Nieuwe prijs: ").replace(",", "."))
    if nieuwe_prijs < 0:
        print("Ongeldige prijs.")
        return

    titel = items[keuze - 1]['titel']
    update_prijs(verbinding, lijstnaam, titel, nieuwe_prijs)
    print(f"De prijs van {titel} is aangepast naar €{nieuwe_prijs:.2f}.")


def verwijder_item(verbinding):
    """UC4: Verwijdert een item van de verlanglijst op basis van een gekozen lijst en titel."""
    lijstnaam = kies_verlanglijst(verbinding)
    if lijstnaam is None:
        return

    items = haal_items_van_lijst_op(verbinding, lijstnaam)
    if not items:
        print("Er zijn geen items in deze verlanglijst.")
        return

    for volgnummer, item in enumerate(items, start=1):
        print(f"{volgnummer}. {item['titel']} - €{item['prijs']:.2f}")

    keuze = int(input("Welk item wil je verwijderen? (nummer): "))
    if keuze < 1 or keuze > len(items):
        print("Ongeldige keuze.")
        return

    titel = items[keuze - 1]['titel']
    verwijder_item_uit_db(verbinding, lijstnaam, titel)

    # Sessieteller voor verwijderde items verhogen.
    sessiestatistieken['verwijderd'] += 1

    print(f"Item succesvol verwijderd! (totaal deze sessie: {sessiestatistieken['verwijderd']})")


def toon_items_binnen_budget(verbinding):
    """UC5: Toont items waarvan de prijs tussen twee opgegeven budgetgrenzen ligt."""

    # Stap 2. Het systeem vraagt om twee budgetgrenzen:
    grens1 = float(input("Voer de eerste budgetgrens in: ").replace(",", "."))
    grens2 = float(input("Voer de tweede budgetgrens in: ").replace(",", "."))

    # Stap 3. Het systeem bepaalt automatisch de laagste en hoogste grens:
    min_budget = min(grens1, grens2)
    max_budget = max(grens1, grens2)

    # 4. Het systeem haalt alle items op die binnen dit prijsbereik vallen.
    items = haal_items_binnen_budget(verbinding, min_budget, max_budget)
    if not items:
        print("Er zijn geen items binnen het opgegeven budgetbereik.")
        return

    print(f"Items tussen €{min_budget} en €{max_budget}:")
    for item in items:
        print(f"{item['titel']} - €{item['prijs']}")


# === Helper functies ===


def toon_beschikbare_verlanglijsten(verbinding):
    """Toont alle beschikbare verlanglijsten en geeft ze terug."""
    lijsten = haal_lijsten_op(verbinding)
    if not lijsten:
        print("Er zijn geen verlanglijsten.")
        return []
    for volgnummer, lijst in enumerate(lijsten, start=1):
        print(f"{volgnummer}. {lijst['naam']}")
    return lijsten


def kies_verlanglijst(verbinding):
    """Vraagt de gebruiker om eerst een verlanglijst te kiezen."""
    lijsten = toon_beschikbare_verlanglijsten(verbinding)
    if not lijsten:
        return None

    keuze = int(input("Welke verlanglijst kies je? (nummer): "))
    if keuze < 1 or keuze > len(lijsten):
        print("Ongeldige keuze.")
        return None

    return lijsten[keuze - 1]['naam']


# ==== Databasefuncties ====


def haal_alle_items_op(verbinding):
    """Haalt alle items op inclusief winkel- en lijstnaam."""
    cursor = verbinding.cursor()
    query = """
        SELECT Item.lijst as lijstnaam, Item.titel, Item.prijs, Winkel.naam as winkelnaam, Winkel.verzendkosten, Item.prioriteit
        FROM Item
        INNER JOIN Winkel ON Item.winkel = Winkel.naam
    """
    cursor.execute(query)
    return cursor.fetchall()


def haal_items_van_lijst_op(verbinding, lijstnaam):
    """Haalt alleen items van een specifieke verlanglijst op via SQL-filtering."""
    cursor = verbinding.cursor()
    cursor.execute(
        "SELECT titel, prijs FROM Item WHERE lijst = ? ORDER BY titel",
        (lijstnaam,)
    )
    return cursor.fetchall()


def haal_lijsten_op(verbinding):
    """Haalt alle lijsten op inclusief hun budgetlimiet."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam, budget_limiet FROM Lijst ORDER BY naam")
    return cursor.fetchall()


def update_prijs(verbinding, lijstnaam, titel, nieuwe_prijs):
    """Update de prijs van een item op basis van lijstnaam en titel."""
    cursor = verbinding.cursor()
    cursor.execute(
        "UPDATE Item SET prijs = ? WHERE lijst = ? AND titel = ?",
        (nieuwe_prijs, lijstnaam, titel)
    )


def verwijder_item_uit_db(verbinding, lijstnaam, titel):
    """Verwijdert een item op basis van lijstnaam en titel."""
    cursor = verbinding.cursor()
    cursor.execute(
        "DELETE FROM Item WHERE lijst = ? AND titel = ?",
        (lijstnaam, titel)
    )


def voeg_item_toe_aan_db(verbinding, titel, prijs, winkel_naam, lijst_naam, prio):
    """Voegt een nieuw item toe aan de database."""
    cursor = verbinding.cursor()
    query = """
        INSERT INTO Item (lijst, titel, prijs, winkel, prioriteit)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (lijst_naam, titel, prijs, winkel_naam, prio))


def haal_items_binnen_budget(verbinding, min_budget, max_budget):
    """Haal items op waarvan de prijs tussen min_budget en max_budget ligt."""
    cursor = verbinding.cursor()
    # BETWEEN zoekt inclusief de ondergrens en bovengrens.
    cursor.execute(
        "SELECT titel, prijs FROM Item WHERE prijs BETWEEN ? AND ?",
        (min_budget, max_budget)
    )
    return cursor.fetchall()


def check_winkel_bestaat(verbinding, winkelnaam):
    """Controleert of een winkel al bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam FROM Winkel WHERE naam = ?", (winkelnaam,))
    if cursor.fetchone() is not None:
        return True
    else:
        return False