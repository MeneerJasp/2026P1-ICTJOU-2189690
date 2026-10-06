# Analyse QuestComposer

## Inleiding

In dit document worden de functionele en non-functionele eisen van de applicatie "QuestComposer" beschreven. Deze applicatie is bedoeld voor studenten en beginnende ontwerpers die escaperoom-scenario's willen produceren met intake, leveranciersafstemming, urgentiebepaling en haalbaarheidschecks. De focus ligt op operationeel overzicht, datakwaliteit en budgetinzichten.

De kern van het probleem is dat creatieve ideeen in ontwerpfases vaak sneller groeien dan de financiele en logistieke realiteit. Teams ontdekken daardoor soms te laat dat een scenario niet haalbaar is binnen het beschikbare budget of de planning. QuestComposer moet dit voorkomen door vroeg in het proces inzicht te geven in complete kosten, leveranciersafhankelijkheden en budgetoverschrijdingen per scenario.

## Analyse-start increment 1

Voor de eerste versie kiezen we de handelingen die nodig zijn om de onderdelen en het budget van een bestaand scenario bij te houden. Een ontwerper kan een onderdeel toevoegen, de prijs bijwerken, het scenariobudget bijstellen en een onderdeel verwijderen. Daarbij zijn consistente scenario- en leveranciersnamen belangrijk voor betrouwbare gegevens. Het menu moet duidelijk genoeg zijn om deze handelingen zonder kennis van de opslag te gebruiken.

Voor increment 1 zijn C1 (consistente scenario- en leveranciersnamen), C5 (een duidelijk menu) en C8 (kunnen werken via de terminal) de drie belangrijkste user concerns. De beveiliging met toegangscode uit C2, C3 en C4 hoort bij increment 3.

De prioriteit 1-3 voor onderdelen staat bij US5 als Should. De gegeven UC1 vraagt tijdens het toevoegen al om een prioriteit. Dit verschil moet nog met de docent worden afgestemd. Het uitgebreide haalbaarheidsoverzicht, transportkosten, zoeken en inkoopritme staan bij increment 2. CSV-import en de toegangscode staan bij increment 3. Deze afbakening is een eerste analyse op basis van het interview en de gegeven Use Cases.

### User stories

| User Story | Prioriteit | Increment |
|---|---|---:|
| **US1.** Als ontwerper wil ik een puzzelonderdeel aan een scenario kunnen toevoegen, zodat ik alle onderdelen per scenario kan bijhouden. | Must | 1 |
| **US2.** Als ontwerper wil ik de prijs van een puzzelonderdeel kunnen aanpassen, zodat ik met actuele kosten werk. | Must | 1 |
| **US3.** Als ontwerper wil ik het budget van een scenario kunnen aanpassen, zodat het budget aansluit bij de gemaakte afspraken. | Must | 1 |
| **US4.** Als ontwerper wil ik een puzzelonderdeel uit een scenario kunnen verwijderen, zodat het overzicht alleen onderdelen bevat die nog nodig zijn. | Must | 1 |
| **US5.** Als ontwerper wil ik prioriteit (1-3) aan onderdelen kunnen geven, zodat ik weet wat eerst aangeschaft moet worden. | Should | 1 |
| **US6.** Als ontwerper wil ik de totale kosten (prijs + transportkosten) zien, zodat ik niet voor verrassingen kom te staan. | Must | 2 |
| **US7.** Als ontwerper wil ik kosten per scenario kunnen inzien, inclusief budgetoverschrijdingen, zodat ik realistisch kan plannen. | Must | 2 |
| **US8.** Als ontwerper wil ik onderdelen binnen een prijsrange kunnen zoeken, zodat ik snel alternatieven kan kiezen tijdens technische reviews. | Must | 2 |
| **US9.** Als ontwerper wil ik een maandelijks inkoopritme kunnen berekenen voor een duur sleutelonderdeel, zodat ik gefaseerd kan inkopen. | Should | 2 |
| **US10.** Als ontwerper wil ik bij afsluiten een sessieoverzicht zien, zodat ik voortgang kan volgen. | Could | 2 |
| **US11.** Als ontwerper wil ik CSV-bestanden kunnen importeren vanaf een gekozen bestandslocatie, zodat ik snel met workshopdata kan starten en niet afhankelijk ben van een vaste opslagplek. | Must | 3 |
| **US12.** Als gebruiker wil ik bij het starten van de applicatie een toegangscode invoeren, zodat de applicatie niet direct toegankelijk is zonder geheime configuratie. | Must | 3 |

