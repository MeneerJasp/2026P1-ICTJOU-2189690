# Testplan: QuestComposer

## Testdoel

Dit testplan controleert niet alleen of functies technisch werken, maar vooral of QuestComposer het kernprobleem oplost: vroeg signaleren of scenario-ideeen financieel realistisch zijn. De testcases zijn daarom gericht op complete kosteninvoer, correcte budgetvergelijkingen en functies die misrekeningen in late bouwfasen helpen voorkomen.

## Voorbereiding

Voor alle testcases wordt de volgende voorbereiding verwacht:

* Zorg dat de juiste tabellen zijn aangemaakt in de database (`Onderdeel`, `Leverancier`, `Scenario`).
* Verwijder eventueel alle aanwezige data in de database.
* Zorg dat de database is voorbereid met `db/creates.sql`.
* Zorg dat minstens de volgende leveranciers aanwezig zijn: `EscapeParts`, `TechStage`, `PuzzelShop`.
* Zorg dat minstens de volgende scenario's aanwezig zijn: `Bankoverval`, `Labgeheim`, `Horrorzolder`.
* Zorg dat de databaseconnectie correct is ingevuld.

---

## UC1: Testen "Registreer nieuw puzzelonderdeel"

### Testscenario 1: Succesvolle toevoeging van onderdeel

**Precondities:**
* De applicatie is gestart.
* Leverancier `EscapeParts` bestaat.
* Er is minimaal een scenario beschikbaar, bijvoorbeeld `Bankoverval`.

**Testscenario:**
1. Kies in het menu voor optie 1.
2. Het systeem toont een lijst met beschikbare scenario's.
3. Kies scenario `Bankoverval`.
4. Voer in:
   * **Naam:** `Laserdoolhof`
   * **Prijs:** `120.00`
   * **Leverancier:** `EscapeParts`
   * **Prioriteit:** `1`

**Verwacht resultaat:**
* Het systeem toont een bevestiging.
* De sessieteller voor toegevoegde onderdelen wordt met 1 verhoogd.
* Het onderdeel staat in de database.

### Testscenario 2: Toevoegen met niet-bestaande leverancier

**Precondities:**
* De applicatie is gestart.
* Leverancier `OnbekendLab` bestaat niet.
* Er is minimaal een scenario beschikbaar.

**Testscenario:**
1. Kies in het menu voor optie 1.
2. Het systeem toont een lijst met beschikbare scenario's.
3. Kies een geldig scenario.
4. Voer in:
   * **Naam:** `Testonderdeel`
   * **Prijs:** `50.00`
   * **Leverancier:** `OnbekendLab`

**Verwacht resultaat:**
* Het systeem toont dat de leverancier niet bestaat.
* Er wordt geen onderdeel toegevoegd.

### Testscenario 3: Toevoegen met ongeldig scenario-keuzenummer

**Precondities:**
* De applicatie is gestart.
* Er is minimaal een scenario beschikbaar.

**Testscenario:**
1. Kies in het menu voor optie 1.
2. Het systeem toont een lijst met beschikbare scenario's.
3. Voer een ongeldig keuzenummer in, bijvoorbeeld `9999`.

**Verwacht resultaat:**
* Het systeem toont: `Ongeldige keuze.`
* De use case stopt direct.
* Er wordt geen onderdeel toegevoegd.

### Testscenario 4: Prioriteitscorrectie buiten bereik 1-3

**Precondities:**
* De applicatie is gestart.
* Leverancier en scenario's bestaan.

**Testscenario:**
1. Kies in het menu voor optie 1.
2. Het systeem toont een lijst met beschikbare scenario's.
3. Kies een geldig scenario.
4. Voer prioriteit `7` in.

**Verwacht resultaat:**
* Het systeem corrigeert prioriteit naar geldige waarde (3).
* Het onderdeel wordt toegevoegd met gecorrigeerde prioriteit.

---

