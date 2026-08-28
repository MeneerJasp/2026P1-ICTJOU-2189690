# Testresultaten: QuestComposer

* **Uitgevoerd op:** 13 mei 2026
* **Door:** Docenten

## Bevindingen voor uitvoering

De tests zijn uitgevoerd op een vers geinitialiseerde SQLite-database via `db/creates.sql`. De database is voorbereid met basisleveranciers en basisscenario's met standaard transportkosten en budgetlimieten. Daarnaast is een tijdelijk `.env`-bestand gebruikt met een geldige `TOEGANGSCODE_HASH` voor de toegangscodecontrole.

## Resultaten

| Testcase | Resultaat |
|---|---|
| TC1: Voeg onderdeel toe (succesvol) | Geslaagd |
| TC2: Voeg onderdeel toe (leverancier niet bestaand) | Geslaagd |
| TC3: Voeg onderdeel toe (scenario niet bestaand) | Geslaagd |
| TC4: Prijs aanpassen (succesvol) | Geslaagd |
| TC5: Onderdeel verwijderen (succesvol) | Geslaagd |
| TC6: Zoeken op budget | Geslaagd |
| TC7: Stel scenariobudget bij | Geslaagd |
| TC8: Toon volledige onderdelenlijst | Geslaagd |
| TC9: Toon overzicht per scenario | Geslaagd |
| TC10: Import CSV onderdelen | Geslaagd |
| TC11: Import met ongeldige bestandsnaam | Geslaagd |
| TC12: Prijs aanpassen met ongeldige keuze | Geslaagd |
| TC13: Onderdeel verwijderen met ongeldige keuze | Geslaagd |
| TC14: Inkoopritme voor sleutelonderdeel | Geslaagd |
| TC15: Afsluiten met sessiestatistieken | Geslaagd |
| TC16: Starten met onjuiste toegangscode | Geslaagd |
| TC17: Starten zonder `TOEGANGSCODE_HASH` | Geslaagd |

## Opmerkingen

* De functionele scenario's zijn inhoudelijk allemaal geslaagd.
* Bij geautomatiseerde CLI-tests met bewust afgekorte invoer ontstaat na sommige foutpaden een `EOFError`, omdat de applicatie na de fout netjes terugkeert naar het menu en vervolgens geen extra invoer meer ontvangt. Dit is geen fout in normaal interactief gebruik.
* Tijdens de CSV-import zijn nieuwe leveranciers en scenario's uit [data/items.csv](c:/Users/jsno/Documents/GitHub/ICTJOU-ICTORG-2627/ICTJOU-n3-questcomposer/data/items.csv) correct aangemaakt met standaardwaarden.

## Conclusie

17 van de 17 uitgevoerde testcases zijn geslaagd. De applicatie verwerkt de volledige kernset correct: toegangscodecontrole, registratie en verwijdering van puzzelonderdelen, kostprijsaanpassingen, zoeken binnen budget, intake-import, scenario-budgetbeheer, haalbaarheidsoverzicht, inkoopritme en sessiestatistieken bij afsluiten.
