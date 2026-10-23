## Kwaliteitseisen Use Cases

- De actor en precondities zijn duidelijk.
- De normale flow beschrijft stap voor stap wat de gebruiker en het systeem doen.
- Een alternatieve flow verwijst naar de stap waar het anders loopt.
- Bij een fout is duidelijk welke melding volgt, of de use case stopt en of gegevens veranderen.

## Kwaliteitseisen testplan

- Elk scenario heeft een concrete voorbereiding of preconditie.
- De invoer en de uit te voeren stappen zijn duidelijk.
- Het verwachte resultaat is controleerbaar, ook in de opgeslagen gegevens.
- De normale flow en de alternatieve flows uit de Use Case hebben testscenario's.

## Voorstel kwaliteitseisen domeinmodellen (nog met de groep bespreken)

1. De entiteittypen komen uit de casus en hebben duidelijke namen.
2. Attributen staan bij het entiteittype waar ze bij horen.
3. Elk entiteittype heeft een primary identifier; die is onderstreept.
4. Een zwak entiteittype heeft een complete identificatie via zijn eigen attribuut en het entiteittype waarvan het afhankelijk is.
5. Relaties hebben een naam en verbinden de juiste entiteittypen.
6. Bij beide kanten van elke relatie staat de minimale en maximale kardinaliteit.
7. Verplichte en optionele relaties kloppen met het interview en de voorbeelden.
8. Het model bevat geen technische koppelingattributen of databasetermen.
9. Het model is leesbaar en gebruikt overal dezelfde notatie.

## Oefening kunstacademie (voorbeeld om samen te bespreken)

- Afstudeerwerk: titel (primary identifier), type, naam maker en optioneel beschrijving.
- Afbeelding: volgnummer (deel van de identificatie) en bestandsnaam.
- Een afstudeerwerk heeft 1 of meer afbeeldingen; een afbeelding hoort bij precies 1 afstudeerwerk.
- Afbeelding is zwak: afstudeerwerktitel en volgnummer identificeren samen een afbeelding. De pijl loopt van Afbeelding naar Afstudeerwerk.

## Les 3.4 - Increment 2 en Python modules

### Vraag: Waarom komt User Story 9 (totale kosten = prijs + verzendkosten) in drie Use Cases voor?

Omdat de totale kosten niet een losse menu-optie zijn, maar een berekening die op meerdere plekken nodig is om goede financiele keuzes te maken:
- Bij **UC5 (Zoeken op budget)** om te zien wat een item echt kost binnen je restbudget.
- Bij **UC6 (Persoonlijk spaarplan berekenen)** om het juiste totaalbedrag te sparen.
- Bij **UC7 (Uitgaven per lijst inzien)** om te controleren of het totaalbedrag inclusief verzendkosten het lijstbudget overschrijdt.

### Use Case-matrix Increment 2 QuestComposer

| User Story | UC5 | UC6 | UC7 | UC8 |
|---|---|---|---|---|
| **US6.** (Totale kosten: prijs + transportkosten) | X | X | X | |
| **US7.** (Kosten per scenario en budgetoverschrijding) | | | X | |
| **US8.** (Onderdelen zoeken binnen prijsrange) | X | | | |
| **US9.** (Maandelijks inkoopritme voor sleutelonderdeel) | | X | | |
| **US10.** (Sessieoverzicht bij afsluiten) | | | | X |

### Orientatie op Python modules

**Drie problemen als alle functies in een enkel bestand staan:**
1. **Slecht overzicht:** Het bestand wordt erg lang, waardoor je lang moet scrollen en moeilijk terugvindt waar een bepaalde functie staat.
2. **Lastiger te onderhouden:** Functies voor verschillende onderdelen (zoals klanten, bestellingen, facturen en de database) staan door elkaar. Bij een aanpassing maak je sneller fouten in andere onderdelen.
3. **Lastig samenwerken in Git:** Als meerdere groepsleden tegelijk in hetzelfde grote bestand werken, ontstaan er snel merge-conflicten.

**Oplossing:**
De code opsplitsen in aparte Python-bestanden (modules) per onderwerp, bijvoorbeeld `klantbeheer.py`, `bestellingbeheer.py`, `factuurbeheer.py` en een hoofdmodule voor het menu. Met `import` kun je de functies vanuit de hoofdmodule aanroepen.

## Les 3.5 - Software Architectuur, import en SQL

### Wat is een module in Python?
Een module is een los Python-bestand (met de extensie `.py`) waarin functies en variabelen staan die bij hetzelfde onderwerp horen. Door die module te importeren in een ander bestand kun je de code hergebruiken en blijft het hoofdprogramma overzichtelijk.

**Waar moet je op letten bij het maken van een module (zoals `belasting.py`)?**
- **De naam:** Een duidelijke naam in kleine letters zonder spaties (en niet dezelfde naam als een standaard Python-module).
- **De plek:** Het bestand moet in dezelfde map (`src/`) staan als het hoofdprogramma, zodat Python het bestand kan vinden.
- **De import:** Bovenaan in `main.py` zet je `import belasting` (aanroep: `belasting.bereken_btw(100)`) of `from belasting import bereken_btw` (aanroep: `bereken_btw(100)`).

