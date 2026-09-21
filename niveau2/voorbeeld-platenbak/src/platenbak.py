import sqlite3


def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect("db/platenbak.db")
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding


def voeg_track_toe_aan_database(
    verbinding,
    artiest,
    titel,
    duur,
    jaar,
    genre
):
    """Voegt een track toe aan de database."""
    pass


def toon_menu():
    """Toont het hoofdmenu van de Platenbak."""
    print()
    print("   Platenbak")
    print("1. Track toevoegen")


def vraag_keuze():
    """Vraagt de gebruiker om een menukeuze en retourneert deze als getal."""
    keuze = int(input("Maak een keuze: "))
    return keuze


def voeg_track_toe(verbinding):
    """Vraagt trackgegevens en geeft deze door aan de databasefunctie."""
    artiest = input("Artiest: ")
    titel = input("Titel: ")
    duur = input("Duur: ")
    jaar = input("Jaar: ")
    genre = input("Genre: ")

    voeg_track_toe_aan_database(
        verbinding,
        artiest,
        titel,
        duur,
        jaar,
        genre
    )


def start_platenbak():
    """Start de interactieve hoofdloop van de Platenbak."""
    verbinding = maak_verbinding()

    print("Welkom bij de Platenbak! Veel plezier met je collectie.")

    toon_menu()
    keuze = vraag_keuze()

    if keuze == 1:
        voeg_track_toe(verbinding)

    verbinding.close()


if __name__ == '__main__':
    start_platenbak()