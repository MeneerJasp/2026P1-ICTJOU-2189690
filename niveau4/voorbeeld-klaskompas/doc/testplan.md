# Testplan: Klaskompas

## Voorbereiding

Voor alle testcases wordt de volgende voorbereiding verwacht:

* Maak de tabellen opnieuw aan met `db/creates.sql`
* Start de applicatie met: `python src/klaskompas.py`
* Importeer basisdata via menuoptie 1.

Na deze import is de verwachte basisset:

* Personen: 15 records (o.a. `Lars Jansen`, `Fatima Elhami`, `Tim Kuipers`).
* Hobby's: 5 records (`Gamen`, `Series kijken`, `Fitness`, `Lezen`, `Programmeren`).
* Koppelingen in `persoon_hobby`: 0 records.

---

## UC1 en UC2: Basisdata importeren uit CSV

### Testscenario 1: Gecombineerde import werkt met meegeleverde CSV-bestanden

**Precondities:**

* Database is leeg (opnieuw opgebouwd met `db/creates.sql`).
* `data/personen.csv` en `data/hobbys.csv` zijn ongewijzigd aanwezig.

**Stappen:**

1. Start de applicatie.
2. Kies menuoptie `1`.

**Concrete testwaarden:**

* Geen extra invoer nodig.

**Verwacht resultaat:**

* Personen uit CSV worden toegevoegd, inclusief:
  * `Lars Jansen` met afstand `6.3`
  * `Tim Kuipers` met afstand `0.9`
  * `Milan Brouwer` met afstand `30.0`
* Hobby's uit CSV worden toegevoegd, inclusief:
  * `Lezen` met `individuele_hobby = 1`
  * `Programmeren` met `individuele_hobby = 0`
* Database bevat daarna 15 personen en 5 hobby's.

---

## UC3: Hobby toevoegen

### Testscenario 2: Nieuwe hobby succesvol toevoegen

**Precondities:**

* Basisimport is uitgevoerd.
* Hobby `Schaken` staat nog niet in de tabel `hobby`.

**Stappen:**

1. Kies menuoptie `2`.
2. Voer in bij `Voer naam in van de hobby:` -> `Schaken`
3. Voer in bij `Is dit een individuele hobby? (ja/nee):` -> `ja`
4. Voer in bij `Voer een omschrijving in van de hobby:` -> `Strategisch bordspel`

**Verwacht resultaat:**

* Hobby `Schaken` wordt toegevoegd.

---

## UC5: Student aan hobby koppelen

### Testscenario 3: Koppeling met volgorde succesvol toevoegen

**Precondities:**

* Basisimport is uitgevoerd.
* Er bestaat nog geen koppeling voor `Lars Jansen` met `volgorde = 1`.

**Stappen:**

1. Kies menuoptie `3`.
2. Voer in bij `Voer naam in:` -> `Lars Jansen`
3. Voer in bij `Voer hobby in:` -> `Lezen`
4. Voer in bij `Welk volgnummer heeft deze hobby voor deze persoon?` -> `1`

**Verwacht resultaat:**

* Koppeling wordt toegevoegd zonder foutmeldingen.

---

## UC6: Student loskoppelen van hobby

### Testscenario 4: Bestaande koppeling succesvol verwijderen

**Precondities:**

* Testscenario 3 is uitgevoerd, dus `(Lars Jansen, Lezen, 1)` bestaat.

**Stappen:**

1. Kies menuoptie `4`.
2. Voer in bij `Voer naam in van de persoon waarvan u een hobby wil verwijderen:` -> `Lars Jansen`
3. Voer in bij `Voer naam in van de hobby die u wil verwijderen voor deze persoon:` -> `Lezen`

**Verwacht resultaat:**

* Koppeling wordt verwijderd zonder foutmeldingen.

---

## UC4: Afstand bijwerken

### Testscenario 5: Afstand succesvol bijwerken

**Precondities:**

* Basisimport is uitgevoerd.
* Persoon `Lars Jansen` bestaat met afstand `6.3`.

**Stappen:**

1. Kies menuoptie `5`.
2. Voer in bij `Voer naam in van de persoon die u wilt bijwerken:` -> `Lars Jansen`
3. Voer in bij `Voer nieuwe afstand in:` -> `9.9`

**Verwacht resultaat:**

* Afstand wordt bijgewerkt zonder foutmeldingen.

---

## UC8: Grafiek met afstanden tonen

### Testscenario 6: ASCII-grafiek succesvol tonen

**Precondities:**

* Basisimport is uitgevoerd.

**Stappen:**

