import hashlib


# ==== Use Case functies ====


def controleer_toegangscode():
    """UC10: Controleert of de ingevoerde toegangscode klopt."""
    # Wordt in increment 3 geprogrammeerd.
    return True


# === Helper functies ===


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