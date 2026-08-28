# import matplotlib.pyplot as plt

import hobbybeheer, persoonsbeheer

def koppel_hobby_aan_persoon(verbinding):
    '''Interactieve functie om een hobby aan een persoon te koppelen'''
    naam = input('Voer naam in: ')
    if not persoonsbeheer.persoon_aanwezig_in_database(verbinding, naam):
        print('Persoon niet gevonden in database.')
        return
    print('Kies een van de volgende hobby\'s:')
    hobbybeheer.print_hobbys(verbinding)
    hobby = input('Voer hobby in: ')
    volgorde = int(input('Welk volgnummer heeft deze hobby voor deze persoon? '))
    if not hobbybeheer.hobby_aanwezig_in_database(verbinding, hobby):
        print('Hobby niet gevonden in database.')
        return
    if persoon_hobby_combinatie_aanwezig_in_database(verbinding, naam, hobby):
        print('Deze persoon is al aan deze hobby gekoppeld.')
        return
    if volgorde_aanwezig_in_database(verbinding, naam, volgorde):
        print('Deze persoon heeft al een hobby met deze volgorde.')
        return
    koppel_hobby_aan_persoon_in_database(verbinding, naam, hobby, volgorde)


def print_personenlijst_met_hobbys(verbinding):
    '''Functie om personenlijst uit database te printen'''
    rijen = haal_personenlijst_met_hobbys_op_uit_database(verbinding)
    for rij in rijen:
        naam = rij[0]
        afstand = rij[1]
        print(naam + ' - ' + str(afstand) + 'km - ', end='')
        hobby = rij[2]
        if hobby is None:
            print('Geen hobby\'s')
        else:
            if rij[3] == 1:
                individuele_hobby = 'Individueel'
            else:
                individuele_hobby = 'Niet individueel'
            omschrijving = rij[4]
            print(hobby + ' - ' + individuele_hobby + ' - ' + omschrijving)


def haal_personenlijst_met_hobbys_op_uit_database(verbinding):
    '''Haalt personen met gekoppelde hobby-informatie op.'''
    cursor = verbinding.cursor()
    cursor.execute('''SELECT persoon.naam, afstand, hobby.naam, hobby.individuele_hobby,
               hobby.omschrijving
               FROM persoon
               JOIN persoon_hobby ON persoon.naam = persoon_hobby.persoon_naam
               JOIN hobby ON persoon_hobby.hobby_naam = hobby.naam
               ORDER BY persoon.naam''')
    return cursor.fetchall()

def print_personen_met_hobby(verbinding, hobby):
    '''Geeft een lijst van personen per hobby.'''
    rijen = haal_personen_per_hobby_op_uit_database(verbinding, hobby)
    if len(rijen) == 0:
        print('Geen personen gevonden voor deze hobby.')
    else:
        for rij in rijen:
            print(' - ' + rij['persoon_naam'])


def haal_personen_per_hobby_op_uit_database(verbinding, hobby):
    '''Haalt alle personen op voor een specifieke hobby.'''
    cursor = verbinding.cursor()
    cursor.execute('SELECT persoon_naam FROM persoon_hobby WHERE hobby_naam = ?', (hobby,))
    return cursor.fetchall()

def print_personen_per_hobby(verbinding):
    '''Print personen per hobby'''
    hobbys = hobbybeheer.haal_hobbys_op_uit_database(verbinding)
    for hobby in hobbys:
        print(hobby)
        print_personen_met_hobby(verbinding, hobby)

def koppel_hobby_aan_persoon_in_database(verbinding, naam, hobby, volgorde):
    '''Koppelt een persoon aan een hobby in de database.'''
    cursor = verbinding.cursor()
    cursor.execute('INSERT INTO persoon_hobby VALUES (?, ?, ?)', (naam, hobby, volgorde))


def ontkoppel_hobby_van_persoon(verbinding):
    '''Interactieve functie om een hobby te ontkoppelen van een persoon'''
    naam = input(
        'Voer naam in van de persoon waarvan u een hobby wil verwijderen: ')
    hobby = input(
        'Voer naam in van de hobby die u wil verwijderen voor deze persoon: ')
    if not persoon_hobby_combinatie_aanwezig_in_database(verbinding, naam, hobby):
        print('Combinatie van persoon en hobby niet gevonden in database.')
    else:
        ontkoppel_hobby_van_persoon_in_database(verbinding, naam, hobby)


def ontkoppel_hobby_van_persoon_in_database(verbinding, naam, hobby):
    '''Ontkoppelt een persoon van een hobby in de database.'''
    cursor = verbinding.cursor()
    cursor.execute(
        'DELETE FROM persoon_hobby WHERE persoon_naam = ? and hobby_naam = ?', (naam, hobby))

def persoon_hobby_combinatie_aanwezig_in_database(verbinding, naam, hobby):
    '''Controleert of de combinatie van persoon en hobby in de database staat.'''
    cursor = verbinding.cursor()
    cursor.execute(
        'SELECT persoon_naam FROM persoon_hobby WHERE persoon_naam = ? and hobby_naam = ?',
        (naam, hobby))
    row = cursor.fetchone()
    return row is not None

def volgorde_aanwezig_in_database(verbinding, naam, volgorde):
    '''Controleert of de combinatie van persoon en volgorde in de database staat.'''
    cursor = verbinding.cursor()
    cursor.execute(
        'SELECT persoon_naam FROM persoon_hobby WHERE persoon_naam = ? and volgorde = ?',
        (naam, volgorde))
    row = cursor.fetchone()
    return row is not None

def print_aantal_personen_per_hobby(verbinding):
    '''Geeft een lijst met het aantal personen per hobby.'''
    rijen = haal_aantal_personen_per_hobby_op_uit_database(verbinding)
    for hobby, aantal in rijen:
        print(hobby + ': ' + str(aantal))


def haal_aantal_personen_per_hobby_op_uit_database(verbinding):
    '''Haalt het aantal personen per hobby op.'''
    cursor = verbinding.cursor()
    cursor.execute('''SELECT hobby_naam, COUNT(persoon_naam) AS aantal_personen
                    FROM persoon_hobby
                    GROUP BY hobby_naam
                    ORDER BY aantal_personen DESC;''')
    return cursor.fetchall()

def haal_favoriete_hobby_aantallen_op_uit_database(verbinding):
    '''Haalt het aantal personen per favoriete hobby op.'''
    cursor = verbinding.cursor()
    pass


def verwijder_alle_koppelingen_uit_database(verbinding):
    '''Verwijdert alle koppelingen tussen personen en hobby's uit de database.'''
    cursor = verbinding.cursor()
    cursor.execute('DELETE FROM persoon_hobby')

def toon_taartdiagram_van_favoriete_hobbys(verbinding):
    '''Functie om data uit database te halen en als taartdiagram te tonen'''
    rijen = haal_favoriete_hobby_aantallen_op_uit_database(verbinding)
    pass