### User concerns

- **C1. Data integrity:** Scenario's en leveranciers moeten consequent onder dezelfde naam worden vastgelegd, zodat onderdelen niet onbedoeld over verschillende namen worden verdeeld en overzichten betrouwbaar blijven.
- **C2. Security:** De applicatie moet beschermd worden tegen ongeautoriseerde toegang door het gebruik van een toegangscode.
- **C3. Security:** Gevoelige configuratie, zoals de toegangscode, mag niet leesbaar in de broncode of in gedeelde projectbestanden staan.
- **C4. Security:** De toegangscode moet veilig worden verwerkt en opgeslagen, zodat de oorspronkelijke code niet uit de opgeslagen waarde kan worden afgelezen.
- **C5. Usability:** Het menu moet duidelijke keuzes en begrijpelijke foutmeldingen tonen, zodat een ontwerper de onderdelen en budgetten zonder technische voorkennis kan beheren.
- **C6. Scalability:** Het ontwerp moet uitbreidbaar zijn voor toekomstige versies.
- **C7. Realiteitscheck:** Het systeem moet vroeg en duidelijk laten zien of een scenario financieel haalbaar is, zodat misrekeningen tijdens bouw of testweek worden voorkomen.
- **C8. Deployment/Usability:** De applicatie moet op een standaardbesturingssysteem via de terminal gestart kunnen worden, zodat de gebruiker het programma kan gebruiken en testen in de beoogde leeromgeving.
- **C9. Data portability:** De applicatie moet import- en databestanden vanaf verschillende opslaglocaties kunnen gebruiken, zodat de gebruiker flexibel kan werken met projectmappen, andere schijven of externe opslag.

## Increment 1 Use Cases

### UC1: Onderdeel handmatig toevoegen
**Actor:** Ontwerper

**Beschrijving:**

1. De ontwerper kiest de optie "Registreer nieuw puzzelonderdeel".
2. Het systeem toont eerst een lijst met beschikbare scenario's.
3. De ontwerper kiest een scenario.
4. Het systeem vraagt titel en prijs van het onderdeel.
5. Het systeem vraagt leverancier en controleert of deze bestaat.
6. Het systeem vraagt prioriteit (1-3) en corrigeert invoer buiten bereik.
7. Het systeem slaat het onderdeel op in het gekozen scenario.
8. Het systeem bevestigt toevoeging en toont de sessieteller.

**Alternatieve flows:**

2. a. Als er geen scenario's aanwezig zijn, volgt een foutmelding en stopt de use case.
5. a. Als de leverancier niet bestaat, volgt een foutmelding en stopt de use case.

### UC2: Kostprijs van onderdeel herberekenen
**Actor:** Ontwerper

**Beschrijving:**

1. De ontwerper kiest "Herbereken kostprijs van onderdeel".
2. Het systeem toont eerst een lijst met beschikbare scenario's.
3. De ontwerper kiest een scenario.
4. Het systeem toont een genummerde onderdelenlijst uit dat scenario.
5. De ontwerper kiest een nummer.
6. Het systeem vraagt de nieuwe prijs.
7. Het systeem werkt de prijs bij en bevestigt dit.

**Alternatieve flows:**

2. a. Als er geen scenario's aanwezig zijn, volgt een foutmelding en stopt de use case.
4. a. Als er geen onderdelen in het gekozen scenario aanwezig zijn, volgt een foutmelding en stopt de use case.
5. a. Als het gekozen onderdeelnummer niet bestaat, volgt een foutmelding en stopt de use case.

### UC3: Scenariobudget bijstellen
**Actor:** Ontwerper

**Precondities:**
- De applicatie is gestart.

