import sqlite3
import onderdelenbeheer
import scenariobeheer
import importbeheer
import beveiliging

# Constante voor de naam van het databasebestand.
DATABASE = "niveau3/oefen-questcomposer/db/questcomposer.db"


# ==== Functies voor het hoofdmenu en de hoofdfunctie ====

def main():
    """Hoofdfunctie die toegang controleert, de database verbindt en het hoofdmenu afhandelt. UC8 wordt uitgevoerd wanneer optie 8 gekozen wordt."""
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
            onderdelenbeheer.pas_onderdeelprijs_aan(verbinding)
        elif keuze == "3":
            onderdelenbeheer.verwijder_onderdeel(verbinding)
        elif keuze == "4":
            scenariobeheer.pas_scenariobudget_aan(verbinding)
        elif keuze == "5":
            onderdelenbeheer.toon_onderdelen_binnen_budget(verbinding)
        elif keuze == "6":
            scenariobeheer.bereken_spaarplan(verbinding)
        elif keuze == "7":
            scenariobeheer.toon_overzicht_per_scenario(verbinding)
        elif keuze == "8":
            # Use Case 8: Afsluiten van de sessie
            print("Ontwerpsessie afgerond. Succes met prototyping!")
            print("Sessiestatistieken:")
            print(f"Onderdelen toegevoegd: {onderdelenbeheer.sessiestatistieken['toegevoegd']}")
            print(f"Onderdelen verwijderd: {onderdelenbeheer.sessiestatistieken['verwijderd']}")
            break
        elif keuze == "9":
            importbeheer.importeer_csv(verbinding)
        else:
            print("Ongeldige keuze.")

    verbinding.close()


def toon_menu():
    """Toont het hoofdmenu en vraagt de gebruiker om een keuze te maken."""
    print("--- QuestComposer ---")
    print("1. Registreer nieuw puzzelonderdeel")
    print("2. Herbereken kostprijs van onderdeel")
    print("3. Schrap onderdeel uit build")
    print("4. Stel scenariobudget bij")
    print("5. Zoek alternatieven binnen restbudget")
    print("6. Maak inkoopritme voor sleutelonderdeel")
    print("7. Toon haalbaarheidsoverzicht per scenario")
    print("8. Sluit ontwerpsessie af")
    print("9. Importeer intakebestand uit CSV")
    return input("Maak een keuze: ")


# ==== Databasefuncties ====

def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect(DATABASE)
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding


# ==== Applicatie startpunt ====

if __name__ == "__main__":
    main()