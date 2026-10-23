# Testresultaten: Verlanglijstmanager

* **Uitgevoerd op:** 23 oktober 2026
* **Door:** Jasper van Dis

## Bevindingen voor uitvoering

De tests zijn uitgevoerd op een versgeimporteerde database (via `db/creates.sql` en `db/inserts.sql`). De database werd voorbereid met standaard winkels en lijsten met respectievelijk standaard verzendkosten en budgetlimieten.

## Resultaten

| Testcase | Resultaat |
|---|---|
| TC1: Voeg item toe (succesvol) | Geslaagd |
| TC2: Voeg item toe (winkel niet bestaand) | Geslaagd |
| TC3: Voeg item toe (lijst niet bestaand) | Geslaagd |
| TC4: Prijs aanpassen (succesvol) | Geslaagd |
| TC5: Item verwijderen (succesvol) | Geslaagd |
| TC6: Zoeken op budget | Geslaagd |
| TC7: Pas lijstbudget aan | Geslaagd |
| TC8: Persoonlijk spaarplan berekenen (UC6) | Geslaagd |
| TC9: Toon overzicht lijsten (UC7) | Geslaagd |
| TC10: Afsluiten en sessiestatistieken tonen (UC8) | Geslaagd |
| TC11: Import CSV items (UC9) | Geslaagd |

## Conclusie

11 van de 11 geteste testcases (UC1 t/m UC9) zijn geslaagd. De applicatie verwerkt itemtoevoeging, verwijdering, prijsaanpassingen, budgetgebaseerd zoeken, spaarplanberekening, het statistiekenoverzicht per lijst, de sessiestatistieken en de CSV-import inclusief het automatisch aanmaken van ontbrekende winkels en lijsten correct.