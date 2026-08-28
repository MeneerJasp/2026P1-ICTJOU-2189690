# Testplan: Verlanglijstmanager

## Voorbereiding

Voor alle testcases wordt de volgende voorbereiding verwacht:

* Zorg dat de juiste tabellen zijn aangemaakt in de database (`Item`, `Winkel`, `Lijst`).
* Verwijder eventueel alle aanwezige data in de database.
* Zorg dat de standaard testdata is ingeladen met [ICTJOU-n3-verlanglijstmanager/db/creates.sql](ICTJOU-n3-verlanglijstmanager/db/creates.sql).
* Zorg dat minstens de volgende winkels aanwezig zijn: `MediaMarkt`, `Bol.com`, `Coolblue`.
* Zorg dat minstens de volgende lijsten aanwezig zijn: `Elektronica`, `Studie`, `Sport`.
* Zorg dat de databaseconnectie correct is ingevuld.

---

## UC1: Testen "Voeg item toe aan verlanglijst"

### Testscenario 1: Succesvolle toevoeging van item

**Precondities:**
* De applicatie is gestart.
* De winkel `MediaMarkt` bestaat in de database.
* Er is minimaal één verlanglijst aanwezig in de database, bijvoorbeeld `Elektronica`.

**Testscenario:**
1. Start de applicatie.
3. Kies in het menu voor optie 1 ("Voeg item toe aan verlanglijst").
3. Het systeem toont een lijst met verlanglijsten.
4. Kies verlanglijst `Elektronica`.
5. Voer in:
   * **Naam:** `Wireless Koptelefoon`
   * **Prijs:** `79.99`
   * **Winkel:** `MediaMarkt`
   * **Prioriteit:** `2`

**Verwacht resultaat:**
* Het systeem toont een bevestiging: `Item succesvol toegevoegd!`
* Het systeem verhoogt de sessieteller voor toegevoegde items met 1.
* In de database staat een nieuw item met bovengenoemde gegevens.

---

### Testscenario 2: Toevoegen met niet-bestaande winkel

**Precondities:**
* De applicatie is gestart.
* De winkel `OnduidelijkeWinkel` bestaat niet in de database.
* Er is minimaal één verlanglijst aanwezig in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 1 ("Voeg item toe aan verlanglijst").
3. Het systeem toont een lijst met verlanglijsten.
4. Kies een geldige verlanglijst.
5. Voer in:
   * **Naam:** `Test Item`
   * **Prijs:** `50.00`
   * **Winkel:** `OnduidelijkeWinkel`

**Verwacht resultaat:**
* Het systeem toont: `Fout: Winkel 'OnduidelijkeWinkel' bestaat niet in de database.`
* De use case stopt direct.
* Er wordt geen item toegevoegd.

---

### Testscenario 3: Toevoegen met niet-bestaande lijst

**Precondities:**
* De applicatie is gestart.
* De winkel `MediaMarkt` bestaat in de database.
* Er bestaat geen extra handmatige lijstkeuze; de gebruiker kiest uit de door het systeem getoonde verlanglijsten.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 1 ("Voeg item toe aan verlanglijst").
3. Het systeem toont een lijst met verlanglijsten.
4. Voer een ongeldig keuzenummer in, bijvoorbeeld `9999`.

**Verwacht resultaat:**
* Het systeem toont: `Ongeldige keuze.`
* De use case stopt direct.
* Er wordt geen item toegevoegd.

---

### Testscenario 4: Prioriteitscorrectie buiten bereik 1-3

**Precondities:**
* De applicatie is gestart.
* De winkel `MediaMarkt` bestaat in de database.
* De lijst `Studie` bestaat in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 1 ("Voeg item toe aan verlanglijst").
3. Het systeem toont een lijst met verlanglijsten.
4. Kies verlanglijst `Studie`.
5. Voer in:
   * **Naam:** `Boek over AI`
   * **Prijs:** `35.00`
   * **Winkel:** `MediaMarkt`
   * **Prioriteit:** `5` (buiten bereik)

