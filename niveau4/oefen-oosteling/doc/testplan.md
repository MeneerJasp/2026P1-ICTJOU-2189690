# Testplan: Oosteling

## Voorbereiding

Voor alle testcases wordt de volgende voorbereiding verwacht:

* Maak de tabellen opnieuw aan met `db/create.sql`.
* Start de applicatie met: `python src/oosteling.py`.
* Log in met een geldige toegangscode uit `.env`.
* Importeer basisdata via menuopties `1` en `2`.

Na deze import is de verwachte basisset:

* Attracties: 8 records (o.a. `Nachtvlucht`, `Rockbird`, `Kompelklap`).
* Onderhoudstypes: 5 records (`Smeersysteem`, `Schilderwerk`, `Beugel-inspectie`, `Sensor-kalibratie`, `Schoonmaakbeurt`).
* Onderhoudsregistraties: 0 records.

---

## UC1: Attracties importeren uit CSV-bestand

### Testscenario 1: Import van attracties werkt met meegeleverd CSV-bestand

**Precondities:**

* Database is leeg (opnieuw opgebouwd met `db/create.sql`).
* `data/attracties.csv` is ongewijzigd aanwezig.

**Stappen:**

1. Start de applicatie.
2. Kies menuoptie `1`.
3. Kies menuoptie `6`.

**Concrete testwaarden:**

* Geen extra invoer nodig.

**Verwacht resultaat:**

* 8 attracties zijn toegevoegd.
* Overzicht bevat onder andere:
  * `Nachtvlucht` (`1993`, `Mythenrijk`)
  * `Rockbird` (`1998`, `Expeditierijk`)
  * `Pantagorica` (`2017`, `Mythenrijk`)

---

## UC2: Onderhoudstypes importeren uit CSV-bestand

### Testscenario 2: Import van onderhoudstypes werkt met meegeleverd CSV-bestand

**Precondities:**

* Database is leeg of bevat nog geen onderhoudstypes.
* `data/onderhoudstypes.csv` is ongewijzigd aanwezig.

**Stappen:**

1. Start de applicatie.
2. Kies menuoptie `2`.
3. Kies menuoptie `7`.

**Concrete testwaarden:**

* Geen extra invoer nodig.

**Verwacht resultaat:**

* 5 onderhoudstypes zijn toegevoegd.
* Overzicht bevat onder andere:
  * `Smeersysteem` met `Veiligheidskritisch: Ja`
  * `Schilderwerk` met `Veiligheidskritisch: Nee`

---

## UC3: Nieuwe attractie toevoegen

### Testscenario 3: Nieuwe attractie succesvol toevoegen

**Precondities:**

* Basisimport is uitgevoerd.
* Attractie `Sterrenstorm` bestaat nog niet.

**Stappen:**

1. Kies menuoptie `3`.
2. Voer in bij naam: `Sterrenstorm`.
3. Voer in bij bouwjaar: `2027`.
4. Voer in bij locatie: `Mythenrijk`.
5. Voer in bij omschrijving: `Testattractie voor validatie van toevoegen`.
6. Kies menuoptie `6`.

**Verwacht resultaat:**

* Applicatie meldt dat attractie succesvol is toegevoegd.
* `Sterrenstorm` staat in het attractie-overzicht.

---

## UC4: Nieuw onderhoudstype toevoegen

### Testscenario 4: Nieuw onderhoudstype succesvol toevoegen

**Precondities:**

* Basisimport is uitgevoerd.
* Onderhoudstype `Remtest` bestaat nog niet.

**Stappen:**

1. Kies menuoptie `4`.
2. Voer in bij naam: `Remtest`.
3. Voer in bij veiligheidskritisch: `ja`.
4. Voer in bij omschrijving: `Controle van remsystemen onder belasting`.
5. Kies menuoptie `7`.

**Verwacht resultaat:**

* Applicatie meldt dat onderhoudstype succesvol is toegevoegd.
* `Remtest` staat in het onderhoudstype-overzicht met `Veiligheidskritisch: Ja`.

---

## UC5: Uitgevoerd onderhoud registreren

### Testscenario 5: Onderhoudsregistratie succesvol vastleggen

**Precondities:**

* Basisimport is uitgevoerd.
* Attractie `Rockbird` bestaat.
* Onderhoudstype `Smeersysteem` bestaat.

**Stappen:**

1. Kies menuoptie `5`.
2. Voer in bij attractie: `Rockbird`.
3. Voer in bij onderhoudstype: `Smeersysteem`.
4. Voer in bij datum: `2026-06-26`.
5. Voer in bij dagen buiten bedrijf: `4`.
6. Kies menuoptie `8`.

