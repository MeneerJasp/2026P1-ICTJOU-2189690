# Testscenario's Elftalbeheer

## Testscenario 1 - Elftal en speler toevoegen

**Doel:** Controleren of een elftal en speler kunnen worden toegevoegd.

**Stappen:**

1. Kies `Elftal toevoegen`.
2. Vul de gegevens van een nieuw elftal in.
3. Kies `Speler toevoegen`.
4. Vul de gegevens van een nieuwe speler in.
5. Controleer de database.

**Verwacht resultaat:**
Het elftal en de speler worden succesvol toegevoegd aan de database.

**Werkelijk resultaat:**
Het elftal en de speler zijn succesvol toegevoegd aan de database.

**Resultaat:** Geslaagd

---

## Testscenario 2 - Speler zoeken op naam

**Doel:** Controleren of een speler op naam kan worden gevonden.

**Stappen:**

1. Kies `Speler zoeken op naam`.
2. Voer de naam van een bestaande speler in.
3. Bekijk het resultaat.

**Verwacht resultaat:**
De juiste speler wordt getoond.

**Werkelijk resultaat:**
De juiste speler wordt getoond.

**Resultaat:** Geslaagd

---

## Testscenario 3 - Overzicht elftallen met spelers

**Doel:** Controleren of alle elftallen met hun spelers worden weergegeven.

**Stappen:**

1. Kies `Alle elftallen met spelers`.
2. Bekijk het overzicht.

**Verwacht resultaat:**
Alle elftallen worden getoond met de bijbehorende spelers.

**Werkelijk resultaat:**
Alle elftallen worden getoond met de bijbehorende spelers.

**Resultaat:** Geslaagd

---

## Testscenario 4 - Leeftijdscontrole

**Doel:** Controleren of een te oude speler niet wordt toegevoegd.

**Stappen:**

1. Kies `Speler toevoegen`.
2. Voer een leeftijd in die hoger is dan de maximumleeftijd van het gekozen elftal.
3. Probeer de speler toe te voegen.

**Verwacht resultaat:**
De speler wordt niet toegevoegd en er wordt een melding gegeven dat de speler te oud is.

**Werkelijk resultaat:**
De speler wordt niet toegevoegd en de melding wordt weergegeven.

**Resultaat:** Geslaagd