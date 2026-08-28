"""Beheer van attractiegegevens voor de Oosteling-onderhoudsapplicatie.

Bevat functies voor import, opslag, validatie en weergave van attracties.
"""

import csv

attracties_csv = 'data/attracties.csv'

def importeer_attracties_uit_csv(verbinding):
    """Importeert attracties uit een CSV-bestand en voegt ze toe aan de database."""
    with open(attracties_csv, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for rij in csv_reader:
            naam = rij['naam']
            bouwjaar = rij['bouwjaar']
            locatie = rij['locatie']
            omschrijving = rij['omschrijving']
            voeg_attractie_toe_aan_database(verbinding, naam, bouwjaar, locatie, omschrijving)

def voeg_attractie_toe(verbinding):
    """Voegt een nieuwe attractie toe aan de database."""
    naam = input("Voer de naam van de attractie in: ")
    bouwjaar = input("Voer het bouwjaar van de attractie in: ")
    bouwjaar = int(bouwjaar)
    locatie = input("Voer de locatie van de attractie in: ")
    omschrijving = input("Voer een korte omschrijving van de attractie in: ")
    voeg_attractie_toe_aan_database(verbinding, naam, bouwjaar, locatie, omschrijving)

def voeg_attractie_toe_aan_database(verbinding, naam, bouwjaar, locatie, omschrijving):
    """Voegt een nieuwe attractie toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute("INSERT INTO attractie (naam, bouwjaar, locatie, omschrijving) VALUES (?, ?, ?, ?)", (naam, bouwjaar, locatie, omschrijving))
    print(f"Attractie '{naam}' succesvol toegevoegd aan de database.")
    
def attractie_bestaat(verbinding, naam):
    """Controleert of een attractie met de gegeven naam bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT COUNT(*) FROM attractie WHERE naam = ?", (naam,))
    row = cursor.fetchone()
    return row is not None and row[0] > 0

def toon_attracties(verbinding):
    """Toont alle attracties uit de database."""
    attracties = haal_attracties_op_uit_database(verbinding)
    for attractie in attracties:
        print(f"Naam: {attractie['naam']}, Bouwjaar: {attractie['bouwjaar']}, Locatie: {attractie['locatie']}, Omschrijving: {attractie['omschrijving']}")

def haal_attracties_op_uit_database(verbinding):
    """Haalt alle attracties op uit de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam, bouwjaar, locatie, omschrijving FROM attractie")
    return cursor.fetchall()