**Verwacht resultaat:**

* Applicatie meldt dat onderhoud succesvol is geregistreerd.
* Overzicht van onderhoudsregistraties bevat de ingevoerde regel.

---

## UC6: Overzicht van alle attracties weergeven

### Testscenario 6: Attractie-overzicht toont alle kernvelden

**Precondities:**

* Basisimport is uitgevoerd.

**Stappen:**

1. Kies menuoptie `6`.

**Verwacht resultaat:**

* Voor elke attractie worden `Naam`, `Bouwjaar`, `Locatie` en `Omschrijving` getoond.
* Minimaal 8 regels met attracties worden getoond.

---

## UC7: Overzicht van alle onderhoudstypes weergeven

### Testscenario 7: Onderhoudstype-overzicht toont alle kernvelden

**Precondities:**

* Basisimport is uitgevoerd.

**Stappen:**

1. Kies menuoptie `7`.

**Verwacht resultaat:**

* Voor elk onderhoudstype worden `Naam`, `Veiligheidskritisch` en `Omschrijving` getoond.
* Minimaal 5 regels met onderhoudstypes worden getoond.

---

## UC8: Overzicht van alle onderhoudsregistraties weergeven

### Testscenario 8: Onderhoudsregistraties-overzicht toont alle kernvelden

**Precondities:**

* Basisimport is uitgevoerd.
* Er bestaan minimaal 2 onderhoudsregistraties, bijvoorbeeld:
  * `Rockbird` + `Smeersysteem` + `2026-06-26` + `4`
  * `Nachtvlucht` + `Beugel-inspectie` + `2026-06-27` + `2`

**Stappen:**

1. Kies menuoptie `8`.

**Verwacht resultaat:**

* Overzicht toont per registratie: attractie, onderhoudstype, datum en dagen buiten bedrijf.
* Beide voorbeeldregistraties zijn zichtbaar.

---

## UC9: Staafdiagram per attractie weergeven

### Testscenario 9: ASCII-staafdiagram per attractie wordt correct getoond

**Precondities:**

* Basisimport is uitgevoerd.
* Er bestaan onderhoudsregistraties voor minimaal 2 attracties.

**Stappen:**

1. Kies menuoptie `9`.
2. Kies subkeuze `2` (ASCII).
3. Voer in bij maximale balklengte: `20`.
4. Voer in bij karakter: `#`.

**Verwacht resultaat:**

* Voor elke attractie met onderhoud verschijnt een regel met balk.
* Attractie met hoogste aantal registraties heeft de langste balk.

---

## UC10: Taartdiagram per onderhoudstype weergeven

### Testscenario 10: Taartdiagram per onderhoudstype wordt getoond

**Precondities:**

* Basisimport is uitgevoerd.
* Er bestaan onderhoudsregistraties met minimaal 2 verschillende onderhoudstypes.

**Stappen:**

1. Kies menuoptie `10`.

**Verwacht resultaat:**

* Een taartdiagram opent.
* Labels komen overeen met de gebruikte onderhoudstypes.

---

## UC11: Toegangscontrole bij opstarten

### Testscenario 11: Toegangscodecontrole werkt voor fout en succes

**Precondities:**

* `.env` bevat een geldige `TOEGANGSCODE_HASH`.

**Stappen:**

1. Start de applicatie.
2. Voer eerst een onjuiste toegangscode in.
3. Start de applicatie opnieuw.
4. Voer daarna de juiste toegangscode in.

**Verwacht resultaat:**

* Bij onjuiste code: melding `FOUT: Onjuiste toegangscode.` en applicatie stopt.
* Bij juiste code: hoofdmenu wordt getoond.

---

## UC12: Overzicht attracties per categorie buiten bedrijf dagen

### Testscenario 12: Categorie-overzicht op basis van totaaldagen buiten bedrijf

**Precondities:**

* Basisimport is uitgevoerd.
* Er zijn onderhoudsregistraties aanwezig met verschillende totaaldagen, bijvoorbeeld:
  * `Rockbird`: totaal 30 dagen
  * `Nachtvlucht`: totaal 8 dagen
  * `Kompelklap`: totaal 5 dagen

**Stappen:**

1. Kies menuoptie `11`.
2. Voer in bij aantal categorieen: `3`.

**Verwacht resultaat:**

* De applicatie toont categoriegrenzen en attracties per categorie.
* Met bovenstaande data wordt in elk geval een indeling getoond waarbij:
  * `Rockbird` in de hoogste categorie valt.
  * `Nachtvlucht` en `Kompelklap` in lagere categorieen vallen.
* Lege categorieen zijn toegestaan.
