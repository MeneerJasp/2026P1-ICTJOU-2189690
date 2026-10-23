import sqlite3
import onderdelenbeheer
import scenariobeheer
import importbeheer
import beveiliging

# Constante voor de naam van het databasebestand.
DATABASE = "niveau3/oefen-questcomposer/db/questcomposer.db"


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
            onderdelenbeheer.voeg_onderdeel_toe(verbinding)
        elif keuze == "2":
            onderdelenbeheer.pas_onderdeelkosten_aan(verbinding)
        elif keuze == "3":
            scenariobeheer.pas_scenariobudget_aan(verbinding)
        elif keuze == "4":
            onderdelenbeheer.verwijder_onderdeel(verbinding)
        elif keuze == "5":
            onderdelenbeheer.toon_onderdelen_binnen_budget(verbinding)
        elif keuze == "6":
            scenariobeheer.bereken_spaarplan(verbinding)
        elif keuze == "7":
            scenariobeheer.toon_overzicht_per_scenario(verbinding)
        elif keuze == "8":
            importbeheer.importeer_csv(verbinding)
        elif keuze == "9":
            print("Succes met het plannen van je LARP-avonturen!")
            print("Sessiestatistieken:")
            print(f"- Aantal onderdelen toegevoegd: {onderdelenbeheer.aantal_onderdelen_toegevoegd}")
            print(f"- Aantal onderdelen verwijderd: {onderdelenbeheer.aantal_onderdelen_verwijderd}")
            break
        else:
            print("Ongeldige keuze.")

    verbinding.close()


def toon_menu():
    """Toont het hoofdmenu en geeft de gekozen optie terug."""
    print("\n--- LARP QuestComposer Menu ---")
    print("1. Onderdeel toevoegen")
    print("2. Onderdeelkosten aanpassen")
    print("3. Scenariobudget aanpassen")
    print("4. Onderdeel verwijderen")
    print("5. Onderdelen zoeken binnen budget")
    print("6. Spaarplan berekenen")
    print("7. Overzicht tonen per scenario")
    print("8. Onderdelen importeren uit CSV-bestand")
    print("9. Afsluiten")
    return input("Kies een optie: ")


# ==== Databasefuncties ====

def maak_verbinding():
    """Maakt verbinding met de database en geeft het verbindingsobject terug."""
    verbinding = sqlite3.connect(DATABASE)
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding


# ==== Applicatie startpunt ====
if __name__ == "__main__":
    main()