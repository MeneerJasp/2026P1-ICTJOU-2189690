import os
import sqlite3
import hashlib
import os
import csv

# Configuratievariabelen (constanten)
STANDAARD_VERZENDKOSTEN = 0.00
STANDAARD_LIJSTBUDGET = 100.00

# Maak hier globale variabelen om statistieken bij te houden:




# ==== Functies voor het hoofdmenu en de hoofdfunctie ====


def main():
    """Hoofdfunctie die de verbinding met de database maakt en het hoofdmenu toont totdat de gebruiker ervoor kiest om af te sluiten."""
    # [Programmeer: Controleer toegangscode voordat de gebruiker verder kan]

    verbinding = maak_verbinding()
    if not verbinding:
        return

    while True:
        keuze = toon_menu()
        if keuze == '1':
            itembeheer.voeg_item_toe(verbinding)
        elif keuze == '2':
            itembeheer.pas_itemprijs_aan(verbinding)
        elif keuze == '3':
            itembeheer.verwijder_item(verbinding)
        elif keuze == '4':
            lijstbeheer.pas_lijstbudget_aan(verbinding)
        elif keuze == '5':
            itembeheer.toon_items_binnen_budget(verbinding)
        elif keuze == '6':
            lijstbeheer.bereken_spaarplan(verbinding)
        elif keuze == '7':
            lijstbeheer.toon_overzicht_per_lijst(verbinding)
        elif keuze == '8':
            print("Succes met sparen!")
            print("Sessiestatistieken:")
            # UC8: Print hier hoeveel items er in deze sessie zijn toegevoegd en verwijderd:

            break
        elif keuze == '9':
            importbeheer.importeer_csv(verbinding)
        else:
            print("Ongeldige keuze.")

def toon_menu():
    """Toont het hoofdmenu en vraagt de gebruiker om een keuze te maken."""
    print('--- Verlanglijstmanager ---')
    print('1. Voeg item toe aan verlanglijst')
    print('2. Pas item prijs aan')
    print('3. Verwijder item')
    print('4. Pas lijstbudget aan')
    print('5. Zoek items op budget')
    print('6. Persoonlijk spaarplan berekenen')
    print('7. Uitgaven per lijst inzien')
    print('8. Afsluiten')
    print('9. Importeer items uit CSV')
    return input('Maak een keuze: ')

# ==== Use Case functies ====

def voeg_item_toe(verbinding):
    """UC1: Voegt een nieuw item toe aan de verlanglijst. Controleert of de opgegeven winkel en lijst bestaan voordat het item wordt toegevoegd."""
    lijstnaam = kies_verlanglijst(verbinding)
    if lijstnaam is None:
        return

    naam = input("Naam van het item: ")
    prijs = float(input("Prijs van het item: "))
    winkelnaam = input("Winkel waar je het wilt kopen: ")
    if not check_winkel_bestaat(verbinding, winkelnaam):
        print("FOUT: Winkel bestaat niet.")
        return
    prio = int(input("Prioriteit (1-3): "))
    prio = max(1, min(prio, 3))
    
    voeg_item_toe_aan_db(verbinding, naam, prijs, winkelnaam, lijstnaam, prio)

    # Voeg aan de globale sessiestatistieken toe dat er een item is toegevoegd:
    

    print(f"Item succesvol toegevoegd! (totaal deze sessie: {sessiestatistieken['toegevoegd']})")

def pas_itemprijs_aan(verbinding):
    """UC2: Past de prijs van een bestaand item aan op basis van een gekozen lijst en titel."""
    pass # [Programmeer Use Case 2, gebruik de functie kies_verlanglijst en haal_items_van_lijst_op, en update_prijs om de prijs aan te passen]

def pas_lijstbudget_aan(verbinding):
    """UC3: Past het budgetlimiet van een lijst aan op basis van de gebruikersinvoer."""
    pass # [Programmeer Use Case 3, gebruik de functie haal_lijsten_op en update_lijstbudget om het budget aan te passen]

