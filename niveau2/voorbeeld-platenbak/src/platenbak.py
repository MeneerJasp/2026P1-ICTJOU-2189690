import sqlite3


DATABASE = "niveau2/voorbeeld-platenbak/db/platenbak.db"


def maak_verbinding():
    verbinding = sqlite3.connect(DATABASE)

    # Rij ook met kolomnaam kunnen gebruiken, bijvoorbeeld rij["naam"].
    verbinding.row_factory = sqlite3.Row

    # Foreign keys aanzetten.
    # SQLite controleert dan of gekoppelde gegevens bestaan.
    verbinding.execute("PRAGMA foreign_keys = ON")

    # Wijzigingen meteen opslaan.
    verbinding.autocommit = True

    return verbinding


def toon_menu():
    print("1. Track toevoegen")
    print("2. Tracks bekijken")
    print("3. Tracks zoeken")
    print("4. Artiest toevoegen")
    print("5. Statistieken bekijken")
    print("6. Artiesten per land bekijken")
    print("7. Genreoverzicht bekijken")
    print("8. Sessiestatistieken bekijken")
    print("9. Genre toevoegen")
    print("10. Genre verwijderen")
    print("11. Track verwijderen")
    print("12. Playlist samenstellen")
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

    # Tip: ? zijn placeholders.
    # Waardes worden apart en op dezelfde volgorde meegegeven.

    print(f"{titel} is toegevoegd")


def voeg_track_toe(verbinding):
    artiest = input("Artiest: ")
    titel = input("Titel: ")
    genre = input("Genre: ")
    duur = input("Duur: ")
    jaar = input("Jaar: ")

    # Alleen toevoegen als artiest en genre bestaan.
    if bestaat_artiest(artiest) and bestaat_genre(genre):

        voeg_track_toe_aan_database(
            verbinding,
            artiest,
            titel,
            duur,
            jaar,
            genre
        )

        return True

    else:
        print("Artiest of genre bestaat niet")
        return False


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
    # 1 track tonen.
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

    # Tip: bij 1 waarde staat er een komma in (artiest,).
    # Zo weet Python dat dit een tuple is.

    tracks = cursor.fetchall()

    verbinding.close()

    return tracks


def bestaat_artiest(artiest):
    verbinding = sqlite3.connect(DATABASE)
    cursor = verbinding.cursor()

    # Kijken of artiest bestaat.
    cursor.execute("""
    SELECT naam
    FROM artiest
    WHERE naam = ?
    """, (artiest,))

    resultaat = cursor.fetchone()

    verbinding.close()

    # True als iets gevonden is, anders False.
    return resultaat is not None


def bestaat_genre(genre):
    verbinding = sqlite3.connect(DATABASE)
    cursor = verbinding.cursor()

    # Kijken of genre bestaat.
    cursor.execute("""
    SELECT naam
    FROM genre
    WHERE naam = ?
    """, (genre,))

    resultaat = cursor.fetchone()

    verbinding.close()

    return resultaat is not None


def track_bestaat_in_database(verbinding, artiest, titel):
    cursor = verbinding.cursor()

    # Track zoeken op artiest + titel.
    cursor.execute("""
    SELECT titel
    FROM track
    WHERE artiest = ? AND titel = ?
    """, (artiest, titel))

    resultaat = cursor.fetchone()

    return resultaat is not None


def verwijder_track_uit_database(verbinding, artiest, titel):
    cursor = verbinding.cursor()

    cursor.execute("""
    DELETE FROM track
    WHERE artiest = ? AND titel = ?
    """, (artiest, titel))


def verwijder_track(verbinding):
    artiest = input("Artiest: ")
    titel = input("Titel: ")

    # Eerst controleren of de track bestaat.
    if track_bestaat_in_database(verbinding, artiest, titel):

        verwijder_track_uit_database(verbinding, artiest, titel)

        print(f"{titel} is verwijderd")

        return True

    else:
        print("Track bestaat niet")
        return False


def toon_track_info(track):
    print_tracks(track)


def stel_playlist_samen(verbinding):
    minuten = int(input("Gewenste tijd in minuten: "))

    if minuten <= 0:
        print("Tijd moet groter zijn dan 0")
        return

    # Minuten naar seconden.
    gewenste_duur = minuten * 60

    cursor = verbinding.cursor()

    # Tracks in willekeurige volgorde ophalen.
    cursor.execute("""
    SELECT artiest, titel, genre, duur, jaar
    FROM track
    ORDER BY RANDOM()
    """)

    tracks = cursor.fetchall()

    totale_duur = 0

    # Stoppen zodra de gewenste duur bereikt is.
    for track in tracks:

        if totale_duur >= gewenste_duur:
            break

        toon_track_info(track)

        totale_duur += track[3]

    print("Totale duur playlist:", totale_duur, "seconden")


def zoek_tracks_op_criteria_uit_database(verbinding, genre, jaar_min):
    cursor = verbinding.cursor()

    # Filteren op minimaal jaar en genre.
    cursor.execute("""
    SELECT artiest, titel, genre, duur, jaar
    FROM track
    WHERE jaar >= ? AND genre = ?
    """, (jaar_min, genre))

    tracks = cursor.fetchall()

    return tracks


def voeg_genre_toe(verbinding):
    naam = input("Naam genre: ")
    omschrijving = input("Omschrijving: ")

    cursor = verbinding.cursor()

    # Eerst kijken of het genre al bestaat.
    cursor.execute("""
    SELECT naam
    FROM genre
    WHERE naam = ?
    """, (naam,))

    if cursor.fetchone() is not None:
        print("Genre bestaat al")

    else:
        cursor.execute("""
        INSERT INTO genre (naam, omschrijving)
        VALUES (?, ?)
        """, (naam, omschrijving))

        print(f"{naam} is toegevoegd")


