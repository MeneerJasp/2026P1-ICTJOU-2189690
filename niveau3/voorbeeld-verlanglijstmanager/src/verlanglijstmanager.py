import sqlite3
import itembeheer
import lijstbeheer
import importbeheer
import beveiliging

DATABASE = "niveau3/voorbeeld-verlanglijstmanager/db/verlanglijstmanager.db"


# ==== Functies voor het hoofdmenu en de hoofdfunctie ====

def main():
    """Hoofdfunctie die de verbinding met de database maakt en het hoofdmenu toont totdat de gebruiker ervoor kiest om af te sluiten."""
    if not beveiliging.controleer_toegangscode():
        return

    verbinding = maak_verbinding()
    if not verbinding:
        return

    while True:
        keuze = toon_menu()
        if keuze == "1":
            itembeheer.voeg_item_toe(verbinding)
        elif keuze == "2":
            itembeheer.pas_itemprijs_aan(verbinding)
        elif keuze == "3":
            itembeheer.verwijder_item(verbinding)
        elif keuze == "4":
            lijstbeheer.pas_lijstbudget_aan(verbinding)
        elif keuze == "5":
            itembeheer.toon_items_binnen_budget(verbinding)
        elif keuze == "6":
            lijstbeheer.bereken_spaarplan(verbinding)
        elif keuze == "7":
            lijstbeheer.toon_overzicht_per_lijst(verbinding)
        elif keuze == "8":
            print("Succes met sparen!")
            print("Sessiestatistieken:")
            print(f"Items toegevoegd: {itembeheer.sessiestatistieken['toegevoegd']}")
            print(f"Items verwijderd: {itembeheer.sessiestatistieken['verwijderd']}")
            break
        elif keuze == "9":
            importbeheer.importeer_csv(verbinding)
        else:
            print("Ongeldige keuze.")

    verbinding.close()


def toon_menu():
    """Toont het hoofdmenu en vraagt de gebruiker om een keuze te maken."""
    print("--- Verlanglijstmanager ---")
    print("1. Voeg item toe aan verlanglijst")
    print("2. Pas item prijs aan")
    print("3. Verwijder item")
    print("4. Pas lijstbudget aan")
    print("5. Zoek items op budget")
    print("6. Persoonlijk spaarplan berekenen")
    print("7. Uitgaven per lijst inzien")
    print("8. Afsluiten")
    print("9. Importeer items uit CSV")
    return input("Maak een keuze: ")


# ==== Databasefuncties ====

def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect(DATABASE)
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding


if __name__ == "__main__":
    main()