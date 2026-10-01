# Analyse verlanglijstmanager

## Inleiding

In dit document worden de functionele en non-functionele eisen van de applicatie "Verlanglijstmanager" beschreven. Deze applicatie is bedoeld voor gebruikers die hun verlanglijst willen beheren, inclusief het bijhouden van items, prijzen, winkels en lijsten. De focus ligt op gebruiksvriendelijkheid, datakwaliteit en het bieden van nuttige inzichten in de verlanglijst.

### User stories

| User Story | Prioriteit | Increment |
|-------------|------------|----------:|
| **US1.** Als student wil ik een item aan een verlanglijst kunnen toevoegen, zodat ik mijn wensen op één plek kan bijhouden. | Must | 1 |
| **US2.** Als student wil ik de prijs van een item kunnen aanpassen, zodat mijn verlanglijst actuele prijzen bevat. | Must | 1 |
| **US3.** Als student wil ik het budget van een verlanglijst kunnen aanpassen, zodat het budget blijft aansluiten bij mijn afspraken. | Must | 1 |
| **US4.** Als student wil ik een item van een verlanglijst kunnen verwijderen, zodat mijn verlanglijst alleen items bevat die ik nog wil kopen. | Must | 1 |
| **US5.** Als student wil ik een prioriteit aan een item kunnen geven, zodat ik kan aangeven welke items het belangrijkst zijn. | Should | 1 |
| **US6.** Als student wil ik kunnen zoeken naar items binnen een specifieke prijsrange, zodat ik gericht iets nuttigs kan kopen van mijn restbudget. | Must | 2 |
| **US7.** Als student wil ik een maandelijks spaarplan kunnen berekenen voor items, zodat ik weet hoeveel ik opzij moet leggen voor toekomstige aankopen. | Must | 2 |
| **US8.** Als student wil ik mijn uitgaven per lijst kunnen inzien, inclusief budgetoverschrijdingen, zodat ik mijn financiële doelen bewaak. | Must | 2 |
| **US9.** Als student wil ik altijd de totale kosten (prijs + verzendkosten) zien, zodat ik niet voor verrassingen kom te staan bij het afrekenen. | Must | 2 |
| **US10.** Als student wil ik bij het afsluiten een motiverend overzicht van mijn sessie zien, zodat ik gestimuleerd word in mijn gezonde financiële gedrag. | Should | 2 |
| **US11.** Als student wil ik zien hoeveel budget er overblijft als ik alleen "hoge" prioriteit items koop, zodat ik betere keuzes kan maken. | Won't | 2 |
| **US12.** Als student wil ik de verzendkosten per winkel kunnen aanpassen, zodat het getoonde totaalbedrag nog klopt als de winkel de verzendkosten heeft aangepast. | Won't | 2 |
| **US13.** Als student wil ik de verzendkosten per item automatisch laten berekenen op basis van de regels van de winkel, zodat de getoonde bedragen echt kloppen. | Won't | 2 |
| **US14.** Als student wil ik CSV-bestanden kunnen importeren vanaf een usb-stick, zodat ik de lijst die ik tijdens de workshop heb gemaakt snel kan inladen. | Must | 3 |
| **US15.** Als student wil ik bij het starten van de applicatie een toegangscode invoeren, zodat niet iedereen direct toegang heeft tot mijn verlanglijst. | Must | 3 |


### User concerns


- **C1. Data integrity:** Winkels en verlanglijsten moeten consistent en herkenbaar worden opgeslagen, zodat dezelfde gegevens niet onder verschillende namen voorkomen en de overzichten betrouwbaar blijven.
- **C2. Security:** De applicatie moet beschermd worden tegen ongeautoriseerde toegang door het gebruik van een toegangscode.
- **C3. Security:** Gevoelige gegevens mogen niet onveilig worden opgeslagen of zichtbaar zijn in de broncode.
- **C4. Security:** De toegangscode moet op een veilige manier worden verwerkt en opgeslagen.
- **C5. Usability:** De gebruikersinterface moet intuïtief en gemakkelijk te navigeren zijn, zodat studenten zonder technische kennis de verlanglijst kunnen beheren. Het mag wel een CLI-interface zijn.
- **C6. Scalability:** De applicatie moet ontworpen zijn met het oog op toekomstige uitbreidingen, zoals het toevoegen van meer geavanceerde functies of integraties met externe diensten.
- **C7. Deployment/Usability:** De applicatie moet op een standaardbesturingssysteem via de terminal gestart kunnen worden, zodat de gebruiker het programma kan gebruiken en testen in de beoogde leeromgeving.
- **C8. Data portability:** [Vul in]