def verwijder_genre(verbinding):
    naam = input("Naam genre: ")

    cursor = verbinding.cursor()

    # Eerst kijken of het genre bestaat.
    cursor.execute("""
    SELECT naam
    FROM genre
    WHERE naam = ?
    """, (naam,))

    if cursor.fetchone() is None:
        print("Genre bestaat niet")
        return

    # Aantal tracks met dit genre tellen.
    cursor.execute("""
    SELECT COUNT(*)
    FROM track
    WHERE genre = ?
    """, (naam,))

    aantal_tracks = cursor.fetchone()[0]

    if aantal_tracks > 0:
        print("Genre kan niet worden verwijderd omdat er tracks aan gekoppeld zijn")

    else:
        cursor.execute("""
        DELETE FROM genre
        WHERE naam = ?
        """, (naam,))

        print(f"{naam} is verwijderd")


def zoek_tracks(verbinding):
    jaar = input("Vanaf welk jaar: ")
    genre = input("Genre: ")

    tracks = zoek_tracks_op_criteria_uit_database(verbinding, genre, jaar)

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

    # Deze verbinding gebruikt geen autocommit.
    verbinding.commit()

    verbinding.close()

    print(f"{naam} is toegevoegd")


def haal_statistieken_op_uit_database(verbinding):
    cursor = verbinding.cursor()

    # COUNT = aantal, AVG = gemiddelde, SUM = totaal.
    cursor.execute("""
    SELECT COUNT(*), AVG(duur), SUM(duur)
    FROM track
    """)

    statistieken = cursor.fetchone()

    return statistieken


def toon_statistieken(verbinding):
    statistieken = haal_statistieken_op_uit_database(verbinding)

    print("Aantal tracks:", statistieken[0])
    print("Gemiddelde duur:", statistieken[1], "seconden")
    print("Totale duur:", statistieken[2], "seconden")


def haal_landen_op_uit_database(verbinding):
    cursor = verbinding.cursor()

    # Artiesten per land groeperen en tellen.
    cursor.execute("""
    SELECT land, COUNT(*)
    FROM artiest
    GROUP BY land
    """)

    landen = cursor.fetchall()

    return landen


def toon_landen(verbinding):
    landen = haal_landen_op_uit_database(verbinding)

    for land in landen:
        print("Land:", land[0])
        print("Aantal artiesten:", land[1])
        print("###########################")


def haal_genreoverzicht_op_uit_database(verbinding):
    cursor = verbinding.cursor()

    # LEFT JOIN laat ook genres zonder tracks zien.
    # COALESCE maakt een lege totale duur 0.
    cursor.execute("""
    SELECT genre.naam, COUNT(track.titel), COALESCE(SUM(track.duur), 0)
    FROM genre
    LEFT JOIN track
    ON genre.naam = track.genre
    GROUP BY genre.naam
    """)

    genres = cursor.fetchall()

    return genres


def toon_genreoverzicht(verbinding):
    genres = haal_genreoverzicht_op_uit_database(verbinding)

    for genre in genres:
        print("Genre:", genre[0])
        print("Aantal tracks:", genre[1])
        print("Totale duur:", genre[2], "seconden")
        print("###########################")


def toon_sessiestatistieken(aantal_tracks_toegevoegd, aantal_tracks_verwijderd):
    print("Aantal tracks toegevoegd deze sessie:", aantal_tracks_toegevoegd)
    print("Aantal tracks verwijderd deze sessie:", aantal_tracks_verwijderd)


def start_platenbak():
    verbinding = maak_verbinding()

    print("Welkom bij de Platenbak! Veel plezier met je collectie.")

    keuze = -1

    # Tellers beginnen iedere nieuwe sessie op 0.
    aantal_tracks_toegevoegd = 0
    aantal_tracks_verwijderd = 0

    while keuze != 0:

        toon_menu()
        keuze = vraag_keuze()

        if keuze == 1:
            track_toegevoegd = voeg_track_toe(verbinding)

            if track_toegevoegd:
                aantal_tracks_toegevoegd += 1

        elif keuze == 2:
            toon_tracks_all()

        elif keuze == 3:
            zoek_tracks(verbinding)

        elif keuze == 4:
            voeg_artiest_toe()

        elif keuze == 5:
            toon_statistieken(verbinding)

        elif keuze == 6:
            toon_landen(verbinding)

        elif keuze == 7:
            toon_genreoverzicht(verbinding)

        elif keuze == 8:
            toon_sessiestatistieken(
                aantal_tracks_toegevoegd,
                aantal_tracks_verwijderd
            )

        elif keuze == 9:
            voeg_genre_toe(verbinding)

        elif keuze == 10:
            verwijder_genre(verbinding)

        elif keuze == 11:
            track_verwijderd = verwijder_track(verbinding)

            if track_verwijderd:
                aantal_tracks_verwijderd += 1

        elif keuze == 12:
            stel_playlist_samen(verbinding)

        elif keuze == 0:
            toon_sessiestatistieken(
                aantal_tracks_toegevoegd,
                aantal_tracks_verwijderd
            )

            print("Programma afgesloten")

        else:
            print("Keuze is ongeldig")
            start_platenbak()

    verbinding.close()


# Alleen automatisch starten als dit bestand zelf wordt uitgevoerd.
if __name__ == '__main__':
    start_platenbak()