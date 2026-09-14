import sqlite3

connection = sqlite3.connect(
    "niveau1/voorbeeld-workouttracker/db/workouttracker.db"
)

cursor = connection.cursor()

keuze = ""

while keuze != "X":
    print("=== Workouttracker ===")
    print("1. Toon alle workouts")
    print("X. Afsluiten")

    keuze = input("Maak een keuze: ")

    print("Je hebt gekozen voor:", keuze)

    if keuze == "X" or "x":
        print("Dag!")
        quit()

    if keuze == "1":
        cursor.execute("SELECT * FROM Workout")
        workouts = cursor.fetchall()

        for workout in workouts:
            print(workout)