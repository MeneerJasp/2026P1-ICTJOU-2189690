import hashlib
import os


# ==== Use Case functies ====

def controleer_toegangscode():
    """UC10: Controleert of de ingevoerde toegangscode klopt."""
    opgeslagen_hash = lees_toegangscode_hash()
    if opgeslagen_hash is None or opgeslagen_hash == "":
        print("FOUT: TOEGANGSCODE_HASH ontbreekt in .env.")
        return False

    ingevoerde_code = input("Voer toegangscode in: ")
    ingevoerde_hash = hashlib.sha256(ingevoerde_code.encode()).hexdigest()

    if ingevoerde_hash != opgeslagen_hash:
        print("FOUT: Onjuiste toegangscode.")
        return False

    return True


# === Helper functies ===

def lees_toegangscode_hash():
    """Leest de hash van de toegangscode uit het .env-bestand."""
    pad = ".env"
    if not os.path.exists(pad):
        pad_in_project = "niveau3/oefen-questcomposer/.env"
        if os.path.exists(pad_in_project):
            pad = pad_in_project
        else:
            return None

    bestand = open(pad, mode="r", encoding="utf-8-sig")

    for regel in bestand:
        regel = regel.strip()
        if regel.startswith("TOEGANGSCODE_HASH="):
            bestand.close()
            return regel.replace("TOEGANGSCODE_HASH=", "")

    bestand.close()
    return None