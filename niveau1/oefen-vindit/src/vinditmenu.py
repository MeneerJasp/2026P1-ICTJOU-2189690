import sqlite3


connection = sqlite3.connect(
    "niveau1/oefen-vindit/db/vindit.db"
)

cursor = connection.cursor()

keuze = ""


while keuze.upper() != "X":

    print()
    print("=== VIND IT! VERKOOPMANAGER ===")
    print("1. Toon alle verkopen")
    print("2. Toon alle kleding-verkopen")
    print("3. Toon alle boeken-verkopen")
    print("4. Toon alle overige verkopen")
    print("5. Nieuwe verkoop toevoegen")
    print("6. Totale opbrengst tonen")
    print("7. Toon alle gebruikte categorieen")
    print("8. Totale opbrengst van een maand tonen")
    print("X. Afsluiten")

    keuze = input("Maak je keuze: ")

    print("Je hebt gekozen voor:", keuze)
    print()


    # X. Afsluiten
    if keuze.upper() == "X":

        print("Dag!")

        connection.close()

        quit()


    # 1. Alle verkopen tonen
    elif keuze == "1":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            """
        )

        verkopen = cursor.fetchall()

        for verkoop in verkopen:
            print(verkoop)


    # 2. Kleding-verkopen tonen
    elif keuze == "2":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            WHERE categorie = 'kleding'
            """
        )

        verkopen = cursor.fetchall()

        for verkoop in verkopen:
            print(verkoop)


    # 3. Boeken-verkopen tonen
    elif keuze == "3":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            WHERE categorie = 'boeken'
            """
        )

        verkopen = cursor.fetchall()

        for verkoop in verkopen:
            print(verkoop)


    # 4. Overige verkopen tonen
    elif keuze == "4":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            WHERE categorie != 'kleding'
            AND categorie != 'boeken'
            """
        )

        verkopen = cursor.fetchall()

        for verkoop in verkopen:
            print(verkoop)


    # 5. Nieuwe verkoop toevoegen
    elif keuze == "5":

        verkoopmoment = input(
            "Voer het verkoopmoment in (bijvoorbeeld 2026-09-17 10:30:00): "
        )

        categorie = input(
            "Voer de categorie in: "
        )

        opbrengst = input(
            "Voer de opbrengst in: "
        )

        cursor.execute(
            """
            INSERT INTO Verkoop
            (verkoopmoment, categorie, opbrengst)
            VALUES (?, ?, ?)
            """,
            (
                verkoopmoment,
                categorie,
                opbrengst
            )
        )

        connection.commit()

        print("Verkoop is toegevoegd.")


    # 6. Totale opbrengst tonen
    elif keuze == "6":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            """
        )

        verkopen = cursor.fetchall()

        totale_opbrengst = 0

        for verkoop in verkopen:

            opbrengst = float(verkoop[2])

            totale_opbrengst = (
                totale_opbrengst + opbrengst
            )

        print(
            "Totale opbrengst:",
            totale_opbrengst,
            "euro"
        )


    # 7. Alle gebruikte categorieen tonen
    elif keuze == "7":

        cursor.execute(
            """
            SELECT DISTINCT categorie
            FROM Verkoop
            """
        )

        categorieen = cursor.fetchall()

        for categorie in categorieen:
            print(categorie[0])


    # 8. Totale opbrengst van een maand
    elif keuze == "8":

        maand = input(
            "Welke maand wil je bekijken? "
            "(bijvoorbeeld 2026-09): "
        )

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            """
        )

        verkopen = cursor.fetchall()

        totale_opbrengst_in_maand = 0

        for verkoop in verkopen:

            verkoopmoment = verkoop[0]

            if verkoopmoment[0:7] == maand:

                opbrengst = float(verkoop[2])

                totale_opbrengst_in_maand = (
                    totale_opbrengst_in_maand
                    + opbrengst
                )

        print(
            "Totale opbrengst in",
            maand,
            "is",
            totale_opbrengst_in_maand,
            "euro"
        )


    # Ongeldige keuze
    else:

        print("Ongeldige keuze.")