# Testresultaten: Verlanglijstmanager

* **Uitgevoerd op:** 23 oktober 2026
* **Door:** Jasper van Dis

## Bevindingen voor uitvoering

De tests zijn uitgevoerd op een versgeimporteerde database (via `db/creates.sql` en `db/inserts.sql`). De database werd voorbereid met standaard winkels en lijsten met respectievelijk standaard verzendkosten en budgetlimieten. Voor het testen van de toegangsbeveiliging (UC10) is een `.env`-bestand gebruikt met een geldige `TOEGANGSCODE_HASH`.

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
| TC12: Starten met correcte toegangscode (UC10) | Geslaagd |
| TC13: Starten met onjuiste toegangscode (UC10) | Geslaagd |
| TC14: Starten zonder TOEGANGSCODE_HASH in .env (UC10) | Geslaagd |

## Conclusie

14 van de 14 uitgevoerde testcases (UC1 t/m UC10) zijn geslaagd. De applicatie verwerkt alle onderdelen uit Increment 1, 2 en 3 correct: toegangscodecontrole via SHA-256 hashing en `.env`, itemtoevoeging, verwijdering, prijsaanpassingen, budgetgebaseerd zoeken, spaarplanberekening, het statistiekenoverzicht per lijst, de sessiestatistieken en de CSV-import.