def verwijder_item(verbinding):
    """UC4: Verwijdert een item van de verlanglijst op basis van een gekozen lijst en titel."""
    pass # [Programmeer Use Case 4, gebruik de functie kies_verlanglijst en haal_items_van_lijst_op, en verwijder_item_uit_db om het item te verwijderen]

def toon_items_binnen_budget(verbinding):
    """UC5: Toont items waarvan de prijs tussen twee opgegeven budgetgrenzen ligt."""

    # Stap 2. Het systeem vraagt om twee budgetgrenzen:
    grens1 = float(input("Voer de eerste budgetgrens in: ")) # is dit de hoogste of laagste grens? 
    grens2 = float(input("Voer de tweede budgetgrens in: "))

    # Stap 3. Het systeem bepaalt automatisch de laagste en hoogste grens:
    min_budget = # gebruik een python-functie om de laagste waarde te bepalen
    max_budget = # gebruik een python-functie om de hoogste waarde te bepalen

    # 4. Het systeem haalt alle items op die binnen dit prijsbereik vallen.
    items = haal_items_binnen_budget(verbinding, ?)
    if not items:
        print("Er zijn geen items binnen het opgegeven budgetbereik.")
        return

    print(f"Items tussen €{min_budget} en €{max_budget}:")
    for item in items:
        print(f"{item['titel']} - €{item['prijs']}")

def bereken_spaarplan(verbinding):
    """UC6: Bereken een persoonlijk spaarplan voor een gekozen item op basis van de prijs en het aantal maanden dat de gebruiker wil sparen."""

    # 2. Het systeem toont een genummerde lijst van alle items met hun huidige prijs:
    items = haal_verlanglijst_op(verbinding)
    if not items:
        print("Er zijn geen items beschikbaar voor een spaarplan.")
        return

    for ??
        print(f"{volgnummer}. [{item['lijstnaam']}] {item['titel']} - €{item['prijs']:.2f}")

    # 3. De student voert het nummer (index) van het gewenste item in.
    keuze = int(input("Voor welk item wil je een spaarplan? (nummer): "))
    if ??:
        print("Ongeldige keuze.")
        return

    gekozen_item = items[??]
    prijs = float(gekozen_item['prijs'])

    # 4. Het systeem vraagt over hoeveel maanden het item gekocht moet worden.
    maanden = int(input("Over hoeveel maanden wil je dit kopen? "))

    # 6. Het systeem toont voor elke maand het totale bedrag dat tot dan toe gespaard moet zijn.
    print(f"Spaarplan voor {gekozen_item['titel']} ({gekozen_item['lijstnaam']}):")
    
    for maand in range(1, maanden + 1):
        # 5. Het systeem berekent per maand het cumulatieve spaarbedrag.
        gespaard = ??
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


def importeer_csv(verbinding):
    """UC9: Importeert items vanuit een CSV-bestand en voegt deze toe aan de database. Voegt benodigde winkels en lijsten toe indien deze nog niet bestaan."""
 
    # Programmeer Use Case 9


    print("CSV succesvol geimporteerd!")

def controleer_toegangscode():
    """UC10: Controleert of de ingevoerde toegangscode klopt."""

    # Programmeer Use Case 10, vraag gebruiker om toegangscode in te voeren,
    # hash deze met behulp van:
    hash = hashlib.sha256(ingevoerde_code.encode()).hexdigest()
    # maak gebruik van de functie lees_toegangscode_hash() om de hash van de toegangscode uit het .env-bestand te lezen
    # en vergelijk deze met de hash van de door de gebruiker ingevoerde toegangscode.
 


# === Helper functies ===

def toon_beschikbare_verlanglijsten(verbinding):
    """Toont alle beschikbare verlanglijsten en geeft ze terug."""
    pass # [Programmeer functie tonen van beschikbare verlanglijsten, gebruik de functie haal_lijsten_op]