**Beschrijving:**

1. De ontwerper kiest "Stel scenariobudget bij".
2. Het systeem toont de beschikbare scenario's en hun huidige budget.
3. De ontwerper kiest het scenario waarvan het budget moet veranderen.
4. Het systeem vraagt om het nieuwe budget.
5. De ontwerper voert het nieuwe budget in.
6. Het systeem slaat het nieuwe budget voor het gekozen scenario op.
7. Het systeem bevestigt dat het budget is aangepast.

**Alternatieve flows:**

2. a. Als er geen scenario's aanwezig zijn, toont het systeem een foutmelding en stopt de use case zonder budgetwijziging.
3. a. Als het gekozen scenarionummer niet bestaat, toont het systeem "Ongeldige keuze." en stopt de use case zonder budgetwijziging.

### UC4: Onderdeel verwijderen
**Actor:** Ontwerper

**Beschrijving:**

1. De ontwerper kiest "Schrap onderdeel uit build".
2. Het systeem toont eerst een lijst met beschikbare scenario's.
3. De ontwerper kiest een scenario.
4. Het systeem toont een genummerde onderdelenlijst uit dat scenario.
5. De ontwerper kiest een nummer.
6. Het systeem verwijdert het onderdeel.
7. Het systeem bevestigt de verwijdering en verhoogt de sessieteller.

**Alternatieve flows:**

2. a. Als er geen scenario's aanwezig zijn, volgt een foutmelding en stopt de use case.
4. a. Als er geen onderdelen in het gekozen scenario aanwezig zijn, volgt een foutmelding en stopt de use case.
5. a. Als het gekozen onderdeelnummer niet bestaat, volgt een foutmelding en stopt de use case.

## Increment 2 Use Cases

### UC5: Alternatieven zoeken op budget
**Actor:** Ontwerper

**Beschrijving:**

1. De ontwerper kiest "Zoek alternatieven binnen restbudget".
2. Het systeem vraagt twee budgetgrenzen.
3. Het systeem bepaalt automatisch minimum en maximum.
4. Het systeem haalt onderdelen op binnen dit bereik.
5. Het systeem toont titel en prijs per resultaat.

**Alternatieve flows:**

4. a. Als er geen onderdelen binnen het opgegeven budgetbereik zijn, volgt een melding en stopt de use case.

### UC6: Inkoopritme voor sleutelonderdeel berekenen
**Actor:** Ontwerper

**Beschrijving:**

1. De ontwerper kiest "Maak inkoopritme voor sleutelonderdeel".
2. Het systeem toont een genummerde lijst met onderdelen.
3. De ontwerper kiest een onderdeelnummer.
4. Het systeem vraagt over hoeveel maanden aankoop gepland is.
5. Het systeem berekent cumulatief opgebouwd budget per maand.
6. Het systeem toont het inkoopritme.

**Alternatieve flows:**

2. a. Als er geen onderdelen aanwezig zijn, volgt een foutmelding en stopt de use case.
3. a. Als het gekozen onderdeelnummer niet bestaat, volgt een foutmelding en stopt de use case.

### UC7: Haalbaarheid per scenario inzien
**Actor:** Ontwerper

**Beschrijving:**

1. De ontwerper kiest "Toon haalbaarheidsoverzicht per scenario".
2. Het systeem haalt alle scenario's op en toont voor elk scenario:
   - aantal onderdelen in het scenario
   - goedkoopste onderdeel
   - duurste onderdeel
   - gemiddelde onderdeelprijs
   - totaalbedrag van alle onderdelen inclusief transportkosten
   - scenariobudget
   - status: of het budget is overschreden
3. Het systeem toont een overzicht per scenario met bovenstaande informatie.
4. Het systeem waarschuwt met een visuele indicator als het totaalbedrag het budget overschrijdt.

**Alternatieve flows:**

2. a. Als er geen scenario's aanwezig zijn, volgt een foutmelding en stopt de use case.
3. a. Als een scenario geen onderdelen bevat, toont het systeem "Nog geen onderdelen in dit scenario" en het budget.

