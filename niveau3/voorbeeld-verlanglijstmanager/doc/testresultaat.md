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
| TC6: Zoeken op budget | Nog niet getest |
| TC7: Pas lijstbudget aan | Geslaagd |
| TC8: Toon volledige verlanglijst | Nog niet getest |
| TC9: Toon overzicht lijsten | Nog niet getest |
| TC10: Import CSV items | Nog niet getest |

## Conclusie

6 van de 6 uitgevoerde testcases voor Use Case 1 t/m 4 zijn geslaagd. De applicatie verwerkt het toevoegen van items, het aanpassen van itemprijzen, het aanpassen van het lijstbudget en het verwijderen van items correct.