import os
import sqlite3
import hashlib
import os
import csv
import math

DATABASE = "verlanglijstmanager.db"

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
            voeg_item_toe(verbinding)
        elif keuze == '2':
            pas_itemprijs_aan(verbinding)
        elif keuze == '3':
            verwijder_item(verbinding)
        elif keuze == '4':
            pas_lijstbudget_aan(verbinding)
        elif keuze == '5':
            toon_items_binnen_budget(verbinding)
        elif keuze == '6':
            bereken_spaarplan(verbinding)
        elif keuze == '7':
            toon_overzicht_per_lijst(verbinding)
        elif keuze == '8':
            print("Succes met sparen!")
            print("Sessiestatistieken:")
            # UC8: Print hier hoeveel items er in deze sessie zijn toegevoegd en verwijderd:

            break
        elif keuze == '9':
            importeer_csv(verbinding)
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

def lees_toegangscode_hash():
    """Leest de hash van de toegangscode uit het .env-bestand."""
    
    # Programmeer deze functie met behulp van de voorbeeldcode uit de les.


# ==== Databasefuncties ====

def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect(DATABASE)
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
    pass # [Programmeer databasefunctie voor het verwijderen van een item]


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
    pass # [Programmeer databasefunctie voor het ophalen van items binnen een budget]


# ==== Use case functie ====

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

    try:
        keuze = int(input("Welk item wil je aanpassen? (nummer): "))
    except ValueError:
        print("Ongeldige keuze.")
        return
    if not 1 <= keuze <= len(items):
        print("Ongeldige keuze.")
        return

    try:
        nieuwe_prijs = float(input("Nieuwe prijs: ").replace(",", "."))
    except ValueError:
        print("Ongeldige prijs.")
        return
    if not math.isfinite(nieuwe_prijs) or nieuwe_prijs < 0:
        print("Ongeldige prijs.")
        return

    titel = items[keuze - 1]['titel']
    update_prijs(verbinding, lijstnaam, titel, nieuwe_prijs)
    print(f"De prijs van {titel} is aangepast naar €{nieuwe_prijs:.2f}.")


if __name__ == "__main__":
    main()
