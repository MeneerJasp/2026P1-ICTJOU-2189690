import sqlite3

def maak_verbinding():
    """Maakt een verbinding met de database."""
    verbinding = sqlite3.connect("db/platenbak.db")
    verbinding.row_factory = sqlite3.Row
    verbinding.execute("PRAGMA foreign_keys = ON")
    verbinding.autocommit = True
    return verbinding

def start_platenbak():
    """Start de interactieve hoofdloop van de platenbak."""
    verbinding = maak_verbinding()

    print("Welkom bij de Platenbak! Veel plezier met je collectie.")

    
    verbinding.close()


if __name__ == '__main__':
    """Startpunt van het script."""
    start_platenbak()