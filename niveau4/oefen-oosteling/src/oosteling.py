"""Startmodule voor de Oosteling-onderhoudsapplicatie.

Bevat de programmastroom, databaseverbinding en menuafhandeling.
"""

import sqlite3
import beveiliging
import attractie
import onderhoudstype
import onderhoudslog

def maak_verbinding():
    '''Maakt een verbinding met de database.'''
    verbinding = sqlite3.connect('db/oosteling.db')
    verbinding.row_factory = sqlite3.Row
    verbinding.execute('PRAGMA foreign_keys = ON')
    verbinding.autocommit = True
    return verbinding

def toon_menu():
    """Toont het hoofdmenu en vraagt de gebruiker om een keuze te maken."""
    print("Hoofdmenu:")
    print("1. Importeer attracties uit CSV-bestand")
    print("2. Importeer onderhoudstypes uit CSV-bestand")
    print("3. Voeg een nieuwe attractie toe")
    print("4. Voeg een nieuw onderhoudstype toe")
    print("5. Registreer uitgevoerd onderhoud")
    print("6. Toon alle attracties")
    print("7. Toon alle onderhoudstypes")
    print("8. Toon alle uitgevoerde onderhoudsregistraties")
    print("9. Visualiseer aantal uitgevoerde onderhoudsregistraties per attractie")
    print("10. Visualiseer aantal uitgevoerde onderhoudsregistraties per onderhoudstype")
    print("11. Toon attracties in categorieen op basis van totale dagen buiten bedrijf")
    print("x. Exit")

    keuze = input("Maak een keuze: ")
    return keuze

def main():
    """Hoofdfunctie die de verbinding met de database maakt en het hoofdmenu toont totdat de gebruiker ervoor kiest om af te sluiten."""
    if not beveiliging.controleer_toegangscode():
        return

    verbinding = maak_verbinding()
    
    # Menu-afhandeling
                
if __name__ == "__main__":
    main()