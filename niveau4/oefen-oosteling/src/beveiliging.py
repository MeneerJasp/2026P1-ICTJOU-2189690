"""Toegangscontrole voor de Oosteling-onderhoudsapplicatie.

Leest een gehashte toegangscode uit .env en valideert gebruikersinvoer.
"""

import hashlib


def lees_toegangscode_hash():
    """Leest de hash van de toegangscode uit het .env-bestand."""
    bestand = open('.env', mode='r', encoding='utf-8-sig')

    for regel in bestand:
        regel = regel.strip()
        if regel.startswith('TOEGANGSCODE_HASH='):
            bestand.close()
            return regel.replace('TOEGANGSCODE_HASH=', '')

    bestand.close()

    return None


def controleer_toegangscode():
    """Controleert of de ingevoerde toegangscode klopt."""
    ingevoerde_code = input('Voer toegangscode in: ')
    ingevoerde_hash = hashlib.sha256(ingevoerde_code.encode()).hexdigest()
    opgeslagen_hash = lees_toegangscode_hash()

    if opgeslagen_hash is None:
        print('FOUT: TOEGANGSCODE_HASH ontbreekt in .env.')
        return False

    if ingevoerde_hash != opgeslagen_hash:
        print('FOUT: Onjuiste toegangscode.')
        return False

    return True