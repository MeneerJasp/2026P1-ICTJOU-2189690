```md
# Testrapport Elftalbeheer

## Testscenario 1 - Elftal en speler toevoegen

**Doel:** Controleren of een elftal en speler kunnen worden toegevoegd.

**Stappen:**

1. Voeg een nieuw elftal toe.
2. Voeg daarna een speler toe aan dit elftal.
3. Controleer de database.

**Verwacht resultaat:**
Het elftal en de speler worden opgeslagen in de database.

**Werkelijk resultaat:**
Het elftal en de speler zijn succesvol opgeslagen in de database.

**Resultaat:** Geslaagd

---

## Testscenario 2 - Speler zoeken op naam

**Doel:** Controleren of een speler op naam kan worden gevonden.

**Stappen:**

1. Zoek naar `Sem van Leeuwen`.
2. Bekijk het resultaat.

**Verwacht resultaat:**
De gegevens van `Sem van Leeuwen` worden getoond.

**Werkelijk resultaat:**
`Sem van Leeuwen` wordt getoond met elftal `JO13-1`, positie `keeper` en leeftijd `12`.

**Resultaat:** Geslaagd

---

## Testscenario 3 - Overzicht elftallen met spelers

**Doel:** Controleren of de elftallen met hun spelers worden weergegeven.

**Stappen:**

1. Open het overzicht van de elftallen.
2. Bekijk de weergegeven gegevens.

**Verwacht resultaat:**
De elftallen worden samen met hun spelers weergegeven.

**Werkelijk resultaat:**
Alle elftallen en bijbehorende spelers worden weergegeven.

**Resultaat:** Geslaagd

---

## Testscenario 4 - Leeftijdscontrole

**Doel:** Controleren of een te oude speler wordt tegengehouden.

**Stappen:**

1. Probeer een speler van 14 jaar toe te voegen aan `JO13-1`.
2. Bekijk het resultaat.

**Verwacht resultaat:**
De speler wordt niet toegevoegd.

**Werkelijk resultaat:**
De speler wordt niet toegevoegd en de melding `Speler is te oud voor dit elftal` wordt weergegeven.

**Resultaat:** Geslaagd

---

## Testscenario 5 - Speler verwijderen

**Doel:** Controleren of een bestaande speler kan worden verwijderd.

**Stappen:**

1. Verwijder `Sem van Leeuwen`.
2. Controleer de database.

**Verwacht resultaat:**
De speler wordt verwijderd uit de database.

**Werkelijk resultaat:**
De melding `Speler is verwijderd` wordt weergegeven en de speler staat niet meer in de database.

**Resultaat:** Geslaagd

---

## Testscenario 6 - Niet-bestaande speler verwijderen

**Doel:** Controleren wat er gebeurt als de speler niet bestaat.

**Stappen:**

1. Probeer `Bestaat Niet` te verwijderen.
2. Bekijk het resultaat.

**Verwacht resultaat:**
Er wordt geen speler verwijderd.

**Werkelijk resultaat:**
De melding `Speler niet gevonden` wordt weergegeven en de database blijft ongewijzigd.

**Resultaat:** Geslaagd

---

## Testscenario 7 - Sessiestatistieken tonen

**Doel:** Controleren of wijzigingen tijdens een sessie worden geteld.

**Stappen:**

1. Voeg één elftal toe.
2. Voeg één speler toe.
3. Verwijder één speler.
4. Sluit de applicatie af.

**Verwacht resultaat:**
De drie tellers staan allemaal op 1.

**Werkelijk resultaat:**
De applicatie toont:

`Elftallen toegevoegd: 1`

`Spelers toegevoegd: 1`

`Spelers verwijderd: 1`

**Resultaat:** Geslaagd

---

## Testscenario 8 - Sessiestatistieken zonder wijzigingen

**Doel:** Controleren of de tellers op 0 blijven als er geen wijzigingen zijn.

**Stappen:**

1. Start de applicatie.
2. Sluit de applicatie direct af.

**Verwacht resultaat:**
Alle tellers staan op 0.

**Werkelijk resultaat:**
De applicatie toont:

`Elftallen toegevoegd: 0`

`Spelers toegevoegd: 0`

`Spelers verwijderd: 0`

**Resultaat:** Geslaagd

---

## Testscenario 9 - Gemiddelde leeftijd per elftal

**Doel:** Controleren of het gemiddelde correct wordt berekend.

**Stappen:**

1. Gebruik een elftal met spelers van 14, 15 en 16 jaar.
2. Toon de gemiddelde leeftijd.

**Verwacht resultaat:**
De gemiddelde leeftijd is `15.0`.

**Werkelijk resultaat:**
De gemiddelde leeftijd wordt als `15.0` weergegeven.

**Resultaat:** Geslaagd

---

## Testscenario 10 - Gemiddelde leeftijd zonder spelers

**Doel:** Controleren wat er gebeurt bij een elftal zonder spelers.

**Stappen:**

1. Gebruik een elftal zonder spelers.
2. Toon de gemiddelde leeftijd.

**Verwacht resultaat:**
Het systeem toont `Geen spelers`.

**Werkelijk resultaat:**
Het systeem toont `Geen spelers`.

**Resultaat:** Geslaagd

---

# Conclusie

Alle testscenario's zijn geslaagd. De functies voor toevoegen, zoeken, verwijderen, leeftijdscontrole, sessiestatistieken en gemiddelde leeftijd werken volgens het verwachte gedrag.
```