1. Kies menuoptie `6`.
2. Kies subkeuze `2` (ASCII-art).
3. Voer in bij `Voer maximale lengte van balk in:` -> `20`
4. Voer in bij `Voer karakter in voor de grafiek (bijv. * of #):` -> `#`

**Verwacht resultaat:**

* Er verschijnt voor elke persoon een balkregel.
* `Milan Brouwer` (30.0 km) heeft de langste balk (20 tekens).
* `Tim Kuipers` (0.9 km) heeft een korte balk (afgerond 1 teken).

---

## UC9: Taartdiagram favoriete hobby's tonen

### Testscenario 7: Taartdiagram succesvol tonen na setup van koppelingen

**Precondities:**

* Basisimport is uitgevoerd.
* Er zijn minimaal 2 koppelingen met `volgorde = 1`.

**Setupstappen (indien nog geen koppelingen aanwezig):**

1. Kies menuoptie `3` en voeg toe: `Lars Jansen` + `Lezen` + volgorde `1`
2. Kies menuoptie `3` en voeg toe: `Fatima Elhami` + `Programmeren` + volgorde `1`

**Stappen:**

1. Kies menuoptie `7`.

**Verwacht resultaat:**

* Er opent een taartdiagram.
* Labels bevatten ten minste `Lezen (1)` en `Programmeren (1)`.

---

## UC12: Aantal personen per hobby tonen

### Testscenario 8: Overzicht met aantallen succesvol tonen

**Precondities:**

* Basisimport is uitgevoerd.
* De volgende koppelingen bestaan:
  * `(Lars Jansen, Lezen, 1)`
  * `(Tim Kuipers, Lezen, 2)`
  * `(Fatima Elhami, Programmeren, 1)`

**Setupstappen (als nodig):**

1. Kies menuoptie `3` voor `Lars Jansen`, hobby `Lezen`, volgorde `1`.
2. Kies menuoptie `3` voor `Tim Kuipers`, hobby `Lezen`, volgorde `2`.
3. Kies menuoptie `3` voor `Fatima Elhami`, hobby `Programmeren`, volgorde `1`.

**Stappen:**

1. Kies menuoptie `8`.

**Verwacht resultaat:**

* Overzicht bevat in elk geval:
  * `Lezen: 2`
  * `Programmeren: 1`

---

## UC7: Personenlijst met hobby's per persoon tonen

### Testscenario 9: Personenlijst met en zonder hobby succesvol tonen

**Precondities:**

* Basisimport is uitgevoerd.
* Minimaal de koppeling `(Lars Jansen, Lezen, 1)` bestaat.

**Setupstappen (als nodig):**

1. Kies menuoptie `3` voor `Lars Jansen`, hobby `Lezen`, volgorde `1`.

**Stappen:**

1. Kies menuoptie `10`.

**Verwacht resultaat:**

* Regel voor `Lars Jansen` toont hobby-informatie met `Lezen`.
* Regel voor een persoon zonder koppeling, bijvoorbeeld `Sofia Martinez`, toont `Geen hobby's`.

---

## UC11: Groepjes op basis van afstand

### Testscenario 10: Groepjes met concrete verwachte indeling



---

## UC10: Database leegmaken

### Testscenario 11: Volledige opschoning van alle tabellen

**Precondities:**

* Basisimport is uitgevoerd.
* Er staat minimaal 1 koppeling in `persoon_hobby` (optioneel, voor volledige verificatie van volgorde).

**Stappen:**

1. Kies menuoptie `12`.

**Verwacht resultaat:**

* Tabel `persoon_hobby` is leeg.
* Tabel `hobby` is leeg.
* Tabel `persoon` is leeg.

---

## UC13: Personen per hobby tonen

### Testscenario 12: Personen per hobby succesvol afdrukken

**Precondities:**

* Basisimport is uitgevoerd.
* De volgende koppelingen bestaan:
  * `(Lars Jansen, Lezen, 1)`
  * `(Fatima Elhami, Programmeren, 1)`
* Voor hobby `Series kijken` bestaat geen koppeling.

**Setupstappen (als nodig):**

1. Kies menuoptie `3` voor `Lars Jansen`, hobby `Lezen`, volgorde `1`.
2. Kies menuoptie `3` voor `Fatima Elhami`, hobby `Programmeren`, volgorde `1`.

**Stappen:**

1. Kies menuoptie `9`.

**Verwacht resultaat:**

* De applicatie print per hobby eerst de hobbynaam.
* Onder `Lezen` staat `Lars Jansen`.
* Onder `Programmeren` staat `Fatima Elhami`.
* Bij `Series kijken` toont de applicatie `Geen personen gevonden voor deze hobby.`