**Verwacht resultaat:**
* Het systeem corrigeert prioriteit automatisch (bijv. naar 3, de hoogste geldige waarde).
* Het item wordt succesvol toegevoegd met de gecorrigeerde prioriteit.

---

## UC2: Testen "Pas item prijs aan"

[Opstellen testscenario's voor UC2]

---

## UC3: Testen "Pas lijstbudget aan"

### Testscenario 1: Succesvolle budgetaanpassing

**Precondities:**
* De applicatie is gestart.
* De lijst `Elektronica` bestaat en heeft een huidig budget van €200.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 4 ("Pas lijstbudget aan").
3. Het systeem toont een overzicht van alle lijsten en hun huidige budget.
4. Voer in:
   * **Lijst:** `Elektronica`
   * **Nieuw budget:** `500`

**Verwacht resultaat:**
* Het systeem toont: `Lijstbudget succesvol bijgewerkt!`
* In de database is het budget van de lijst bijgewerkt naar €500.

---

### Testscenario 2: Budgetaanpassing zonder beschikbare lijsten

**Precondities:**
* De applicatie is gestart.
* ALLE lijsten zijn verwijderd uit de database (geen Elektronica, Studie, Sport meer).

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 4 ("Pas lijstbudget aan").

**Verwacht resultaat:**
* Het systeem toont: `Fout: Er zijn geen lijsten beschikbaar.`
* De use case stopt direct.

---

## UC4: Testen "Verwijder item"

### Testscenario 1: Succesvolle verwijdering van item

**Precondities:**
* De applicatie is gestart.
* Er staan items in minimaal twee verlanglijsten.

**Testscenario:**
1. Start de applicatie.
3. Kies in het menu voor optie 3 ("Verwijder item").
3. Het systeem toont eerst een lijst met verlanglijsten.
4. Kies een verlanglijst, bijvoorbeeld `Studie`.
5. Het systeem toont een genummerde lijst met items uit die verlanglijst.
6. Voer in:
   * **Keuzenummer:** `1`

**Verwacht resultaat:**
* Het systeem toont: `Item succesvol verwijderd!`
* De sessieteller voor verwijderde items wordt met 1 verhoogd.
* Het gekozen item is uit de database verwijderd.

---

### Testscenario 2: Verwijdering met ongeldig ID

**Precondities:**
* De applicatie is gestart.
* Er is minimaal één verlanglijst aanwezig.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 3 ("Verwijder item").
3. Het systeem toont eerst een lijst met verlanglijsten.
4. Kies een geldige verlanglijst.
5. Voer in:
   * **Keuzenummer:** `9999` (bestaat niet)

**Verwacht resultaat:**
* Het systeem toont: `Ongeldige keuze.`
* De verwijdering wordt geannuleerd.
* De sessieteller voor verwijderde items wordt niet verhoogd.

---

## UC5: Testen "Zoek items op budget"

### Testscenario 1: Zoeken met resultaten

**Precondities:**
* De applicatie is gestart.
* In de database zijn items opgeslagen met verschillende prijzen, bijvoorbeeld:
  * Item 1: €30.00 (Elektronica)
  * Item 2: €50.00 (Studie)
  * Item 3: €75.00 (Sport)
  * Item 4: €150.00 (Elektronica)

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 5 ("Zoek items op budget").
3. Voer in:
   * **Eerste budgetgrens:** `40`
   * **Tweede budgetgrens:** `100`

**Verwacht resultaat:**
* Het systeem bepaalt automatisch de laagste (€40) en hoogste (€100) grens.
* Het systeem toont de items: €50.00 en €75.00.
* De lijst bevat de namen en prijzen van de gevonden items.

---

### Testscenario 2: Zoeken zonder resultaten

**Precondities:**
* De applicatie is gestart.
* De database bevat GEEN items tussen €500 en €1000.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 5 ("Zoek items op budget").
3. Voer in:
   * **Eerste budgetgrens:** `500`
   * **Tweede budgetgrens:** `1000`

**Verwacht resultaat:**
* Het systeem toont `Items tussen €500.0 en €1000.0:` zonder itemregels daaronder.

---

### Testscenario 3: Automatische bepaling van grenzen

**Precondities:**
* De applicatie is gestart.
* In de database zijn items met verschillende prijzen opgeslagen.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 5 ("Zoek items op budget").
3. Voer in:
   * **Eerste budgetgrens:** `100`
   * **Tweede budgetgrens:** `40` (omgekeerde volgorde)

**Verwacht resultaat:**
* Het systeem bepaalt automatisch dat de laagste grens €40 en de hoogste €100 moet zijn.
* De zoekresultaten zijn correct en identiek aan Testscenario 1.

---

### Testscenario 4: Zoeken buiten bereik

**Precondities:**
* De applicatie is gestart.
* De database bevat items, maar GEEN items tussen €500 en €1000.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 5 ("Zoek items op budget").
3. Voer in:
   * **Eerste budgetgrens:** `500`
   * **Tweede budgetgrens:** `1000`

**Verwacht resultaat:**
* Het systeem toont `Items tussen €500.0 en €1000.0:` zonder itemregels daaronder.

---

## UC6: Testen "Persoonlijk spaarplan berekenen"

### Testscenario 1: Spaarplan berekenen voor item

**Precondities:**
* De applicatie is gestart.
* In de database zijn items opgeslagen, bijvoorbeeld:
  * [Elektronica] Bluetooth speaker - €45.00
  * [Studie] Boek over Python - €35.00
  * [Sport] Tennisracket - €60.00

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 6 ("Persoonlijk spaarplan berekenen").
3. Het systeem toont een genummerde lijst van alle items.
4. Voer in:
   * **Item nummer:** `1` (selecteer Bluetooth speaker - €45.00)
   * **Aantal maanden:** `3`

**Verwacht resultaat:**
* Het systeem berekent het cumulatieve spaarbedrag per maand: €45 / 3 maanden = €15/maand.
* Het systeem toont:
  ```
  Spaarplan voor Bluetooth speaker (Elektronica):
  Maand 1: Totaal gespaard: €15.0
  Maand 2: Totaal gespaard: €30.0
  Maand 3: Totaal gespaard: €45.0
  ```

---

### Testscenario 2: Spaarplan zonder beschikbare items

**Precondities:**
* De applicatie is gestart.
* Er zijn GEEN items in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 6 ("Persoonlijk spaarplan berekenen").

**Verwacht resultaat:**
* Het systeem toont: `Fout: Er zijn geen items beschikbaar.`
* De use case stopt direct.

---

### Testscenario 3: Spaarplan met ongeldig itemnummer

**Precondities:**
* De applicatie is gestart.
* De database bevat items.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 6 ("Persoonlijk spaarplan berekenen").
3. Het systeem toont een genummerde lijst van alle items.
4. Voer in:
   * **Item nummer:** `9999` (bestaat niet)

**Verwacht resultaat:**
* Het systeem toont: `Ongeldige keuze.`
* De use case stopt direct.

---

## UC7: Testen "Uitgaven per lijst inzien"

### Testscenario 1: Overzicht van alle lijsten met statistieken

**Precondities:**
* De applicatie is gestart.
* In de database zijn meerdere lijsten aanwezig met items.
* Lijsten hebben verschillende budgetstatussen (onder/over budget).

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 7 ("Uitgaven per lijst inzien").

**Verwacht resultaat:**
* Het systeem toont voor elke lijst een overzicht met:
  - Lijstnaam (duidelijk zichtbaar)
  - Aantal items in de lijst
  - Goedkoopste item (prijs)
  - Duurste item (prijs)
  - Gemiddelde itemprijs
  - Totaalbedrag (prijs + verzendkosten van alle items)
  - Ingestelde budget
  - Waarschuwing (in rood) als totaalbedrag > budget
* Alle lijsten worden opeenvolgend getoond.

---

### Testscenario 2: Overzicht zonder items in een lijst

**Precondities:**
* De applicatie is gestart.
* Minstens één lijst bestaat zonder items.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 7 ("Uitgaven per lijst inzien").

**Verwacht resultaat:**
* Voor de lege lijst toont het systeem:
  - Lijstnaam
  - "Aantal items: 0"
  - "Nog geen items in deze lijst."
  - Ingestelde budget
  - Geen waarschuwing over budgetoverschrijding
* Andere lijsten met items worden normaal getoond.

---

## UC8: Testen "Afsluiten"

### Testscenario 1: Sessiestatistieken bij afsluiten

**Precondities:**
* De applicatie is gestart.
* Tijdens deze sessie zijn items toegevoegd en/of verwijderd.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 1 ("Voeg item toe aan verlanglijst").
3. Verwijder een item (via UC4).
4. Kies in het menu voor optie 8 ("Afsluiten").

**Verwacht resultaat:**
* Het systeem toont een afscheidsgroet.
* Het systeem toont de sessiestatistieken:
  ```
  Sessiestatistieken:
  Items toegevoegd: 1
  Items verwijderd: 1
  ```
* Het programma stopt.

---

## UC9: Testen "Items importeren uit CSV"

### Testscenario 1: Succesvolle import van CSV-bestand

**Precondities:**
* De applicatie is gestart.
* Een geldig CSV-bestand `data/items.csv` bestaat met kolommen: `titel`, `prijs`, `winkel`, `lijst`, `prioriteit`.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 9 ("Importeer items uit CSV").
3. Voer in:
   * **Bestandsnaam:** `data/items.csv`

**Verwacht resultaat:**
* Het systeem leest het bestand regel voor regel.
* Het systeem toont een bevestiging: `CSV succesvol geïmporteerd!`
* Alle items uit het bestand zijn in de database opgeslagen.
* Tijdens de import worden ontbrekende winkels en lijsten automatisch toegevoegd.

---

### Testscenario 2: Import met bestandsnaam korter dan 4 tekens

**Precondities:**
* De applicatie is gestart.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 9 ("Importeer items uit CSV").
3. Voer in:
   * **Bestandsnaam:** `abc`

**Verwacht resultaat:**
* Het systeem toont: `Ongeldige bestandsnaam.`
* De import wordt geannuleerd.

---

### Testscenario 3: Import met automatisch aanmaken van winkel en lijst

**Precondities:**
* De applicatie is gestart.
* Een CSV-bestand `special_items.csv` bevat items met:
  * **Nieuwe winkel:** `AmazonNL` (bestaat NIET in database)
  * **Nieuwe lijst:** `Gadgets` (bestaat NIET in database)
  * **Bestaande winkel:** `MediaMarkt` (bestaat WEL in database)
  * **Bestaande lijst:** `Elektronica` (bestaat WEL in database)

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 9 ("Importeer items uit CSV").
3. Voer in:
   * **Bestandsnaam:** `special_items.csv`

**Verwacht resultaat:**
* Het systeem leest het CSV-bestand.
* Het systeem maakt automatisch aan:
  * Winkel `AmazonNL` met standaardwaarden (Verzendkosten: €0.00)
  * Lijst `Gadgets` met standaardwaarden (Budget: €100.00)
* Het systeem voegt alle items toe aan de database.
* Het systeem toont: `CSV succesvol geïmporteerd!`
* Alle winkels en lijsten staan in de database.

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

---

### Testscenario 2: Starten met onjuiste toegangscode

**Precondities:**
* In `.env` staat een geldige hash bij `TOEGANGSCODE_HASH`.

**Testscenario:**
1. Start de applicatie.
2. Voer een onjuiste toegangscode in.

**Verwacht resultaat:**
* Het systeem toont `FOUT: Onjuiste toegangscode.`
* De applicatie stopt zonder het hoofdmenu te tonen.

---

### Testscenario 3: Starten zonder TOEGANGSCODE_HASH in `.env`

**Precondities:**
* Het `.env`-bestand ontbreekt of bevat geen `TOEGANGSCODE_HASH`.

**Testscenario:**
1. Start de applicatie.

**Verwacht resultaat:**
* Het systeem toont `FOUT: TOEGANGSCODE_HASH ontbreekt in .env.`
* De applicatie stopt zonder het hoofdmenu te tonen.
