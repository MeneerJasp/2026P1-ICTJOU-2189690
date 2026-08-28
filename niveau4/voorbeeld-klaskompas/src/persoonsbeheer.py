'''Functies voor het beheren van personen.'''

# import matplotlib.pyplot as plt

import csv


def importeer_personen(verbinding):
    '''Functie om personen-data uit CSV-bestand te lezen'''
    with open('data/personen.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for rij in csv_reader:
            afstand = float(rij['afstand'])
            voeg_persoon_toe_aan_database(verbinding, rij['naam'], afstand)            


def persoon_aanwezig_in_database(verbinding, naam):
    '''Functie om  te controleren of persoon in de database bestaat'''
    cursor = verbinding.cursor()
    cursor.execute('SELECT naam FROM persoon WHERE naam = ?', (naam,))
    row = cursor.fetchone()
    return row is not None


def voeg_persoon_toe_aan_database(verbinding, naam, afstand):
    '''Functie om persoonsdata (naam, afstand) in SQLite-database op te slaan'''
    if persoon_aanwezig_in_database(verbinding, naam):
        print('Persoon ' + naam + ' bestaat al in database.')
    else:
        cursor = verbinding.cursor()
        cursor.execute('INSERT INTO persoon VALUES (?, ?)', (naam, afstand))
        print('Persoon ' + naam + ' toegevoegd aan database.')


def wijzig_afstand_in_database(verbinding, naam, nieuwe_afstand):
    '''Wijzigt afstand en geeft status terug voor foutafhandeling in de UI-laag.'''
    cursor = verbinding.cursor()
    cursor.execute('UPDATE persoon SET afstand = ? WHERE naam = ?',
                   (nieuwe_afstand, naam))


def verwijder_alle_personen_uit_database(verbinding):
    '''Functie om personentabel in database te legen'''
    cursor = verbinding.cursor()
    cursor.execute('DELETE FROM persoon')


def maak_groepjes_op_basis_van_afstanden(verbinding, aantal_groepjes):
    '''Functie om groepjes te maken op basis van afstand, de personen die
    ongeveer even ver van school wonen, worden in dezelfde groep geplaatst.'''
    pass


def haal_personen_op_volgorde_van_afstand_uit_database(verbinding):
    '''Haalt personen op, gesorteerd op afstand.'''
    cursor = verbinding.cursor()
    cursor.execute('SELECT naam, afstand FROM persoon ORDER BY afstand')
    return cursor.fetchall()


def haal_afstanden_per_persoon_op_uit_database(verbinding):
    '''Haalt naam en afstand op voor alle personen.'''
    cursor = verbinding.cursor()
    cursor.execute('SELECT naam, afstand FROM persoon')
    return cursor.fetchall()


def toon_grafiek_van_afstanden_als_afbeelding(verbinding):
    '''Functie om data uit database te halen en als staafdiagram te tonen'''
    pass


def toon_grafiek_van_afstanden_als_ascii(verbinding, maximale_staaflengte, karakter):
    '''Functie om data uit database te halen en als staafdiagram te tonen met ASCII-art'''
    pass
        
def werk_afstand_bij_voor_persoon(verbinding):
    '''Interactieve functie om afstand bij te werken voor een persoon'''
    naam = input('Voer naam in van de persoon die u wilt bijwerken: ')
    nieuwe_afstand = input('Voer nieuwe afstand in: ')
    nieuwe_afstand = float(nieuwe_afstand)
    wijzig_afstand_in_database(verbinding, naam, nieuwe_afstand)


def toon_grafiek_met_afstand_per_persoon(verbinding):
    '''Interactieve functie om een grafiek te tonen met afstanden per persoon'''
    pass