## UC2: Testen "Herbereken kostprijs van onderdeel"
[Schrijf testscenario's voor deze use case, inclusief precondities, teststappen en verwachte resultaten.]

## UC3: Testen "Stel scenariobudget bij"

### Testscenario 1: Succesvolle budgetaanpassing

**Precondities:**
* Scenario `Bankoverval` bestaat met budget 200.

**Testscenario:**
1. Kies optie 4.
2. Kies scenario `Bankoverval`.
3. Voer nieuw budget `450` in.

**Verwacht resultaat:**
* Het budget wordt aangepast in de database.
* Het systeem toont bevestiging.

### Testscenario 2: Budgetaanpassing zonder beschikbare scenario's

**Precondities:**
* Er zijn geen scenario's aanwezig in de database.

**Testscenario:**
1. Kies optie 4.

**Verwacht resultaat:**
* Het systeem toont dat er geen scenario's beschikbaar zijn.
* De use case stopt direct.

---

## UC4: Testen "Schrap onderdeel uit build"

### Testscenario 1: Succesvolle verwijdering

**Precondities:**
* Er staat minimaal een onderdeel in minimaal twee scenario's.

**Testscenario:**
1. Kies optie 3.
2. Het systeem toont een lijst met beschikbare scenario's.
3. Kies een scenario, bijvoorbeeld `Bankoverval`.
4. Het systeem toont een genummerde onderdelenlijst uit dat scenario.
5. Kies een bestaand onderdeelnummer.

**Verwacht resultaat:**
* Het onderdeel wordt verwijderd.
* De sessieteller voor verwijderde onderdelen wordt met 1 verhoogd.

### Testscenario 2: Verwijdering met ongeldig nummer

**Precondities:**
* De applicatie is gestart.
* Er is minimaal een scenario beschikbaar.

**Testscenario:**
1. Kies optie 3.
2. Het systeem toont een lijst met beschikbare scenario's.
3. Kies een geldig scenario.
4. Voer ongeldig nummer `9999` in.

**Verwacht resultaat:**
* Het systeem toont `Ongeldige keuze.`
* Er wordt geen onderdeel verwijderd.

---

## UC5: Testen "Zoek alternatieven binnen restbudget"

### Testscenario 1: Zoeken met resultaten

**Precondities:**
* Er zijn onderdelen met prijzen tussen 20 en 60 euro.

**Testscenario:**
1. Kies optie 5.
2. Voer grenzen `20` en `60` in.

**Verwacht resultaat:**
* Het systeem toont onderdelen in die range.

### Testscenario 2: Zoeken zonder resultaten

**Precondities:**
* Er zijn geen onderdelen tussen 500 en 1000 euro.

**Testscenario:**
1. Kies optie 5.
2. Voer `500` en `1000` in.

**Verwacht resultaat:**
* Het systeem meldt dat er geen onderdelen binnen het opgegeven budgetbereik zijn.

### Testscenario 3: Automatische bepaling van grenzen

**Precondities:**
* De applicatie is gestart.

**Testscenario:**
1. Kies optie 5.
2. Voer `100` en `40` in.

**Verwacht resultaat:**
* Het systeem bepaalt automatisch minimum 40 en maximum 100.
* De zoekresultaten zijn gelijk aan zoeken met grenzen `40` en `100`.

---

## UC6: Testen "Maak inkoopritme voor sleutelonderdeel"

### Testscenario 1: Inkoopritme voor sleutelonderdeel

**Precondities:**
* Er staat minimaal een onderdeel in de database.

**Testscenario:**
1. Kies optie 6.
2. Kies een onderdeel.
3. Voer `3` maanden in.

**Verwacht resultaat:**
* Het systeem toont per maand het cumulatieve opgebouwde budget.

### Testscenario 2: Inkoopritme zonder beschikbare onderdelen

**Precondities:**
* Er zijn geen onderdelen aanwezig in de database.

**Testscenario:**
1. Kies optie 6.

**Verwacht resultaat:**
* Het systeem toont dat er geen onderdelen beschikbaar zijn.
* De use case stopt direct.

### Testscenario 3: Inkoopritme met ongeldig onderdeelnummer

**Precondities:**
* Er staat minimaal een onderdeel in de database.

**Testscenario:**
1. Kies optie 6.
2. Voer onderdeelnummer `9999` in.

**Verwacht resultaat:**
* Het systeem toont `Ongeldige keuze.`
* De use case stopt direct.

---

## UC7: Testen "Toon haalbaarheidsoverzicht per scenario"

### Testscenario 1: Overzicht van scenario's met statistieken

**Precondities:**
* De applicatie is gestart.
* In de database zijn meerdere scenario's aanwezig met onderdelen.
* Scenario's hebben verschillende budgetstatussen.

**Testscenario:**
1. Kies optie 7.

**Verwacht resultaat:**
* Het systeem toont per scenario:
  - scenarionaam
  - aantal onderdelen
  - goedkoopste onderdeel
  - duurste onderdeel
  - gemiddelde onderdeelprijs
  - totaalbedrag inclusief transportkosten
  - scenariobudget
  - waarschuwing als het totaalbedrag hoger is dan het budget

### Testscenario 2: Overzicht met leeg scenario

**Precondities:**
* Minstens een scenario bestaat zonder onderdelen.

**Testscenario:**
1. Kies optie 7.

**Verwacht resultaat:**
* Voor het lege scenario toont het systeem:
  - scenarionaam
  - `Aantal onderdelen: 0`
  - `Nog geen onderdelen in dit scenario.`
  - budget
* Er verschijnt geen budgetoverschrijdingswaarschuwing voor het lege scenario.

---

## UC8: Testen "Sluit ontwerpsessie af"

### Testscenario 1: Sessiestatistieken bij afsluiten

**Precondities:**
* Tijdens de sessie zijn onderdelen toegevoegd en/of verwijderd.

**Testscenario:**
1. Kies optie 8.

**Verwacht resultaat:**
* Het systeem toont afsluitbericht.
* Het systeem toont statistieken toegevoegd/verwijderd.
* Het programma stopt.

---

## UC9: Testen "Importeer intakebestand uit CSV"

### Testscenario 1: Succesvolle import van CSV-bestand

**Precondities:**
* De applicatie is gestart.
* Een geldig CSV-bestand `data/items.csv` bestaat met kolommen `titel`, `prijs`, `leverancier`, `scenario`, `prioriteit`.

**Testscenario:**
1. Kies in het menu voor optie 9.
2. Voer `data/items.csv` in.

**Verwacht resultaat:**
* Het systeem leest regel voor regel in.
* Het systeem meldt succesvolle import.
* Alle onderdelen uit het bestand zijn opgeslagen.
* Ontbrekende leveranciers en scenario's worden automatisch aangemaakt.

### Testscenario 2: Import met bestandsnaam korter dan 4 tekens

**Precondities:**
* De applicatie is gestart.

**Testscenario:**
1. Kies in het menu voor optie 9.
2. Voer `abc` in.

**Verwacht resultaat:**
* Het systeem meldt ongeldige bestandsnaam.
* Import wordt afgebroken.

### Testscenario 3: Import met niet-bestaand bestand

**Precondities:**
* De applicatie is gestart.
* Het bestand `data/bestaatniet.csv` bestaat niet.

**Testscenario:**
1. Kies in het menu voor optie 9.
2. Voer `data/bestaatniet.csv` in.

**Verwacht resultaat:**
* Het systeem toont `Bestand niet gevonden.`
* Import wordt afgebroken.

### Testscenario 4: Import met automatisch aanmaken van leverancier en scenario

**Precondities:**
* CSV bevat ten minste een nieuwe leverancier en een nieuw scenario.

**Testscenario:**
1. Kies in het menu voor optie 9.
2. Importeer een bestand met onbekende stamdata.

**Verwacht resultaat:**
* Nieuwe leverancier wordt aangemaakt met transportkosten 0.00.
* Nieuw scenario wordt aangemaakt met budget 100.00.
* Onderdelen worden opgeslagen.

---

## UC10: Testen "Applicatie starten met toegangscode"

### Testscenario 1: Starten met correcte toegangscode

**Precondities:**
* In `.env` staat een geldige hash bij `TOEGANGSCODE_HASH`.

**Testscenario:**
1. Start de applicatie.
2. Voer de juiste toegangscode in.

**Verwacht resultaat:**
* Het systeem accepteert de toegangscode.
* Het hoofdmenu wordt getoond.

### Testscenario 2: Starten met onjuiste toegangscode

**Precondities:**
* In `.env` staat een geldige hash bij `TOEGANGSCODE_HASH`.

**Testscenario:**
1. Start de applicatie.
2. Voer een onjuiste toegangscode in.

**Verwacht resultaat:**
* Het systeem toont `FOUT: Onjuiste toegangscode.`
* De applicatie stopt zonder het hoofdmenu te tonen.

### Testscenario 3: Starten zonder TOEGANGSCODE_HASH in `.env`

**Precondities:**
* Het `.env`-bestand ontbreekt of bevat geen `TOEGANGSCODE_HASH`.

**Testscenario:**
1. Start de applicatie.

**Verwacht resultaat:**
* Het systeem toont `FOUT: TOEGANGSCODE_HASH ontbreekt in .env.`
* De applicatie stopt zonder het hoofdmenu te tonen.
