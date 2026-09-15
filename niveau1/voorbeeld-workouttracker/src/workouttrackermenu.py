import sqlite3
from datetime import datetime

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
    print("7. Toon alle unieke workouts")
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
    if keuze == "1":
        cursor.execute("SELECT * FROM Workout")
        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)

    # 2. Alle hardloop workouts
    if keuze == "2":
        cursor.execute(
            "SELECT * FROM Workout WHERE type = 'Hardlopen'"
        )

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)

    # 3. Alle krachttraining workouts
    if keuze == "3":
        cursor.execute(
            "SELECT * FROM Workout WHERE type = 'Krachttraining'"
        )

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)

    # 4. Alle andere workouts
    if keuze == "4":
        cursor.execute(
            """
            SELECT * FROM Workout
            WHERE type != 'Hardlopen'
            AND type != 'Krachttraining'
            """
        )

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)

    # 5. Nieuwe workout toevoegen
    if keuze == "5":

        type_workout = input("Welke workout? ")
        duur = input("Hoeveel minuten? ")

        datumtijd = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            """
            INSERT INTO Workout (datumtijd, type, duur)
            VALUES (?, ?, ?)
            """,
            (datumtijd, type_workout, duur)
        )

        connection.commit()

        print("Workout toegevoegd.")

    # 6. Totale duur van alle workouts
    if keuze == "6":
        cursor.execute("SELECT SUM(duur) FROM Workout")

        totaal = cursor.fetchone()

        print("Totale duur:", totaal[0], "minuten")

    # 7. Alle unieke workouts
    if keuze == "7":
        cursor.execute("SELECT DISTINCT type FROM Workout")

        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout[0])   