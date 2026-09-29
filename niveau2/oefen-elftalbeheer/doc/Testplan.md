```md
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

1. Kies `Speler zoeken`.
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

1. Kies `Elftallen bekijken`.
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

---

## Testscenario 5 - Speler verwijderen

**Doel:** Controleren of een bestaande speler kan worden verwijderd.

**Stappen:**

1. Kies `Speler verwijderen`.
2. Voer de naam van een bestaande speler in.
3. Controleer of de speler is verwijderd.

**Verwacht resultaat:**
De speler wordt verwijderd en de melding `Speler is verwijderd` wordt getoond.

**Werkelijk resultaat:**
Nog uitvoeren.

**Resultaat:** Nog uitvoeren

---

## Testscenario 6 - Niet-bestaande speler verwijderen

**Doel:** Controleren wat er gebeurt als een speler niet bestaat.

**Stappen:**

1. Kies `Speler verwijderen`.
2. Voer een naam in die niet in de database staat.
3. Bekijk de melding.

**Verwacht resultaat:**
Er wordt geen speler verwijderd en de melding `Speler niet gevonden` wordt getoond.

**Werkelijk resultaat:**
Nog uitvoeren.

**Resultaat:** Nog uitvoeren

---

## Testscenario 7 - Sessiestatistieken tonen

**Doel:** Controleren of wijzigingen tijdens de sessie worden bijgehouden.

**Stappen:**

1. Start de applicatie opnieuw.
2. Voeg één elftal toe.
3. Voeg één speler toe.
4. Verwijder één speler.
5. Kies `Afsluiten`.

**Verwacht resultaat:**
Het systeem toont dat er 1 elftal is toegevoegd, 1 speler is toegevoegd en 1 speler is verwijderd.

**Werkelijk resultaat:**
Nog uitvoeren.

**Resultaat:** Nog uitvoeren

---

## Testscenario 8 - Sessiestatistieken zonder wijzigingen

**Doel:** Controleren of de tellers op 0 staan als er niets is gewijzigd.

**Stappen:**

1. Start de applicatie opnieuw.
2. Kies direct `Afsluiten`.

**Verwacht resultaat:**
Alle sessietellers tonen 0.

**Werkelijk resultaat:**
Nog uitvoeren.

**Resultaat:** Nog uitvoeren

---

## Testscenario 9 - Gemiddelde leeftijd per elftal

**Doel:** Controleren of de gemiddelde leeftijd per elftal goed wordt berekend.

**Stappen:**

1. Zorg dat een elftal spelers van 14, 15 en 16 jaar bevat.
2. Kies `Gemiddelde leeftijd per elftal`.
3. Bekijk het resultaat.

**Verwacht resultaat:**
De gemiddelde leeftijd van het elftal wordt als `15.0` getoond.

**Werkelijk resultaat:**
Nog uitvoeren.

**Resultaat:** Nog uitvoeren

---

## Testscenario 10 - Gemiddelde leeftijd zonder spelers

**Doel:** Controleren wat er wordt getoond bij een elftal zonder spelers.

**Stappen:**

1. Zorg dat er een elftal zonder spelers bestaat.
2. Kies `Gemiddelde leeftijd per elftal`.
3. Bekijk het resultaat.

**Verwacht resultaat:**
Bij het elftal wordt `Geen spelers` getoond.

**Werkelijk resultaat:**
Nog uitvoeren.

**Resultaat:** Nog uitvoeren
```