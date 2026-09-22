# Niveau 2, les 2 - Samen & Zelf

## 1. Queries voor Elftalbeheer

Voor iedere user story bekijken we welke SQL-query nodig is.

### US1 - Elftallen bekijken

```sql
SELECT elftallen.omschrijving, spelers.naam
FROM elftallen
INNER JOIN spelers
ON elftallen.code = spelers.elftal_code;
```

**Doel:** zien welke spelers bij welk elftal horen.

### US2 - Elftal toevoegen

```sql
INSERT INTO elftallen (code, omschrijving, coach, maximumleeftijd)
VALUES ('JO15-1', 'Onder 15 eerste team', 'Jan Jansen', 15);
```

**Doel:** een nieuw elftal toevoegen.

### US3 - Speler toevoegen

```sql
INSERT INTO spelers (naam, leeftijd, positie, elftal_code)
VALUES ('Piet de Vries', 14, 'Aanvaller', 'JO15-1');
```

**Doel:** een nieuwe speler toevoegen.

### US4 - Speler verwijderen

```sql
DELETE FROM spelers
WHERE naam = 'Piet de Vries';
```

**Doel:** een speler verwijderen.

### US5 - Alleen vaste posities kiezen

```sql
SELECT naam
FROM posities;
```

**Doel:** beschikbare posities ophalen.

### US6 - Speler blokkeren als die te oud is

```sql
SELECT spelers.naam, spelers.leeftijd, elftallen.maximumleeftijd
FROM spelers
INNER JOIN elftallen
ON spelers.elftal_code = elftallen.code
WHERE spelers.leeftijd > elftallen.maximumleeftijd;
```

**Doel:** controleren of een speler te oud is voor het elftal.

### US7 - Hele bestand controleren

```sql
SELECT spelers.naam, spelers.leeftijd, elftallen.omschrijving
FROM spelers
INNER JOIN elftallen
ON spelers.elftal_code = elftallen.code
WHERE spelers.leeftijd > elftallen.maximumleeftijd;
```

**Doel:** alle spelers vinden die niet bij hun elftal passen.

### US8 - Gemiddelde leeftijd per elftal

```sql
SELECT elftallen.omschrijving, AVG(spelers.leeftijd) AS gemiddelde_leeftijd
FROM elftallen
INNER JOIN spelers
ON elftallen.code = spelers.elftal_code
GROUP BY elftallen.code, elftallen.omschrijving;
```

**Doel:** de gemiddelde leeftijd per elftal berekenen.

### US9 - Passend elftal voorstellen

```sql
SELECT *
FROM elftallen
WHERE maximumleeftijd >= 14;
```

**Doel:** elftallen vinden waarin een speler van 14 jaar past.

### US10 - Willekeurige speler kiezen

```sql
SELECT *
FROM spelers
ORDER BY RANDOM()
LIMIT 1;
```

**Doel:** één willekeurige speler ophalen.

### US11 - Spelers per elftal exporteren

```sql
SELECT elftallen.omschrijving, spelers.naam, spelers.leeftijd, spelers.positie
FROM elftallen
INNER JOIN spelers
ON elftallen.code = spelers.elftal_code
ORDER BY elftallen.omschrijving, spelers.naam;
```

**Doel:** spelers per elftal ophalen voor export.

### US12 - Speler op naam zoeken

```sql
SELECT *
FROM spelers
WHERE naam LIKE '%Vries%';
```

**Doel:** een speler zoeken op naam.

### US13 - Aantal spelers per positie

```sql
SELECT elftallen.omschrijving, spelers.positie, COUNT(*) AS aantal_spelers
FROM elftallen
INNER JOIN spelers
ON elftallen.code = spelers.elftal_code
GROUP BY elftallen.code, elftallen.omschrijving, spelers.positie;
```

**Doel:** zien hoeveel spelers per positie in ieder elftal zitten.

### US14 - Seizoenslabel gebruiken

```sql
SELECT *
FROM spelers
WHERE seizoen = '2026-2027';
```

**Doel:** spelers van een bepaald seizoen bekijken.

### US15 - Elftal met te weinig spelers

```sql
SELECT elftallen.omschrijving, COUNT(spelers.naam) AS aantal_spelers
FROM elftallen
INNER JOIN spelers
ON elftallen.code = spelers.elftal_code
GROUP BY elftallen.code, elftallen.omschrijving
HAVING COUNT(spelers.naam) < 11;
```

**Doel:** elftallen vinden met minder dan 11 spelers.

---

# 2. Use cases

Een **use case** beschrijft stap voor stap hoe een gebruiker een bepaalde functie van de applicatie gebruikt.

Een **user story** beschrijft vooral:

* wat de gebruiker wil;
* waarom de gebruiker dit wil.

Een **use case** beschrijft:

* hoe de gebruiker dit doet;
* wat het systeem doet.

## Gebruiker

De officiële term hiervoor is **actor**.

Een **actor** is de gebruiker die de applicatie gebruikt.

Bij Elftalbeheer is dit bijvoorbeeld:

> **Gebruiker: Medewerker**

## Voorwaarde vooraf

De officiële term hiervoor is **preconditie**.

Een **preconditie** is iets wat al geregeld of aanwezig moet zijn voordat de use case kan beginnen.

Bijvoorbeeld:

> **Voorwaarde vooraf:** Er moeten spelers in het gekozen elftal aanwezig zijn.

---

# 3. Voorbeeld use case

## UC6: Gemiddelde leeftijd per elftal

**Gebruiker:** Bestuurder

**Voorwaarde vooraf:** Er moeten spelers in het gekozen elftal aanwezig zijn.

**Beschrijving:**

1. De bestuurder kiest de optie "Gemiddelde leeftijd".
2. Het systeem toont alle beschikbare elftallen.
3. De bestuurder selecteert een elftal.
4. Het systeem berekent de gemiddelde leeftijd van alle spelers in dat elftal.
5. Het systeem toont de gemiddelde leeftijd met één decimaal nauwkeurigheid.

---

# 4. Kwaliteitseisen voor een goede use case

Een goede use case moet:

1. **Duidelijk** zijn.
2. **Stap voor stap** beschreven zijn.
3. Een duidelijke **gebruiker** hebben.
4. Een duidelijke **voorwaarde vooraf** hebben.
5. Beschrijven wat de **gebruiker en het systeem** doen.

---

# 5. Belangrijk

Een use case wordt later gebruikt om **testcases** te maken.

Daarom moet een use case duidelijk en nauwkeurig genoeg zijn om later te kunnen controleren of de functionaliteit goed werkt.