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
De speler wordt verwijderd en de melding `Speler is verwijderd` wordt weergegeven.

**Resultaat:** Geslaagd

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
De melding `Speler niet gevonden` wordt weergegeven en er wordt geen speler verwijderd.

**Resultaat:** Geslaagd

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
Het systeem toont 1 toegevoegd elftal, 1 toegevoegde speler en 1 verwijderde speler.

**Resultaat:** Geslaagd

---

## Testscenario 8 - Sessiestatistieken zonder wijzigingen

**Doel:** Controleren of de tellers op 0 staan als er niets is gewijzigd.

**Stappen:**

1. Start de applicatie opnieuw.
2. Kies direct `Afsluiten`.

**Verwacht resultaat:**
Alle sessietellers tonen 0.

**Werkelijk resultaat:**
Alle sessietellers tonen 0.

**Resultaat:** Geslaagd

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
De gemiddelde leeftijd wordt als `15.0` getoond.

**Resultaat:** Geslaagd

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
Bij het elftal wordt `Geen spelers` getoond.

**Resultaat:** Geslaagd

---

## Testscenario 11 - Bestaand elftal opnieuw toevoegen

**Doel:** Controleren of een bestaande elftalcode niet opnieuw kan worden toegevoegd.

**Stappen:**

1. Kies `Elftal toevoegen`.
2. Voer als elftalcode `JO13-1` in.
3. Vul de overige gegevens in.

**Verwacht resultaat:**
Het elftal wordt niet toegevoegd en de melding `Elftal bestaat al` wordt weergegeven.

**Werkelijk resultaat:**
Het elftal wordt niet toegevoegd en de melding `Elftal bestaat al` wordt weergegeven.

**Resultaat:** Geslaagd na bugfix

---

## Testscenario 12 - Elftalsuggestie

**Doel:** Controleren of een passend elftal wordt voorgesteld.

**Stappen:**

1. Kies `Speler toevoegen`.
2. Voer een naam in.
3. Voer leeftijd `14` in.

**Verwacht resultaat:**
Het systeem toont `Voorgesteld elftal: JO15-1`.

**Werkelijk resultaat:**
Het systeem toont `Voorgesteld elftal: JO15-1`.

**Resultaat:** Geslaagd

---

## Testscenario 13 - Geen passende elftalsuggestie

**Doel:** Controleren wat er gebeurt wanneer geen passend elftal bestaat.

**Stappen:**

1. Kies `Speler toevoegen`.
2. Voer een naam in.
3. Voer leeftijd `20` in.

**Verwacht resultaat:**
Het systeem toont `Geen passend elftal gevonden`.

**Werkelijk resultaat:**
Het systeem toont `Geen passend elftal gevonden`.

**Resultaat:** Geslaagd

---

## Testscenario 14 - Speler van de maand

**Doel:** Controleren of willekeurig een bestaande speler wordt gekozen.

**Stappen:**

1. Kies `Speler van de maand`.
2. Bekijk de gekozen speler.

**Verwacht resultaat:**
Het systeem toont een bestaande speler met het bijbehorende elftal.

**Werkelijk resultaat:**
Het systeem toont een bestaande speler met het bijbehorende elftal.

**Resultaat:** Geslaagd

---

## Testscenario 15 - Speler van de maand zonder spelers

**Doel:** Controleren wat er gebeurt wanneer er geen spelers zijn.

**Stappen:**

1. Zorg dat de tabel `speler` leeg is.
2. Kies `Speler van de maand`.

**Verwacht resultaat:**
Het systeem toont `Er zijn geen spelers om uit te kiezen`.

**Werkelijk resultaat:**
Het systeem toont `Er zijn geen spelers om uit te kiezen`.

**Resultaat:** Geslaagd

---

## Testscenario 16 - Ongeldige positie bij speler toevoegen

**Doel:** Controleren of alleen vaste posities gebruikt kunnen worden.

**Stappen:**

1. Kies `Speler toevoegen`.
2. Voer een geldige naam, leeftijd en bestaand elftal in.
3. Voer als positie `BestaatNiet` in.

**Verwacht resultaat:**
De speler wordt niet toegevoegd en het systeem toont `Positie bestaat niet`.

**Werkelijk resultaat:**
De speler wordt niet toegevoegd en het systeem toont `Positie bestaat niet`.

**Resultaat:** Geslaagd

---

## Testscenario 17 - Leeftijdscontrole zonder afwijkingen

**Doel:** Controleren of de volledige leeftijdscontrole werkt als alle spelers bij hun elftal passen.

**Stappen:**

1. Gebruik de standaard testdata.
2. Kies `Leeftijdscontrole`.

**Verwacht resultaat:**
Het systeem toont `Geen spelers met een te hoge leeftijd gevonden`.

**Werkelijk resultaat:**
Het systeem toont `Geen spelers met een te hoge leeftijd gevonden`.

**Resultaat:** Geslaagd

---

## Testscenario 18 - Leeftijdscontrole met afwijking

**Doel:** Controleren of de volledige leeftijdscontrole een te oude speler vindt.

**Preconditie:**
Er staat voor deze test een speler van 14 jaar in `JO13-1`.

**Stappen:**

1. Kies `Leeftijdscontrole`.
2. Bekijk het resultaat.

**Verwacht resultaat:**
De speler van 14 jaar in `JO13-1` wordt weergegeven als afwijking.

**Werkelijk resultaat:**
De speler van 14 jaar in `JO13-1` wordt weergegeven als afwijking.

**Resultaat:** Geslaagd

---

## Feedback klasgenoot

**Uitgevoerd scenario:** [invullen]

**Naam klasgenoot:** [invullen]

**Feedback:**
[invullen]

**Verwerking feedback:**
[invullen]

```