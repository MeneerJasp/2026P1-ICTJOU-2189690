'''Startpunt van Klaskompas'''
import sqlite3

import persoonhobbybeheer
import persoonsbeheer
import hobbybeheer


def haal_databaseverbinding_op():
    '''Maakt een verbinding met de database.'''
    verbinding = sqlite3.connect('db/klaskompas.db')
    verbinding.row_factory = sqlite3.Row
    verbinding.execute('PRAGMA foreign_keys = ON')
    verbinding.autocommit = True
    return verbinding


def main():
    '''Startpunt van de applicatie'''
    verbinding = haal_databaseverbinding_op()
    while True:
        print('Menu:')
        print('1. Vul database met data uit CSV-bestanden (personen en hobby\'s)')
        print('2. Voeg een hobby toe')
        print('3. Koppel een hobby aan een persoon')
        print('4. Ontkoppel hobby voor persoon')
        print('5. Werk afstand bij voor persoon')
        print('6. Toon grafiek met afstand per persoon')
        print('7. Toon taartdiagram met favoriete hobby\'s per persoon')
        print('8. Print hobby\'s met aantal personen')
        print('9. Print personen per hobby')
        print('10. Print personenlijst met hobby\'s per persoon')
        print('11. Maak groepjes op basis van afstanden')
        print('12. Leeg database (alle data verwijderen)')
        print('x. Stop')

        keuze = input('Kies een optie: ')
        
        if keuze == '1':
            vul_database_uit_csvbestand(verbinding)
        elif keuze == '2':
            hobbybeheer.voeg_hobby_toe(verbinding)
        elif keuze == '3':
            persoonhobbybeheer.koppel_hobby_aan_persoon(verbinding)
        elif keuze == '4':
            persoonhobbybeheer.ontkoppel_hobby_van_persoon(verbinding)
        elif keuze == '5':
            persoonsbeheer.werk_afstand_bij_voor_persoon(verbinding)
        elif keuze == '6':
            persoonsbeheer.toon_grafiek_met_afstand_per_persoon(verbinding)
        elif keuze == '7':
            persoonhobbybeheer.toon_taartdiagram_van_favoriete_hobbys(verbinding)
        elif keuze == '8':
                persoonhobbybeheer.print_aantal_personen_per_hobby(verbinding)
        elif keuze == '9':
                persoonhobbybeheer.print_personen_per_hobby(verbinding)
        elif keuze == '10':
                persoonhobbybeheer.print_personenlijst_met_hobbys(verbinding)
        elif keuze == '11':
                maak_groepjes_op_basis_van_afstanden(verbinding)
        elif keuze == '12':
                # let op: volgorde is belangrijk vanwege de foreign key constraints
                persoonhobbybeheer.verwijder_alle_koppelingen_uit_database(verbinding)
                hobbybeheer.verwijder_alle_hobbys_uit_database(verbinding)
                persoonsbeheer.verwijder_alle_personen_uit_database(verbinding)
        elif keuze == 'x':
            break
        else:
            print('Ongeldige keuze. Probeer opnieuw.')



def maak_groepjes_op_basis_van_afstanden(verbinding):
    '''Interactieve functie om groepjes te maken op basis van afstanden'''
    aantal_groepjes = input('Voer het aantal groepjes in: ')
    aantal_groepjes = int(aantal_groepjes)
    if aantal_groepjes <= 0:
        print('Ongeldige invoer. Aantal groepjes moet groter zijn dan 0.')
    else:
        persoonsbeheer.maak_groepjes_op_basis_van_afstanden(
            verbinding, aantal_groepjes)

def vul_database_uit_csvbestand(verbinding):
    '''Vul de database met data uit CSV-bestanden'''
    persoonsbeheer.importeer_personen(verbinding)
    hobbybeheer.importeer_hobbys(verbinding)

if __name__ == '__main__':
    main()
