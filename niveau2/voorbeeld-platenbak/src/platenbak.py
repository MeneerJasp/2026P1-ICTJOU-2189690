import sqlite3


def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect("db/platenbak.db")
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding


def toon_menu():
    """Geeft het menu van de platenbak"""
    print("1. Track toevoegen")


def vraag_keuze():
    """Vraagt gebruiker om een keuze"""
    keuze = int(input("Maak een keuze: "))
    return keuze

def voeg_track_toe_aan_database(
    verbinding,
    artiest,
    titel,
    duur,
    jaar,
    genre
):
    """Voegt een track toe aan de database"""
    pass

def voeg_track_toe(verbinding):
    """Vraagt de track gegevens om toe te voegen aan de database"""
    artiest = input("Artiest: ")
    titel = input("Titel: ")
    duur = input("Duur: ")
    jaar = input("Jaar: ")


def start_platenbak():
    """Start de interactieve hoofdloop van de platenbak."""
    verbinding = maak_verbinding()

    print("Welkom bij de Platenbak! Veel plezier met je collectie.")

    verbinding.close()


if __name__ == '__main__':
    start_platenbak()