### UC8: Ontwerpsessie afsluiten met sessiestatistieken
**Actor:** Ontwerper

**Beschrijving:**

1. De ontwerper kiest "Sluit ontwerpsessie af".
2. Het systeem toont een afsluitbericht.
3. Het systeem toont sessiestatistieken: het totaal aantal toegevoegde en verwijderde onderdelen tijdens de huidige sessie.
4. Het programma stopt.

## Increment 3 Use Cases

### UC9: Onderdelen importeren uit CSV
**Actor:** Ontwerper

**Preconditie:** Er is een geldig CSV-bestand met kolommen `titel`, `prijs`, `leverancier`, `scenario`, `prioriteit`.

**Beschrijving:**

1. De ontwerper kiest "Importeer intakebestand uit CSV".
2. Het systeem vraagt de bestandsnaam.
3. Het systeem controleert of de bestandsnaam minimaal 4 tekens bevat.
4. Het systeem controleert of het bestand bestaat.
5. Het systeem leest het bestand regel voor regel.
6. Voor elke regel controleert het systeem of de leverancier bestaat.
7. Voor elke regel controleert het systeem of het scenario bestaat.
8. Het systeem voegt onderdelen toe.
9. Het systeem toont een bevestiging.

**Alternatieve flows:**

3. a. Als de bestandsnaam korter is dan 4 tekens, volgt een foutmelding en stopt de use case.
4. a. Als het bestand niet bestaat, volgt een foutmelding en stopt de use case.
6. a. Als de leverancier niet bestaat, wordt deze aangemaakt met standaardwaarde voor transportkosten.
7. a. Als het scenario niet bestaat, wordt deze aangemaakt met standaardwaarde voor budgetlimiet.

### UC10: Applicatie starten met toegangscode
**Actor:** Gebruiker

**Preconditie:** De hash van de toegangscode staat in het `.env`-bestand.

**Beschrijving:**

1. De gebruiker start de applicatie.
2. Het systeem vraagt om een toegangscode.
3. De gebruiker voert de toegangscode in.
4. Het systeem hasht de invoer en vergelijkt deze met de hash uit het `.env`-bestand.
5. Bij een correcte code toont het systeem het hoofdmenu.
6. Bij een onjuiste code toont het systeem een foutmelding en stopt de applicatie.

**Alternatieve flows:**

5. a. Bij een onjuiste code toont het systeem een foutmelding en stopt de applicatie.
5. b. Als `TOEGANGSCODE_HASH` ontbreekt, toont het systeem een foutmelding en stopt de applicatie.

## Domeinmodel

[Voeg hier het domeinmodel toe]

## Gebruikersinterface

De applicatie draait in de terminal. De gebruiker werkt via een genummerd menu.

### Schermontwerp toegangscode

```text
Voer toegangscode in:
```

### Schermontwerp menu

```text
--- QuestComposer ---
1. Registreer nieuw puzzelonderdeel
2. Herbereken kostprijs van onderdeel
3. Schrap onderdeel uit build
4. Stel scenariobudget bij
5. Zoek alternatieven binnen restbudget
6. Maak inkoopritme voor sleutelonderdeel
7. Toon haalbaarheidsoverzicht per scenario
8. Sluit sessie af
9. Importeer intakebestand uit CSV
Maak een keuze:
```

### Schermontwerp "Inkoopritme voor sleutelonderdeel"

Tonen overzicht van onderdelen:

```text
1. [Bankoverval] Code-slot - EUR 89.00
2. [Labgeheim] UV-lamp - EUR 24.95
3. [Ruimtestation] Audio trigger board - EUR 42.50
```

Vragen input:

```text
Voor welk sleutelonderdeel wil je een inkoopritme? (nummer): 1
Over hoeveel maanden wil je dit onderdeel operationeel hebben? 3
```

Tonen inkoopritme:

```text
Inkoopritme voor Code-slot (Bankoverval):
Maand 1: Opgebouwd budget: EUR 29.67
Maand 2: Opgebouwd budget: EUR 59.33
Maand 3: Opgebouwd budget: EUR 89.00
```