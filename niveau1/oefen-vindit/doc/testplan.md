# Testplan: Vind it! Verkoopmanager

## Voorbereiding

Voor alle testcases wordt de volgende voorbereiding verwacht:

* Zorg dat de juiste tabellen zijn aangemaakt in de database (`verkoop`).
* Verwijder eventueel alle aanwezige data in de database.
* Zorg dat de standaard testdata (`inserts.sql`) is ingeladen in de MariaDB-omgeving.

---

## Testen: "Toon alle verkopen"

### Testscenario
1. Start de applicatie.
2. Kies in het menu voor optie 1.

### Verwacht resultaat
Er verschijnt een lijst met alle verkopen uit de database. Deze ziet er als volgt uit:

**Eerste regels:**
```text
2026-03-02 10:15:00  -  kleding  -  15.00 euro
2026-03-04 14:30:00  -  boeken   -  7.50 euro
2026-03-06 11:05:00  -  kleding  -  22.50 euro
```

**Laatste regels:**
```text
2026-05-14 09:55:00  -  kleding  -  12.00 euro
2026-05-18 16:20:00  -  boeken   -  18.50 euro
2026-05-22 13:35:00  -  overige  -  5.00 euro
```

---

## Testen: "Toon alle kleding-verkopen"

### Testscenario
1. Start de applicatie.
2. Kies in het menu voor optie 2.

### Verwacht resultaat
Er verschijnt een gefilterde lijst met uitsluitend verkopen waarbij de categorie 'kleding' is:
```text
2026-03-02 10:15:00  -  kleding  -  15.00 euro
2026-03-06 11:05:00  -  kleding  -  22.50 euro
2026-03-12 15:50:00  -  kleding  -  10.00 euro
2026-05-14 09:55:00  -  kleding  -  12.00 euro
```

---

## Testen: "Toon alle boeken-verkopen"

### Testscenario
1. Start de applicatie.
2. Kies in het menu voor optie 3.

### Verwacht resultaat
Er verschijnt een gefilterde lijst met uitsluitend verkopen waarbij de categorie 'boeken' is:
```text
2026-03-04 14:30:00  -  boeken  -  7.50 euro
2026-03-09 10:10:00  -  boeken  -  12.50 euro
2026-05-18 16:20:00  -  boeken  -  18.50 euro
```

---

## Testen: "Toon alle overige verkopen"

### Testscenario
1. Start de applicatie.
2. Kies in het menu voor optie 4.

### Verwacht resultaat
Er verschijnt een lijst met verkopen die NIET onder 'kleding' of 'boeken' vallen:
```text
2026-03-15 12:00:00  -  elektronica  -  45.00 euro
2026-04-14 16:40:00  -  games        -  12.50 euro
2026-05-22 13:35:00  -  overige      -  5.00 euro
```

---

## Testen: "Totale opbrengst tonen"

### Testscenario
1. Start de applicatie.
2. Kies in het menu voor optie 6.

### Verwacht resultaat
Het systeem berekent de som van alle opbrengsten en toont dit in euro's.
**Melding:** `Totale opbrengst: € 235,50` (afhankelijk van de gebruikte testdata).

---

## Testen: "Toon alle gebruikte categorieen"

### Testscenario
1. Start de applicatie.
2. Kies in het menu voor optie 7.

### Verwacht resultaat
Er verschijnt een lijst met elke gebruikte categorie precies een keer. Deze ziet er als volgt uit:

```text
boeken
elektronica
games
kleding
overige
```

---

## Testen: "Nieuwe verkoop toevoegen"

*Let op: Het uitvoeren van deze test wijzigt de database en beïnvloedt dus de resultaten van de andere tests!*

### Testscenario
1. Start de applicatie.
2. Kies in het menu voor optie 5.
3. Voer de volgende gegevens in:
   * **Datum:** `2026-09-13`
   * **Tijd:** `15:45:55`
   * **Categorie:** `sneakers`
   * **Opbrengst (in centen):** `12050`

### Verwacht resultaat
* Het systeem geeft de melding: `Verkoop succesvol toegevoegd aan Vind it!`
* In de database is een nieuwe record te vinden met `verkoopmoment = '2026-09-13 15:45:55'`, `categorie = 'sneakers'` en `opbrengst = 12050`.