## Increment 1 Use Cases

### UC1: Item handmatig toevoegen
**Actor:** Student  
**Beschrijving:**

1. De student kiest de optie "Voeg item toe aan verlanglijst".
2. Het systeem toont eerst een lijst met beschikbare verlanglijsten.
3. De student kiest een verlanglijst.
4. Het systeem vraagt om de naam en de prijs van het item.
5. Het systeem vraagt om de winkelnaam en controleert of de winkel bestaat.
6. Het systeem vraagt om de prioriteit (1-3) en corrigeert de invoer automatisch als deze buiten dit bereik valt.
7. Het systeem slaat het item op in de gekozen verlanglijst in de database.
8. Het systeem bevestigt de toevoeging en toont het totaal aantal toegevoegde items van deze sessie.

**Alternatieve flows:**
2. a.  Als er geen verlanglijsten aanwezig zijn, volgt een foutmelding en stopt de use case.
5. a.  Als de winkel niet bestaat, volgt een foutmelding en stopt de use case.

### UC2: Prijs van item aanpassen
**Actor:** Student  
**Beschrijving:**

1. De student kiest de optie "Prijs van item aanpassen".
2. Het systeem toont eerst een lijst met beschikbare verlanglijsten.
3. De student kiest een verlanglijst.
4. Het systeem toont een genummerde lijst van items uit die verlanglijst.
5. Het systeem vraagt om het nummer van het item dat moet worden aangepast.
6. Het systeem vraagt om de nieuwe prijs.
7. Het systeem werkt de prijs bij in de database en bevestigt de wijziging.

**Alternatieve flows:**
2. a.  Als er geen verlanglijsten aanwezig zijn, volgt een foutmelding en stopt de use case.
4. a.  Als er geen items aanwezig zijn in de gekozen verlanglijst, volgt een foutmelding en stopt de use case.


### UC3: Lijstbudget aanpassen
**Actor:** Student  
**Precondities:**
- De applicatie is gestart.

**Normale flow:**

1. De student kiest de optie "Pas lijstbudget aan".
2. Het systeem toont een overzicht van alle verlanglijsten en hun huidige budget.
3. De student kiest de verlanglijst waarvan het budget aangepast moet worden.
4. Het systeem vraagt om het nieuwe budget.
5. De student voert het nieuwe budget in.
6. Het systeem werkt het budget van de gekozen verlanglijst bij in de database.
7. Het systeem bevestigt de wijziging.

**Alternatieve flows:**
2. a. Als er geen verlanglijsten aanwezig zijn, volgt een foutmelding en stopt de use case.

### UC4: Item verwijderen
**Actor:** Student  
**Beschrijving:**

1. De student kiest de optie "Verwijder item".
2. Het systeem toont eerst een lijst met beschikbare verlanglijsten.
3. De student kiest een verlanglijst.
4. Het systeem toont een genummerde lijst van items uit die verlanglijst.
5. Het systeem vraagt om het nummer van het item dat verwijderd moet worden.
6. Het systeem verwijdert het item uit de database.
7. Het systeem bevestigt de verwijdering en toont het totaal aantal verwijderde items van deze sessie.

**Alternatieve flows:**
2. a.  Als er geen verlanglijsten aanwezig zijn, volgt een foutmelding en stopt de use case.
4. a.  Als er geen items aanwezig zijn in de gekozen verlanglijst, volgt een foutmelding en stopt de use case.


## Increment 2 Use Cases

### UC5: Zoeken op budget
[Opstellen Use Case 5]


### UC6: Persoonlijk spaarplan berekenen
**Actor:** Student  
**Beschrijving:**

1. De student kiest de optie "Persoonlijk spaarplan berekenen".
2. Het systeem toont een genummerde lijst van alle items met hun huidige prijs.
3. De student voert het nummer (index) van het gewenste item in.
4. Het systeem vraagt over hoeveel maanden het item gekocht moet worden.
5. Het systeem berekent per maand het cumulatieve spaarbedrag.
6. Het systeem toont voor elke maand het totale bedrag dat tot dan toe gespaard moet zijn.

**Alternatieve flows:**
2. a.  Als er geen items aanwezig zijn, volgt een foutmelding en stopt de use case.

### UC7: Uitgaven per lijst inzien
**Actor:** Student  
**Beschrijving:**

