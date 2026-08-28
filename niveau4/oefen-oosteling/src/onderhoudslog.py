"""Registratie en rapportage van uitgevoerd onderhoud.

Bevat functies voor onderhoudsregistraties en visualisaties per attractie en onderhoudstype.
"""


import attractie
import onderhoudstype

def registreer_uitgevoerd_onderhoud(verbinding):
    """Registreert een uitgevoerd onderhoud in de database."""
    attractienaam = input("Voer de naam van de attractie in: ")
    if not attractie.attractie_bestaat(verbinding, attractienaam):
        print("Deze attractie bestaat niet.")
        return
    onderhoudstypenaam = input("Voer de naam van het onderhoudstype in: ")
    if not onderhoudstype.onderhoudstype_bestaat(verbinding, onderhoudstypenaam):
        print("Dit onderhoudstype bestaat niet.")
        return
    datum = input("Voer de datum van het onderhoud in (YYYY-MM-DD): ")
    dagen_buiten_bedrijf = input("Hoeveel dagen is de attractie buiten bedrijf geweest? ")
    registreer_uitgevoerd_onderhoud_in_database(verbinding, attractienaam, onderhoudstypenaam, datum, dagen_buiten_bedrijf)

def registreer_uitgevoerd_onderhoud_in_database(verbinding, attractienaam, onderhoudstype, datum, dagen_buiten_bedrijf):
    """Registreert een uitgevoerd onderhoud in de database."""
    cursor = verbinding.cursor()
    cursor.execute("INSERT INTO onderhoudslog (attractie, onderhoudstype, datum, dagen_buiten_bedrijf) VALUES (?, ?, ?, ?)", (attractienaam, onderhoudstype, datum, dagen_buiten_bedrijf))
    print(f"Uitgevoerd onderhoud voor attractie '{attractienaam}' succesvol geregistreerd in de database.")
    
def toon_uitgevoerde_onderhoudsregistraties(verbinding):
    """Toont alle uitgevoerde onderhoudsregistraties in de database."""
    uitgevoerde_onderhoudsregistraties = haal_uitgevoerde_onderhoudsregistraties_op_uit_database(verbinding)
    for registratie in uitgevoerde_onderhoudsregistraties:
        print(f"Attractie: {registratie['attractie']}, Onderhoudstype: {registratie['onderhoudstype']}, Datum: {registratie['datum']}, Dagen buiten bedrijf: {registratie['dagen_buiten_bedrijf']}")

def haal_uitgevoerde_onderhoudsregistraties_op_uit_database(verbinding):
    """Haalt alle uitgevoerde onderhoudsregistraties op uit de database."""
    cursor = verbinding.cursor()
    cursor.execute("SELECT attractie, onderhoudstype, datum, dagen_buiten_bedrijf FROM onderhoudslog")
    return cursor.fetchall()

def toon_aantal_uitgevoerde_onderhoudsregistraties_per_attractie(verbinding):
    '''Interactieve functie om een grafiek te tonen met het aantal uitgevoerde onderhoudsregistraties per attractie'''
    subkeuze = input(
        'Wilt u een grafiek als afbeelding (1) of als ASCII-art (2) ? ')
    if subkeuze == '1':
        toon_grafiek_van_aantal_uitgevoerde_onderhoudsregistraties_per_attractie_als_afbeelding(verbinding)
    elif subkeuze == '2':
        maximum_staaflengte = input(
            'Voer maximale lengte van balk in: ')
        maximum_staaflengte = int(maximum_staaflengte)
        if maximum_staaflengte <= 0:
            print('Ongeldige invoer. Maximale lengte moet groter zijn dan 0.')
            return # Ga niet verder met de functie, omdat de waarde niet geldig is.
        karakter = input(
            'Voer karakter in voor de grafiek (bijv. * of #): ')
        toon_grafiek_van_aantal_uitgevoerde_onderhoudsregistraties_per_attractie_als_ascii(
            verbinding, maximum_staaflengte, karakter)

def toon_grafiek_van_aantal_uitgevoerde_onderhoudsregistraties_per_attractie_als_afbeelding(verbinding):
    ''' Functie om aantal uitgevoerde onderhoudsregistraties per attractie uit database te halen en als staafdiagram te tonen'''
    rijen = haal_aantal_uitgevoerde_onderhoudsregistraties_per_attractie_op_uit_database(
        verbinding)
    
    pass
    
    

def toon_grafiek_van_aantal_uitgevoerde_onderhoudsregistraties_per_attractie_als_ascii(
    verbinding, maximum_staaflengte, karakter):
    ''' Functie om aantal uitgevoerde onderhoudsregistraties per attractie uit database te halen en als ASCII-art te tonen'''
    rijen = haal_aantal_uitgevoerde_onderhoudsregistraties_per_attractie_op_uit_database(verbinding)
    
    pass

    


def haal_aantal_uitgevoerde_onderhoudsregistraties_per_attractie_op_uit_database(verbinding):
    '''Functie om aantal uitgevoerde onderhoudsregistraties per attractie uit database te halen'''
    cursor = verbinding.cursor()
    cursor.execute(
        "SELECT attractie, COUNT(*) as aantal FROM onderhoudslog GROUP BY attractie")
    return cursor.fetchall()

def toon_aantal_uitgevoerde_onderhoudsregistraties_per_onderhoudstype(verbinding):
    '''Functie om het aantal uitgevoerde onderhoudsregistraties per onderhoudstype uit database te halen en als taartdiagram te tonen'''
    
    rijen = haal_aantal_uitgevoerde_onderhoudsregistraties_per_onderhoudstype_op_uit_database(verbinding)
    
    pass
    
    


def toon_overzicht_attracties_op_basis_van_buiten_bedrijf_dagen(verbinding):
    """Toont attracties op basis van totale dagen buiten bedrijf, verdeeld in categorieen."""
    aantal_categorieen = input('Voer het aantal categorieen in: ')
    aantal_categorieen = int(aantal_categorieen)
    
    if aantal_categorieen <= 0:
        print('Ongeldige invoer. Aantal categorieen moet groter zijn dan 0.')
        return

    rijen = haal_totaal_dagen_buiten_bedrijf_per_attractie_op_uit_database(verbinding)
    
    pass    
    

def haal_totaal_dagen_buiten_bedrijf_per_attractie_op_uit_database(verbinding):
    """Haalt per attractie het totaal aantal dagen buiten bedrijf op, oplopend gesorteerd."""
    cursor = verbinding.cursor()
    cursor.execute(
        '''SELECT attractie.naam,
                  SUM(onderhoudslog.dagen_buiten_bedrijf) AS totaal_dagen
           FROM attractie
           JOIN onderhoudslog ON onderhoudslog.attractie = attractie.naam
           GROUP BY attractie.naam
           ORDER BY totaal_dagen ASC;'''
    )
    return cursor.fetchall()
    
    
def haal_aantal_uitgevoerde_onderhoudsregistraties_per_onderhoudstype_op_uit_database(verbinding):
    '''Functie om aantal uitgevoerde onderhoudsregistraties per onderhoudstype uit database te halen'''
    cursor = verbinding.cursor()
    cursor.execute(
        "SELECT onderhoudstype, COUNT(*) as aantal FROM onderhoudslog GROUP BY onderhoudstype")
    return cursor.fetchall()