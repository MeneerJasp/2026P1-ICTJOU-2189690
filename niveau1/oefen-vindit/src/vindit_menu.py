import os
import sys
import shutil
import subprocess
import sqlite3

from pathlib import Path
from datetime import datetime


# ==================================================
# INSTELLINGEN
# ==================================================

# True  = openen in apart terminalvenster
# False = draaien in huidige terminal
APARTE_TERMINAL = True


# ==================================================
# APART TERMINALVENSTER OPENEN
# ==================================================

if APARTE_TERMINAL and os.environ.get("VINDIT_TERMINAL") != "1":

    script = str(Path(__file__).resolve())

    omgeving = os.environ.copy()
    omgeving["VINDIT_TERMINAL"] = "1"

    if shutil.which("ptyxis"):
        subprocess.Popen(
            ["ptyxis", "--", sys.executable, script],
            env=omgeving
        )
        sys.exit()

    elif shutil.which("gnome-terminal"):
        subprocess.Popen(
            ["gnome-terminal", "--", sys.executable, script],
            env=omgeving
        )
        sys.exit()

    elif shutil.which("konsole"):
        subprocess.Popen(
            ["konsole", "-e", sys.executable, script],
            env=omgeving
        )
        sys.exit()

    elif shutil.which("xterm"):
        subprocess.Popen(
            ["xterm", "-e", sys.executable, script],
            env=omgeving
        )
        sys.exit()


# ==================================================
# DATABASE
# ==================================================

database = (
    Path(__file__).resolve().parent.parent
    / "db"
    / "vindit.db"
)

connection = sqlite3.connect(database)
cursor = connection.cursor()


# ==================================================
# KLEUREN
# ==================================================

CYAAN = "\033[96m"
GROEN = "\033[92m"
GEEL = "\033[93m"
ROOD = "\033[91m"
PAARS = "\033[95m"
VET = "\033[1m"
RESET = "\033[0m"


# ==================================================
# FUNCTIES
# ==================================================

def leeg_scherm():
    os.system("clear")


def wachten():
    input(
        GEEL
        + "\nDruk op ENTER om terug te gaan naar het menu..."
        + RESET
    )


def toon_menu():
    leeg_scherm()

    print(CYAAN + VET)
    print("+-----------------------------------------------------+")
    print("|              VIND IT! VERKOOPMANAGER                |")
    print("|                                                     |")
    print("|  Maak je keuze:                                     |")
    print("|                                                     |")
    print("|  1. Toon alle verkopen                              |")
    print("|  2. Toon alle kleding-verkopen                      |")
    print("|  3. Toon alle boeken-verkopen                       |")
    print("|  4. Toon alle overige verkopen                      |")
    print("|  5. Nieuwe verkoop toevoegen                        |")
    print("|  6. Totale opbrengst tonen                          |")
    print("|  7. Toon alle gebruikte categorieen                 |")
    print("|  8. Zoeken in verkopen                              |")
    print("|  9. Totale opbrengst per maand tonen                |")
    print("|                                                     |")
    print("|  X. Afsluiten                                       |")
    print("+-----------------------------------------------------+")
    print(RESET)


def toon_verkopen(verkopen):
    leeg_scherm()

    print(CYAAN + VET)
    print("+------------------------------------------------------+")
    print("|                     VERKOPEN                         |")
    print("+------------------------------------------------------+")
    print(RESET)

    if len(verkopen) == 0:
        print(ROOD + "Geen verkopen gevonden." + RESET)

    else:
        for verkoop in verkopen:

            verkoopmoment = verkoop[0]
            categorie = verkoop[1]

            opbrengst = float(
                str(verkoop[2]).replace(",", ".")
            )

            print(
                f"{verkoopmoment} - "
                f"{categorie} - "
                f"{opbrengst:.2f} euro"
            )

    print()
    print("+------------------------------------------------------+")

    wachten()


# ==================================================
# PROGRAMMA
# ==================================================

keuze = ""

