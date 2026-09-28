import sqlite3


DATABASE = "niveau2/voorbeeld-platenbak/db/platenbak.db"


def maak_verbinding():
    verbinding = sqlite3.connect(DATABASE)
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding


def toon_menu():
    print("1. Track toevoegen")
    print("2. Tracks bekijken")
    print("3. Tracks zoeken")
    print("4. Artiest toevoegen")
    print("0. Afsluiten")


def vraag_keuze():
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
    cursor = verbinding.cursor()

    cursor.execute("""
    INSERT INTO track (artiest, titel, genre, duur, jaar)
    VALUES (?, ?, ?, ?, ?)
    """, (artiest, titel, genre, duur, jaar))

    print(f"{titel} is toegevoegd")


def voeg_track_toe(verbinding):
    artiest = input("Artiest: ")
    titel = input("Titel: ")
    genre = input("Genre: ")
    duur = input("Duur: ")
    jaar = input("Jaar: ")

    if bestaat_artiest(artiest) and bestaat_genre(genre):
        voeg_track_toe_aan_database(
            verbinding,
            artiest,
            titel,
            duur,
            jaar,
            genre
        )
    else:
        print("Artiest of genre bestaat niet")


def haal_tracks_op_all():
    verbinding = sqlite3.connect(DATABASE)
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT artiest, titel, genre, duur, jaar
    FROM track
    """)

    tracks = cursor.fetchall()
    verbinding.close()
    return tracks


def toon_tracks_all():
    tracks = haal_tracks_op_all()

    if len(tracks) == 0:
        print("Er zijn geen tracks gevonden")
    else:
        for track in tracks:
            print_tracks(track)


def print_tracks(track):
    print("Artiest:", track[0])
    print("Titel:", track[1])
    print("Genre:", track[2])
    print("Duur:", track[3], "seconden")
    print("Jaar:", track[4])
    print("###########################")


def toon_tracks_artiest(artiest):
    tracks = haal_tracks_artiest_op(artiest)

    if len(tracks) == 0:
        print("Er zijn geen tracks van deze artiest gevonden")
    else:
        for track in tracks:
            print_tracks(track)


def haal_tracks_artiest_op(artiest):
    verbinding = sqlite3.connect(DATABASE)
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT artiest, titel, genre, duur, jaar
    FROM track
    WHERE artiest = ?
    """, (artiest,))

    tracks = cursor.fetchall()
    verbinding.close()
    return tracks


def bestaat_artiest(artiest):
    verbinding = sqlite3.connect(DATABASE)
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT naam
    FROM artiest
    WHERE naam = ?
    """, (artiest,))

    resultaat = cursor.fetchone()
    verbinding.close()

    return resultaat is not None


def bestaat_genre(genre):
    verbinding = sqlite3.connect(DATABASE)
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT naam
    FROM genre
    WHERE naam = ?
    """, (genre,))

    resultaat = cursor.fetchone()
    verbinding.close()

    return resultaat is not None


def zoek_tracks():
    jaar = input("Vanaf welk jaar: ")
    genre = input("Genre: ")

    verbinding = sqlite3.connect(DATABASE)
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT artiest, titel, genre, duur, jaar
    FROM track
    WHERE jaar >= ? AND genre = ?
    """, (jaar, genre))

    tracks = cursor.fetchall()
    verbinding.close()

    if len(tracks) == 0:
        print("Er zijn geen tracks gevonden")
    else:
        for track in tracks:
            print_tracks(track)


def voeg_artiest_toe():
    naam = input("Naam artiest: ")
    land = input("Land: ")

    verbinding = sqlite3.connect(DATABASE)
    cursor = verbinding.cursor()

    cursor.execute("""
    INSERT INTO artiest (naam, land)
    VALUES (?, ?)
    """, (naam, land))

    verbinding.commit()
    verbinding.close()

    print(f"{naam} is toegevoegd")


def start_platenbak():
    verbinding = maak_verbinding()

    print("Welkom bij de Platenbak! Veel plezier met je collectie.")

    keuze = -1

    while keuze != 0:
        toon_menu()
        keuze = vraag_keuze()

        if keuze == 1:
            voeg_track_toe(verbinding)

        elif keuze == 2:
            toon_tracks_all()

        elif keuze == 3:
            zoek_tracks()

        elif keuze == 4:
            voeg_artiest_toe()
        
        elif keuze == 0:
            quit()

        else:
            print("Keuze is ongeldig")
            start_platenbak()

    verbinding.close()


if __name__ == '__main__':
    start_platenbak()
