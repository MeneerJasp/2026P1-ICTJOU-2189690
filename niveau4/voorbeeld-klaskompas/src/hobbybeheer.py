'''Functies voor het beheren van hobby's.'''

import csv

csvbestand_hobbys = 'data/hobbys.csv'

def importeer_hobbys(verbinding):
    '''Functie om hobby-data uit CSV-bestand te lezen'''
    with open(csvbestand_hobbys, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for rij in csv_reader:
            voeg_hobby_toe_aan_database(
                verbinding, rij['naam'], rij['individuele_hobby'], rij['omschrijving'])


def haal_hobbys_op_uit_database(verbinding):
    '''Haal alle hobby's op uit de database.'''
    cursor = verbinding.cursor()
    cursor.execute('SELECT naam FROM hobby')
    rijen = cursor.fetchall()
    return [rij['naam'] for rij in rijen]

def voeg_hobby_toe(verbinding):
    '''Interactieve functie om een hobby toe te voegen aan de database'''
    naam = input('Voer naam in van de hobby: ')
    individuele_hobby = input(
        'Is dit een individuele hobby? (ja/nee): ')
    omschrijving = input('Voer een omschrijving in van de hobby: ')
    if individuele_hobby.lower() == 'ja':
        individuele_hobby = True
    else:
        individuele_hobby = False
    voeg_hobby_toe_aan_database(verbinding, naam, individuele_hobby, omschrijving)

def voeg_hobby_toe_aan_database(verbinding, naam, individuele_hobby, omschrijving):
    '''Voegt een hobby toe aan de database.'''
    cursor = verbinding.cursor()
    cursor.execute('INSERT INTO hobby VALUES (?, ?, ?)',
                   (naam, individuele_hobby, omschrijving))


def print_hobbys(verbinding):
    '''Geeft een lijst van alle hobby's in de database.'''
    rijen = haal_hobby_overzicht_op_uit_database(verbinding)
    for rij in rijen:
        if rij['individuele_hobby'] == 1:
            individuele_hobby = 'Individueel'
        else:
            individuele_hobby = 'Niet individueel'
        print(rij['naam'] + ' - ' + individuele_hobby + ' - ' + rij['omschrijving'])


def haal_hobby_overzicht_op_uit_database(verbinding):
    '''Haalt naam, type en omschrijving op voor alle hobby's.'''
    cursor = verbinding.cursor()
    cursor.execute('SELECT naam, individuele_hobby, omschrijving FROM hobby')
    return cursor.fetchall()


def hobby_aanwezig_in_database(verbinding, hobby):
    '''Controleert of de hobby in de database staat.'''
    cursor = verbinding.cursor()
    cursor.execute('SELECT naam FROM hobby WHERE naam = ?', (hobby,))
    row = cursor.fetchone()
    return row is not None

def verwijder_alle_hobbys_uit_database(verbinding):
    '''Verwijdert alle hobby's uit de database'''
    cursor = verbinding.cursor()
    cursor.execute('DELETE FROM hobby')