1. De student kiest de optie "Uitgaven per lijst inzien".
2. Het systeem haalt alle lijsten op en voor elke lijst de volgende informatie:
   - Aantal items in de lijst
   - Goedkoopste item (prijs)
   - Duurste item (prijs)
   - Gemiddelde itemprijs
   - Totaalbedrag van alle items (inclusief verzendkosten)
   - Lijstbudget
   - Status: of het budget is overschreden
3. Het systeem toont een overzicht per lijst met bovenstaande informatie.
4. Het systeem waarschuwt met een visuele indicator als het totaalbedrag het budget overschrijdt.

**Alternatieve flows:**
2. a.  Als er geen lijsten aanwezig zijn, volgt een foutmelding en stopt de use case.
3. a.  Als een lijst geen items bevat, toont het systeem "Nog geen items in deze lijst" en het budget.

### UC8: Afsluiten
**Actor:** Student  
**Beschrijving:**

1. De student kiest de optie "Afsluiten".
2. Het systeem toont een afscheidsgroet.
3. Het systeem toont een overzicht van de sessiestatistieken: het totaal aantal toegevoegde en verwijderde items tijdens de huidige sessie.
4. Het programma stopt.


## Increment 3 Use Cases

### UC9: Items importeren uit CSV
**Actor:** Student  
**Preconditie:** Er is een geldig CSV-bestand aanwezig met de kolommen 'titel', 'prijs', 'winkel', 'lijst' en 'prioriteit'.  
**Beschrijving:**

1. De student kiest de optie "Importeer items uit CSV".
2. Het systeem vraagt om de bestandsnaam.
3. Het systeem controleert of de bestandsnaam minstens 4 tekens lang is.
4. Het systeem leest het bestand regel voor regel.
5. Voor elke regel controleert het systeem of de winkel bestaat
6. Voor elke regel controleert het systeem of de verlanglijst bestaat.; 
7. Het systeem voegt elk item uit het bestand toe aan de database.
8. Het systeem toont een bevestiging dat de CSV succesvol is geïmporteerd.

**Alternatieve flows:**
3. a.  Als de bestandsnaam korter is dan 4 tekens, volgt een foutmelding en stopt de use case.
5. a.  Als de winkel niet bestaat, dan worden deze aangemaakt met standaardwaarde voor verzendkosten (€0.00) 
6. a. Als de verlanglijst niet bestaat, dan worden deze aangemaakt met standaardwaarde voor budget (€100.00)


### UC10: Applicatie starten met toegangscode
**Actor:** Student  
**Preconditie:** De hash van de toegangscode staat in het `.env`-bestand.  
**Beschrijving:**

1. De student start de applicatie.
2. Het systeem vraagt om een toegangscode.
3. De student voert de toegangscode in.
4. Het systeem hasht de invoer en vergelijkt deze met de hash uit het `.env`-bestand.
5. Het systeem toont het hoofdmenu.

**Alternatieve flows:**
5. a. Bij een onjuiste code toont het systeem een foutmelding en stopt de applicatie.


## Domeinmodel

[Opstellen domeinmodel]


## Gebruikersinterface

De applicatie draait in een terminalscherm. De gebruiker communiceert met het systeem via een genummerd menu. Hieronder staan de schermontwerpen voor de opties met de meeste interacties.

### Schermontwerp toegangscode

```text
Voer toegangscode in:
```

### Schermontwerp menu

```text
--- Verlanglijstmanager ---
1. Voeg item toe aan verlanglijst
2. Pas item prijs aan
3. Verwijder item
4. Pas lijstbudget aan
5. Zoek items op budget
6. Persoonlijk spaarplan berekenen
7. Uitgaven per lijst inzien
8. Afsluiten
9. Importeer items uit CSV
Maak een keuze: 
```

### Schermontwerpen "Persoonlijk spaarplan berekenen"

Tonen overzicht van items:
```text
1. [Studie] Boek over Python - €45.00
2. [Elektronica] Bluetooth speaker - €45.00
3. [Elektronica] Nieuwe koptelefoon - €79.99
```

Vragen input:
```text
Voor welk item wil je een spaarplan? (nummer): 1
Over hoeveel maanden wil je dit kopen? 3
```

Tonen spaarplan:
```text
Spaarplan voor Boek over Python (Studie):
Maand 1: Totaal gespaard: €15.0
Maand 2: Totaal gespaard: €30.0
Maand 3: Totaal gespaard: €45.0
```