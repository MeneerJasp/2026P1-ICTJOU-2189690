import sqlite3


def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect("platenbak.db")
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



def haal_tracks_op_all():
    verbinding = sqlite3.connect("platenbak.db")
    cursor = verbinding.cursor()
    
    cursor.execute("""
    SELECT artiest, titel, genre, duur, jaar FROM track
    """)

    tracks = cursor.fetchall()
    verbinding.close()
    return tracks

def toon_tracks_all():
    tracks = haal_tracks_op_all()
    if len(tracks) == 0 :
        print("Er zijn geen tracks gevonden")
    else:
        for track in tracks:
            print_track(track)

def print_tracka(track):
    print("Artiest:", track[0])
    print("Titel:", track[1])
    print("Genre:", track[2])
    print("Duur:", track[3], "seconden")
    print("###########################")

def toon_tracks_artiest(artiest):
    tracks = haal_tracks_artiest_op(artiest)

    if len(tracks) == 0:
        print("Er zijn geen tracks van deze artiest gevonden")
    else:
        for track in tracks:
            print_track(track)

def haal_tracks_artiest_op(artiest):
    verbinding = sqlite3.connect("platenbak.db")
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT artiest, titel, genre, duur, jaar
    FROM track WHERE artiest = ?
    """, (artiest))
    tracks = cursor.fetchall()
    verbinding.close()
    return tracks

def bestaat_artiest(artiest):
    verbinding = sqlite3.connect("platenbak.db")
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT naam FROM artiest WHERE naam = ?
    """, (artiest,))
    resultaat = cursor.fetchall()
    verbinding.close()
    return resultatt is not None

def bestaat_genre(genre):
    verbinding = sqlite3.connect("platenbak.db")
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT naam FROM genre WHERE naam = ?
    """, (genre,))
    resultaat = cursor.fetchall()
    verbinding.close()
    return resultaat is not none


def start_platenbak():
    """Start de interactieve hoofdloop van de platenbak."""
    verbinding = maak_verbinding()

    print("Welkom bij de Platenbak! Veel plezier met je collectie.")

    verbinding.close()

if __name__ == '__main__':
    start_platenbak()