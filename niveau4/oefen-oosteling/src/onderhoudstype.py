"""Beheer van onderhoudstypes voor de Oosteling-onderhoudsapplicatie.

Bevat functies voor import, opslag, validatie en weergave van onderhoudstypes.
"""

import csv

onderhoudstypes_csv = 'data/onderhoudstypes.csv'

def importeer_onderhoudstypes_uit_csv(verbinding):
    ''' Importeert onderhoudstypes uit een CSV-bestand en voegt ze toe aan de database. '''
    with open(onderhoudstypes_csv, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for rij in csv_reader:
            naam = rij['naam']
            veiligheidskritisch = rij['is_veiligheidskritisch']
            omschrijving = rij['omschrijving']
            voeg_onderhoudstype_toe_aan_database(verbinding, naam, veiligheidskritisch, omschrijving)

def voeg_onderhoudstype_toe(verbinding):
    """Voegt een nieuw onderhoudstype toe aan de database."""
    naam = input("Voer de naam van het onderhoudstype in: ")
    veiligheidskritisch = input("Is dit onderhoudstype veiligheidskritisch? (ja/nee): ")
    if veiligheidskritisch == 'ja':
        veiligheidskritisch = 1
    else:
        veiligheidskritisch = 0
    omschrijving = input("Voer een korte omschrijving van het onderhoudstype in: ")
    voeg_onderhoudstype_toe_aan_database(verbinding, naam, veiligheidskritisch, omschrijving)

def voeg_onderhoudstype_toe_aan_database(verbinding, naam, veiligheidskritisch, omschrijving):
    """Voegt een nieuw onderhoudstype toe aan de database."""
    cursor = verbinding.cursor()
    cursor.execute("INSERT INTO onderhoudstype (naam, is_veiligheidskritisch, omschrijving) VALUES (?, ?, ?)", (naam, veiligheidskritisch, omschrijving))
    print(f"Onderhoudstype '{naam}' succesvol toegevoegd aan de database.")

def toon_onderhoudstypes(verbinding):
    """Toont alle onderhoudstypes in de database."""
    onderhoudstypes = haal_onderhoudstypes_op_uit_database(verbinding)
    for onderhoudstype in onderhoudstypes:
        print(f"Naam: {onderhoudstype['naam']}, Veiligheidskritisch: {'Ja' if onderhoudstype['is_veiligheidskritisch'] else 'Nee'}, Omschrijving: {onderhoudstype['omschrijving']}")
        
def haal_onderhoudstypes_op_uit_database(verbinding):
    """Haalt alle onderhoudstypes op uit de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT naam, is_veiligheidskritisch, omschrijving FROM onderhoudstype")
    return cursor.fetchall()

def onderhoudstype_bestaat(verbinding, onderhoudstype):
    """Controleert of een onderhoudstype met de gegeven naam bestaat in de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT COUNT(*) FROM onderhoudstype WHERE naam = ?", (onderhoudstype,))
    row = cursor.fetchone()
    return row is not None