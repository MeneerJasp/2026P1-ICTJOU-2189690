import sqlite3

connection = sqlite3.connect(
    "niveau1/voorbeeld-workouttracker/db/workouttracker.db"
)

cursor = connection.cursor()

keuze = "" 

while keuze.upper() != "X":

    print()
    print("=== Workouttracker ===")
    print("1. Toon alle workouts")
    print("2. Toon alle hardloop workouts")
    print("3. Toon alle krachttraining workouts")
    print("4. Toon alle andere workouts")
    print("5. Nieuwe workout toevoegen")
    print("6. Totale duur van workouts tonen")
    print("7. Toon alle unieke workout types")
    print("X. Afsluiten")

    keuze = input("Maak een keuze: ")

    print("Je hebt gekozen voor:", keuze)
    print()

    # Afsluiten
    if keuze.upper() == "X":
        print("Dag!")
        connection.close()
        quit()

    # 1. Alle workouts tonen
    elif keuze == "1":
        cursor.execute(
            """
            SELECT datumtijd, type, duur
            FROM Workout
            """
        )

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)

    # 2. Alle hardloop workouts
    elif keuze == "2":
        cursor.execute(
            """
            SELECT datumtijd, type, duur
            FROM Workout
            WHERE type = 'Hardlopen'
            """
        )

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)

    # 3. Alle krachttraining workouts
    elif keuze == "3":
        cursor.execute(
            """
            SELECT datumtijd, type, duur
            FROM Workout
            WHERE type = 'Krachttraining'
            """
        )

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)

    # 4. Alle andere workouts
    elif keuze == "4":
        cursor.execute(
            """
            SELECT datumtijd, type, duur
            FROM Workout
            WHERE type != 'Hardlopen'
            AND type != 'Krachttraining'
            """
        )

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)

    # 5. Nieuwe workout toevoegen
    elif keuze == "5":

        datumtijd = input(
            "Datum en tijd (bijvoorbeeld 2026-09-15 14:30:00): "
        )

        type_workout = input(
            "Type workout: "
        )

        duur = input(
            "Duur in minuten: "
        )

        cursor.execute(
            """
            INSERT INTO Workout (datumtijd, type, duur)
            VALUES (?, ?, ?)
            """,
            (
                datumtijd,
                type_workout,
                duur
            )
        )

        connection.commit()

        print()
        print("Workout is succesvol toegevoegd!")

    # 6. Totale duur van alle workouts
    elif keuze == "6":
        cursor.execute("SELECT * FROM Workout")
        workouts = cursor.fetchall()

        totale_duur_in_minuten = 0

        for workout in workouts:
            duur = workout[2]
            totale_duur_in_minuten += duur

        uren = totale_duur_in_minuten // 60
        minuten = totale_duur_in_minuten % 60

        print(
            "Totale duur:",
            uren,
            "uur en",
            minuten,
            "minuten"
        )

    #betere versie:
    #elif keuze == "6":
    #    cursor.execute(
    #        """
    #        SELECT SUM(duur)
    #        FROM Workout
    #        """
    #    )

    #    totaal = cursor.fetchone()

    #    print(
    #        "Totale duur:",
    #        totaal[0],
    #        "minuten"
    #    )

    # 7. Alle unieke workout types
    elif keuze == "7":
        cursor.execute(
            """
            SELECT DISTINCT type
            FROM Workout
            """
        )

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout[0])

    # Ongeldige keuze
    else:
        print("Ongeldige keuze.")