def kies_verlanglijst(verbinding):
    """Vraagt de gebruiker om eerst een verlanglijst te kiezen."""
    pass # [Programmeer functie om een verlanglijst te kiezen, gebruik de functie toon_beschikbare_verlanglijsten] 


def lees_toegangscode_hash():
    """Leest de hash van de toegangscode uit het .env-bestand."""
    
    # Programmeer deze functie met behulp van de voorbeeldcode uit de les.

# ==== Databasefuncties ====

def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect("db/verlanglijstmanager.db")
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding

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
    pass # [Programmeer databasefunctie voor het ophalen van items van een specifieke lijst]

def haal_lijsten_op(verbinding):
    """Haalt alle lijsten op inclusief hun budgetlimiet."""
    pass # [Programmeer databasefunctie voor het ophalen van lijsten]


def update_prijs(verbinding, ?):
    """Update de prijs van een item op basis van lijstnaam en titel."""
    pass # [Programmeer databasefunctie voor het updaten van de prijs van een item]


def verwijder_item_uit_db(verbinding, ?):
    """Verwijdert een item op basis van lijstnaam en titel."""
    pass # [Programmeer databasefunctie voor het verwijderen van een item]


def voeg_item_toe_aan_db(verbinding, titel, prijs, winkel_naam, lijst_naam, prio):
    """Voegt een nieuw item toe aan de database."""
    cursor = verbinding.cursor()
    query = """
        INSERT INTO Item (lijst, titel, prijs, winkel, prioriteit)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (lijst_naam, titel, prijs, winkel_naam, prio))


def haal_items_binnen_budget(verbinding, ?):
    """Haal items op waarvan de prijs tussen min_budget en max_budget ligt."""
    pass # [Programmeer databasefunctie voor het ophalen van items binnen een budget]


def check_winkel_bestaat(verbinding, winkelnaam):
    """Controleert of een winkel al bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam FROM Winkel WHERE naam = ?", (winkelnaam,))
    if cursor.fetchone() is not None:
        return True
    else:
        return False

def haal_verlanglijst_op(verbinding):
    """Haalt items op inclusief winkel- en lijstnaam."""
    cursor = verbinding.cursor()
    query = """
        SELECT Item.lijst as lijstnaam, Item.titel, Item.prijs, Winkel.naam as winkelnaam, Winkel.verzendkosten, Item.prioriteit
        .....
    """
    cursor.execute(query)
    return cursor.fetchall()


def haal_lijsten_op(verbinding):
    """Haalt alle lijsten op inclusief hun budgetlimiet."""
    pass # [Programmeer databasefunctie voor het ophalen van lijsten]


def haal_lijststatistieken_op(verbinding):
    """Haalt alle UC7-statistieken per lijst op via een geaggregeerde query over drie tabellen."""
    pass # [Programmeer databasefunctie voor het ophalen van UC7-statistieken per lijst, gebruik een SQL-query met JOIN en GROUP BY]


def update_lijstbudget(verbinding, lijstnaam, nieuw_budget):
    """Update het budgetlimiet van een lijst."""
    pass # [Programmeer databasefunctie voor het updaten van het budgetlimiet van een lijst]
  

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
    cursor.execute("INSERT INTO Winkel (naam, verzendkosten) VALUES (?, ?)", (winkelnaam, verzendkosten))


def voeg_lijst_toe(verbinding, lijstnaam, budget_limiet):
    """Voegt een nieuwe lijst toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute("INSERT INTO Lijst (naam, budget_limiet) VALUES (?, ?)", (lijstnaam, budget_limiet))


def voeg_item_toe_aan_db(verbinding, titel, prijs, winkel_naam, lijst_naam, prio):
    """Voegt een nieuw item toe aan de database."""
    cursor = verbinding.cursor()
    query = """
        INSERT INTO Item (lijst, titel, prijs, winkel, prioriteit)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (lijst_naam, titel, prijs, winkel_naam, prio))


# ==== Applicatie startpunt ====

if __name__ == "__main__":
    main()