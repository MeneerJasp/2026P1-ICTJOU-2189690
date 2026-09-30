import random
import sqlite3
 

DATABASE = "niveau2/oefen-elftalbeheer/db/elftalbeheer.db"

aantal_elftallen_toegevoegd = 0
aantal_spelers_toegevoegd = 0
aantal_spelers_verwijderd = 0


def maak_verbinding():
    verbinding = sqlite3.connect(DATABASE)
    verbinding.execute("PRAGMA foreign_keys = ON")
    return verbinding


def toon_menu():
    print("1. Elftal toevoegen")
    print("2. Speler toevoegen")
    print("3. Speler zoeken")
    print("4. Elftallen bekijken")
    print("5. Speler verwijderen")
    print("6. Gemiddelde leeftijd per elftal")
    print("7. Speler van de maand")
    print("0. Afsluiten")


def vraag_keuze():
    keuze = int(input("Maak een keuze: "))
    return keuze


def voeg_elftal_toe():
    global aantal_elftallen_toegevoegd

    elftalcode = input("Elftalcode: ")
    omschrijving = input("Omschrijving: ")
    coach = input("Coach: ")
    maximumleeftijd = int(input("Maximumleeftijd: "))

    verbinding = maak_verbinding()
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT elftalcode
    FROM elftal
    WHERE elftalcode = ?
    """, (elftalcode,))

    bestaand_elftal = cursor.fetchone()

    if bestaand_elftal is not None:
        print("Elftal bestaat al")
    else:
        cursor.execute("""
        INSERT INTO elftal (elftalcode, omschrijving, coach, maximumleeftijd)
        VALUES (?, ?, ?, ?)
        """, (elftalcode, omschrijving, coach, maximumleeftijd))

        verbinding.commit()
        aantal_elftallen_toegevoegd += 1
        print("Elftal is toegevoegd")

    verbinding.close()


def geef_elftalsuggestie(leeftijd):
    verbinding = maak_verbinding()
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT elftalcode, maximumleeftijd
    FROM elftal
    ORDER BY maximumleeftijd, elftalcode
    """)

    elftallen = cursor.fetchall()
    verbinding.close()

    teller = 0
    suggestie = None

    while teller < len(elftallen) and suggestie is None:
        if leeftijd <= elftallen[teller][1]:
            suggestie = elftallen[teller][0]

        teller += 1

    if suggestie is None:
        print("Geen passend elftal gevonden")
    else:
        print("Voorgesteld elftal:", suggestie)


def voeg_speler_toe():
    global aantal_spelers_toegevoegd

    naam = input("Naam: ")
    leeftijd = int(input("Leeftijd: "))

    geef_elftalsuggestie(leeftijd)

    elftal = input("Elftalcode: ")
    positie = input("Positie: ")

    verbinding = maak_verbinding()
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT maximumleeftijd
    FROM elftal
    WHERE elftalcode = ?
    """, (elftal,))

    resultaat = cursor.fetchone()

    if resultaat is None:
        print("Elftal bestaat niet")

    elif leeftijd > resultaat[0]:
        print("Speler is te oud voor dit elftal")

    else:
        cursor.execute("""
        INSERT INTO speler (naam, elftal, positie, leeftijd)
        VALUES (?, ?, ?, ?)
        """, (naam, elftal, positie, leeftijd))

        verbinding.commit()
        aantal_spelers_toegevoegd += 1

        print("Speler is toegevoegd")

    verbinding.close()


def zoek_speler():
    naam = input("Naam speler: ")

    verbinding = maak_verbinding()
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT naam, elftal, positie, leeftijd
    FROM speler
    WHERE naam LIKE ?
    """, ("%" + naam + "%",))

    spelers = cursor.fetchall()
    verbinding.close()

    if len(spelers) == 0:
        print("Geen spelers gevonden")
    else:
        for speler in spelers:
            print(speler)


def toon_elftallen():
    verbinding = maak_verbinding()
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT elftal.elftalcode,
           elftal.omschrijving,
           speler.naam
    FROM elftal
    LEFT JOIN speler
    ON elftal.elftalcode = speler.elftal
    """)

    resultaten = cursor.fetchall()
    verbinding.close()

    for resultaat in resultaten:
        print(resultaat)


def verwijder_speler():
    global aantal_spelers_verwijderd

    naam = input("Naam speler: ")

    verbinding = maak_verbinding()
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT naam
    FROM speler
    WHERE naam = ?
    """, (naam,))

    speler = cursor.fetchone()

    if speler is None:
        print("Speler niet gevonden")

    else:
        cursor.execute("""
        DELETE FROM speler
        WHERE naam = ?
        """, (naam,))

        verbinding.commit()
        aantal_spelers_verwijderd += 1

        print("Speler is verwijderd")

    verbinding.close()


def toon_gemiddelde_leeftijd_per_elftal():
    verbinding = maak_verbinding()
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT elftal.elftalcode,
           AVG(speler.leeftijd)
    FROM elftal
    LEFT JOIN speler
    ON elftal.elftalcode = speler.elftal
    GROUP BY elftal.elftalcode
    """)

    resultaten = cursor.fetchall()
    verbinding.close()

    for resultaat in resultaten:
        if resultaat[1] is None:
            print(resultaat[0], "Geen spelers")
        else:
            print(resultaat[0], round(resultaat[1], 1))


def kies_speler_van_de_maand():
    verbinding = maak_verbinding()
    cursor = verbinding.cursor()

    cursor.execute("""
    SELECT naam, elftal
    FROM speler
    """)

    spelers = cursor.fetchall()
    verbinding.close()

    if len(spelers) == 0:
        print("Er zijn geen spelers om uit te kiezen")
    else:
        speler = random.choice(spelers)
        print("Speler van de maand:", speler[0], "-", speler[1])


def toon_sessiestatistieken():
    print("Elftallen toegevoegd:", aantal_elftallen_toegevoegd)
    print("Spelers toegevoegd:", aantal_spelers_toegevoegd)
    print("Spelers verwijderd:", aantal_spelers_verwijderd)


def start_elftalbeheer():
    keuze = -1

    while keuze != 0:
        toon_menu()
        keuze = vraag_keuze()

        if keuze == 1:
            voeg_elftal_toe()

        elif keuze == 2:
            voeg_speler_toe()

        elif keuze == 3:
            zoek_speler()

        elif keuze == 4:
            toon_elftallen()

        elif keuze == 5:
            verwijder_speler()

        elif keuze == 6:
            toon_gemiddelde_leeftijd_per_elftal()

        elif keuze == 7:
            kies_speler_van_de_maand()

        elif keuze == 0:
            toon_sessiestatistieken()
            print("Programma afgesloten")

        else:
            print("Keuze is ongeldig")


if __name__ == '__main__':
    start_elftalbeheer()