### Indeling van de voorbeeldfuncties in 5 modules

1. **`main.py` (Hoofdmodule):**
   - `start_applicatie()`
   - `toon_menu()`
   - `maak_verbinding()`
2. **`klantbeheer.py`:**
   - `voeg_klant_toe(klanten, klantgegevens)`
   - `zoek_klant(klanten, klant_id)`
3. **`bestellingbeheer.py`:**
   - `maak_bestelling(klant_id, producten)`
   - `annuleer_bestelling(bestelling_id)`
   - `beheer_voorraad(producten, product_id, wijziging)`
4. **`factuurbeheer.py`:**
   - `maak_factuur(bestelling_id)`
   - `bereken_btw(bedrag, btw_percentage)`
5. **`rapportagebeheer.py`:**
   - `toon_omzet(bestellingen, periode)`
   - `haal_statistieken_op_uit_database(verbinding)`

### Overzicht importvormen

| Importvorm in `main.py` | Aanroep in `main.py` | Voordeel | Nadeel |
|---|---|---|---|
| `import belasting` | `belasting.bereken_btw(100)` | Je ziet direct uit welke module de functie komt. | Je moet steeds de modulenaam ervoor typen. |
| `from belasting import bereken_btw` | `bereken_btw(100)` | Kortere aanroep en je ziet bovenin precies welke functie gebruikt wordt. | Kans op naamconflict als `main.py` zelf ook een functie met die naam heeft. |
| `from belasting import *` | `bereken_btw(100)` | Alles uit de module is in een keer beschikbaar. | Onoverzichtelijk: je ziet niet meer waar functies vandaan komen en namen kunnen elkaar overschrijven. |
| `import belasting as bel` | `bel.bereken_btw(100)` | Korter typen bij lange modulenamen en toch duidelijk waar het vandaan komt. | Een onduidelijke afkorting maakt de code minder leesbaar. |
| `from belasting import bereken_btw as btw` | `btw(100)` | Handig om een lange functienaam in te korten of een naamconflict op te lossen. | De functie heet in `main.py` anders dan in `belasting.py`, wat verwarrend kan zijn. |

### Foutmeldingen bij importeren

- **`ModuleNotFoundError: No module named 'belasting'`**: Het bestand `belasting.py` bestaat niet, heeft een spelfout in de bestandsnaam of staat in een verkeerde map. Oplossing: controleer de bestandsnaam en zorg dat het in dezelfde map staat.
- **`ImportError: cannot import name 'bereken_btw' from 'belasting'`**: De module `belasting.py` bestaat wel, maar de functie `bereken_btw` staat er niet in (of is verkeerd gespeld). Oplossing: controleer de functienaam in `belasting.py`.
- **`NameError: name 'bereken_btw' is not defined`**: Je roept `bereken_btw(100)` direct aan terwijl je helemaal niets hebt geimporteerd, of alleen `import belasting` hebt gedaan (dan moet het `belasting.bereken_btw(100)` zijn).
- **`SyntaxError: invalid syntax`**: Er zit een schrijffout in het `import`-statement zelf (bijvoorbeeld `import from belasting`). Oplossing: verbeter de Python-syntax.
- **`AttributeError: module 'belasting' has no attribute 'bereken_btw'`**: Je hebt `import belasting` gedaan en roept `belasting.bereken_btw(100)` aan, maar die functie bestaat niet in `belasting.py`. Oplossing: controleer de functienaam in `belasting.py`.
- **Circulaire import (module A doet `import B` en module B doet `import A`)**: Python raakt in een cirkel terecht tijdens het inladen, waardoor een module nog niet volledig geladen is als de andere er al een functie uit probeert te gebruiken (`ImportError` of `AttributeError`). Oplossing: zorg dat de aanroepen maar een kant op gaan (vanuit de hoofdmodule naar de sub-modules).

### Kwaliteitseisen voor Software Architectuur

- Als er pijlen heen en weer gaan tussen modules, zijn de modules onderling afhankelijk van elkaar. Dit is niet verstandig en heet **spaghetticode**.
- **Kwaliteitseisen:**
  1. Elke module bevat alleen functies die logisch bij hetzelfde onderwerp horen.
  2. Er is een duidelijke hoofdmodule die de andere modules aanroept.
  3. Pijlen lopen van boven naar beneden (geen circulaire imports of pijlen heen en weer tussen alle modules).
  4. Modules en functies hebben duidelijke Nederlandse namen.

### SQL WHERE met BETWEEN, LIKE en IN

**1. BETWEEN:**
- Vraag: Tellen items met een prijs van 10 en 50 mee bij `WHERE prijs BETWEEN 10 AND 50`?
- Antwoord: **Ja**, `BETWEEN` is inclusief de ondergrens (10) en de bovengrens (50).

**2. LIKE oefeningen:**
```sql
-- Alle items waarvan de naam eindigt op 'er'
SELECT *
FROM Item
WHERE titel LIKE '%er';

-- Alle items waarvan de naam 'a' bevat
SELECT *
FROM Item
WHERE titel LIKE '%a%';

-- Alle items waarvan de naam precies 5 tekens lang is
SELECT *
FROM Item
WHERE titel LIKE '_____';