while keuze.upper() != "X":

    toon_menu()

    keuze = input(
        GEEL + "Maak je keuze: " + RESET
    )

    # --------------------------------------------------
    # 1. ALLE VERKOPEN
    # --------------------------------------------------

    if keuze == "1":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            ORDER BY verkoopmoment
            """
        )

        verkopen = cursor.fetchall()

        toon_verkopen(verkopen)


    # --------------------------------------------------
    # 2. KLEDING
    # --------------------------------------------------

    elif keuze == "2":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            WHERE LOWER(categorie) = 'kleding'
            ORDER BY verkoopmoment
            """
        )

        verkopen = cursor.fetchall()

        toon_verkopen(verkopen)


    # --------------------------------------------------
    # 3. BOEKEN
    # --------------------------------------------------

    elif keuze == "3":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            WHERE LOWER(categorie) = 'boeken'
            ORDER BY verkoopmoment
            """
        )

        verkopen = cursor.fetchall()

        toon_verkopen(verkopen)


    # --------------------------------------------------
    # 4. OVERIGE VERKOPEN
    # --------------------------------------------------

    elif keuze == "4":

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            WHERE LOWER(categorie) != 'kleding'
            AND LOWER(categorie) != 'boeken'
            ORDER BY verkoopmoment
            """
        )

        verkopen = cursor.fetchall()

        toon_verkopen(verkopen)


    # --------------------------------------------------
    # 5. NIEUWE VERKOOP TOEVOEGEN
    # --------------------------------------------------

    elif keuze == "5":

        leeg_scherm()

        print(GROEN + VET)
        print("+------------------------------------------------------+")
        print("|                 NIEUWE VERKOOP                       |")
        print("+------------------------------------------------------+")
        print(RESET)

        categorie = input(
            "Categorie: "
        ).strip().lower()

        opbrengst_input = input(
            "Opbrengst in euro: "
        )

        opbrengst_input = opbrengst_input.replace(",", ".")

        verkoopmoment_input = input(
            "Datum en tijd (JJJJ-MM-DD UU:MM:SS) [ENTER = nu]: "
        ).strip()

        # Geen datum ingevuld -> huidige datum en tijd
        if verkoopmoment_input == "":
            verkoopmoment = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        else:
            try:
                datetime.strptime(
                    verkoopmoment_input,
                    "%Y-%m-%d %H:%M:%S"
                )

                verkoopmoment = verkoopmoment_input

            except ValueError:
                print()
                print(
                    ROOD
                    + "Ongeldige datum of tijd."
                    + RESET
                )

                print(
                    "Gebruik bijvoorbeeld: 2026-09-15 14:30:00"
                )

                wachten()
                continue

        try:
            opbrengst = float(opbrengst_input)

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

            print()
            print(
                GROEN
                + "✓ Verkoop succesvol toegevoegd!"
                + RESET
            )

            print(
                f"{verkoopmoment} - "
                f"{categorie} - "
                f"{opbrengst:.2f} euro"
            )

        except ValueError:
            print()
            print(
                ROOD
                + "Voer een geldig bedrag in."
                + RESET
            )

        wachten()


    # --------------------------------------------------
    # 6. TOTALE OPBRENGST
    # --------------------------------------------------

    elif keuze == "6":

        leeg_scherm()

        cursor.execute(
            """
            SELECT SUM(
                CAST(
                    REPLACE(opbrengst, ',', '.')
                    AS REAL
                )
            )
            FROM Verkoop
            """
        )

        totaal = cursor.fetchone()[0]

        if totaal is None:
            totaal = 0

        print(GROEN + VET)
        print("+------------------------------------------------------+")
        print("|                 TOTALE OPBRENGST                     |")
        print("+------------------------------------------------------+")
        print(RESET)

        print()
        print(
            VET
            + f"Totale opbrengst: {totaal:.2f} euro"
            + RESET
        )

        print()
        print("+------------------------------------------------------+")

        wachten()


    # --------------------------------------------------
    # 6. TOTALE OPBRENGST
    # --------------------------------------------------

    elif keuze == "6":

        leeg_scherm()

        cursor.execute(
            """
            SELECT SUM(
                CAST(
                    REPLACE(opbrengst, ',', '.')
                    AS REAL
                )
            )
            FROM Verkoop
            """
        )

        totaal = cursor.fetchone()[0]

        if totaal is None:
            totaal = 0

        print(GROEN + VET)
        print("+------------------------------------------------------+")
        print("|                  TOTALE OPBRENGST                    |")
        print("+------------------------------------------------------+")
        print(RESET)

        print()
        print(
            VET
            + f"Totale opbrengst: {totaal:.2f} euro"
            + RESET
        )

        print()
        print("+------------------------------------------------------+")

        wachten()


    # --------------------------------------------------
    # 7. GEBRUIKTE CATEGORIEEN
    # --------------------------------------------------

    elif keuze == "7":

        leeg_scherm()

        cursor.execute(
            """
            SELECT DISTINCT categorie
            FROM Verkoop
            ORDER BY categorie
            """
        )

        categorieen = cursor.fetchall()

        print(PAARS + VET)
        print("+------------------------------------------------------+")
        print("|               GEBRUIKTE CATEGORIEEN                  |")
        print("+------------------------------------------------------+")
        print(RESET)

        if len(categorieen) == 0:
            print("Geen categorieen gevonden.")

        else:
            for categorie in categorieen:
                print(categorie[0])

        print()
        print("+------------------------------------------------------+")

        wachten()


    # --------------------------------------------------
    # 8. ZOEKEN
    # --------------------------------------------------

    elif keuze == "8":

        leeg_scherm()

        print(GEEL + VET)
        print("+------------------------------------------------------+")
        print("|                   ZOEK VERKOPEN                      |")
        print("+------------------------------------------------------+")
        print(RESET)

        zoekterm = input(
            "Waar wil je naar zoeken? "
        ).strip()

        zoekwaarde = "%" + zoekterm + "%"

        cursor.execute(
            """
            SELECT verkoopmoment, categorie, opbrengst
            FROM Verkoop
            WHERE LOWER(categorie) LIKE LOWER(?)
            OR verkoopmoment LIKE ?
            OR CAST(opbrengst AS TEXT) LIKE ?
            ORDER BY verkoopmoment
            """,
            (
                zoekwaarde,
                zoekwaarde,
                zoekwaarde
            )
        )

        resultaten = cursor.fetchall()

        toon_verkopen(resultaten)


    # --------------------------------------------------
    # 9. US6 - TOTALE OPBRENGST PER MAAND
    # --------------------------------------------------

    elif keuze == "9":

        leeg_scherm()

        cursor.execute(
            """
            SELECT verkoopmoment, opbrengst
            FROM Verkoop
            ORDER BY verkoopmoment
            """
        )

        verkopen = cursor.fetchall()

        opbrengst_per_maand = {}

        for verkoop in verkopen:

            verkoopmoment = verkoop[0]

            opbrengst = float(
                str(verkoop[1]).replace(",", ".")
            )


            maand = verkoopmoment[0:7]

            if maand in opbrengst_per_maand:
                opbrengst_per_maand[maand] += opbrengst

            else:
                opbrengst_per_maand[maand] = opbrengst

        print(CYAAN + VET)
        print("+------------------------------------------------------+")
        print("|               OPBRENGST PER MAAND                    |")
        print("+------------------------------------------------------+")
        print(RESET)

        if len(opbrengst_per_maand) == 0:

            print(
                "Er zijn nog geen verkopen."
            )

        else:

            for maand in opbrengst_per_maand:

                print(
                    f"{maand} : "
                    f"€ {opbrengst_per_maand[maand]:.2f}"
                )

        print()
        print("+------------------------------------------------------+")

        wachten()


    # --------------------------------------------------
    # X. AFSLUITEN
    # --------------------------------------------------

    elif keuze.upper() == "X":

        leeg_scherm()

        print(GROEN + VET)
        print("+------------------------------------------------------+")
        print("|                                                      |")
        print("|        BEDANKT VOOR HET GEBRUIKEN VIND IT!           |")
        print("|                                                      |")
        print("+------------------------------------------------------+")
        print(RESET)

        connection.close()


    # --------------------------------------------------
    # ONJUISTE KEUZE
    # --------------------------------------------------

    else:

        print()
        print(
            ROOD
            + "Ongeldige keuze. Kies opties 1 t/m 9 of X om af te sluiten."
            + RESET
        )

        wachten()