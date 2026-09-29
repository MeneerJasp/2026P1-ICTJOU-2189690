# Analyse Elftalbeheer

## Inleiding

VV Finecce wil een applicatie om elftallen en spelers centraal te beheren. De applicatie moet vooral zorgen voor overzicht en een goede controle van de leeftijd van spelers binnen een elftal.

## User stories

| Nr. | Prioriteit | User story |
|---|---|---|
| US1 | Must | Als medewerker wil ik elftallen kunnen bekijken, zodat ik kan zien welke spelers bij welk elftal horen. |
| US2 | Must | Als medewerker wil ik elftallen kunnen toevoegen met een code, omschrijving, coach en maximumleeftijd, zodat alle elftallen geregistreerd zijn. |
| US3 | Must | Als medewerker wil ik spelers kunnen toevoegen met een naam, leeftijd, positie en elftal, zodat spelers correct geregistreerd worden. |
| US4 | Must | Als medewerker wil ik spelers kunnen verwijderen, zodat de gegevens actueel blijven. |
| US5 | Must | Als medewerker wil ik alleen vaste posities kunnen kiezen, zodat de gegevens netjes en eenduidig blijven. |
| US6 | Must | Als medewerker wil ik dat een speler wordt geblokkeerd als die te oud is voor een elftal, zodat spelers niet in een verkeerde leeftijdscategorie terechtkomen. |
| US7 | Must | Als medewerker wil ik het hele bestand kunnen controleren op spelers die niet bij hun elftal passen, zodat afwijkingen gevonden kunnen worden. |
| US8 | Must | Als medewerker wil ik de gemiddelde leeftijd per elftal kunnen zien, zodat ik deze informatie kan gebruiken bij overleggen met trainers. |
| US9 | Could | Als medewerker wil ik een passend elftal voorgesteld krijgen bij het invoeren van een nieuwe speler, zodat ik sneller een geschikt elftal kan vinden. |
| US10 | Could | Als medewerker wil ik een willekeurige speler als speler van de maand kunnen aanwijzen, zodat de betrokkenheid bij de club wordt vergroot. |
| US11 | Could | Als medewerker wil ik spelers per elftal kunnen exporteren naar een spreadsheet, zodat ik de gegevens kan delen met trainers. |
| US12 | Could | Als medewerker wil ik spelers op naam kunnen zoeken, zodat ik snel een speler kan vinden. |
| US13 | Could | Als medewerker wil ik kunnen zien hoeveel spelers per positie in elk elftal zitten, zodat ik de bezetting per positie kan bekijken. |
| US14 | Could | Als medewerker wil ik een seizoenslabel kunnen gebruiken, zodat ik gegevens van eerdere seizoenen kan terugkijken. |
| US15 | Could | Als medewerker wil ik een melding krijgen wanneer een elftal te weinig basisspelers heeft, zodat ik weet wanneer een elftal niet genoeg spelers heeft voor een wedstrijdselectie. |

## User concerns

| Nr. | User concern |
|---|---|
| C1 | **Gebruiksgemak:** de applicatie moet eenvoudig te gebruiken zijn voor medewerkers. |
| C2 | **Datakwaliteit:** gegevens moeten eenduidig worden opgeslagen, bijvoorbeeld met vaste posities. |
| C3 | **Leeftijdscontrole:** de leeftijdsgrens van een elftal moet betrouwbaar worden gecontroleerd. |
| C4 | **Betrouwbaarheid:** de gegevens moeten na het afsluiten van de applicatie bewaard blijven. |
| C5 | **Lokale werking:** de applicatie moet zonder internetverbinding kunnen werken. |
| C6 | **Onderhoudbaarheid:** de applicatie moet later uitgebreid kunnen worden met nieuwe functies. |
| C7 | **Gelijktijdig gebruik:** de eerste versie hoeft maar door één persoon tegelijk gebruikt te worden. |
| C8 | **Instelbaarheid:** de ondergrens voor het aantal basisspelers moet per elftal instelbaar zijn en niet hardcoded. |

# Use cases

## UC1 – Elftal toevoegen

**Actor:** Medewerker  
**Doel:** Een nieuw elftal toevoegen.

**Scenario:**

1. Medewerker kiest voor elftal toevoegen.
2. Medewerker vult code, omschrijving, coach en maximumleeftijd in.
3. Systeem controleert de gegevens.
4. Systeem slaat het elftal op.

**Uitzondering:**  
Als de code al bestaat of gegevens ongeldig zijn, wordt het elftal niet opgeslagen.

---

## UC2 – Speler toevoegen

**Actor:** Medewerker  
**Doel:** Een speler toevoegen aan een elftal.

**Scenario:**

1. Medewerker kiest voor speler toevoegen.
2. Medewerker vult naam en leeftijd in.
3. Medewerker kiest een positie en een elftal.
4. Systeem controleert of de speler niet te oud is.
5. Systeem slaat de speler op.

**Uitzondering:**  
Als de speler te oud is voor het elftal, wordt de speler niet toegevoegd.

---

## UC3 – Speler verwijderen

**Actor:** Medewerker  
**Doel:** Een speler verwijderen.  
**Preconditie:** De applicatie is gestart.

**Scenario:**

1. Medewerker kiest voor speler verwijderen.
2. Medewerker voert de naam van de speler in.
3. Systeem zoekt de speler.
4. Systeem verwijdert de speler.
5. Systeem toont dat de speler is verwijderd.

**Uitzondering:**  
Als de speler niet gevonden wordt, toont het systeem een melding.

---

## UC4 – Speler zoeken

**Actor:** Medewerker  
**Doel:** Een speler op naam vinden.

**Scenario:**

1. Medewerker kiest voor speler zoeken.
2. Medewerker voert een naam in.
3. Systeem zoekt naar de speler.
4. Systeem toont de gevonden gegevens.

**Uitzondering:**  
Als geen speler wordt gevonden, toont het systeem een melding.

---

## UC5 – Overzicht elftallen en spelers tonen

**Actor:** Medewerker  
**Doel:** Bekijken welke spelers bij welk elftal horen.

**Scenario:**

1. Medewerker kiest voor het elftallenoverzicht.
2. Systeem haalt alle elftallen en spelers op.
3. Systeem toont per elftal de bijbehorende spelers.

---

## UC6 – Spelers per positie tonen

**Actor:** Medewerker  
**Doel:** Bekijken hoeveel spelers per positie in een elftal zitten.

**Scenario:**

1. Medewerker kiest een elftal.
2. Systeem groepeert de spelers per positie.
3. Systeem toont de spelers en aantallen per positie.

---

## UC7 – Gemiddelde leeftijd per elftal tonen

**Actor:** Medewerker  
**Doel:** De gemiddelde leeftijd per elftal bekijken.  
**Preconditie:** De applicatie is gestart.

**Scenario:**

1. Medewerker kiest voor gemiddelde leeftijd per elftal.
2. Systeem groepeert de spelers per elftal.
3. Systeem berekent de gemiddelde leeftijd.
4. Systeem toont de gemiddelde leeftijd per elftal.

**Uitzondering:**  
Als een elftal geen spelers heeft, toont het systeem dat er geen spelers zijn.

---

## UC8 – Leeftijdscontrole uitvoeren

**Actor:** Medewerker  
**Doel:** Controleren of spelers te oud zijn voor hun elftal.

**Scenario:**

1. Medewerker start de leeftijdscontrole.
2. Systeem vergelijkt per speler de leeftijd met de maximumleeftijd van het elftal.
3. Systeem toont spelers die te oud zijn.

---

## UC9 – Passend elftal voorstellen

**Actor:** Medewerker  
**Doel:** Een geschikt elftal voor een nieuwe speler vinden.

**Scenario:**

1. Medewerker voert de leeftijd van de speler in.
2. Systeem controleert de beschikbare elftallen.
3. Systeem zoekt een elftal waarvoor de speler jong genoeg is.
4. Systeem toont het voorgestelde elftal.

---

## UC10 – Speler van de maand kiezen

**Actor:** Medewerker  
**Doel:** Willekeurig een speler van de maand kiezen.

**Scenario:**

1. Medewerker kiest voor speler van de maand.
2. Systeem kiest willekeurig een speler.
3. Systeem toont de gekozen speler.

---

## UC11 – Spelers exporteren

**Actor:** Medewerker  
**Doel:** Spelersgegevens exporteren.

**Scenario:**

1. Medewerker kiest voor exporteren.
2. Systeem haalt de spelers per elftal op.
3. Systeem maakt een spreadsheetbestand.
4. Systeem meldt dat de export klaar is.

---

## UC12 – Gegevens per seizoen bekijken

**Actor:** Medewerker  
**Doel:** Gegevens van een eerder seizoen bekijken.

**Scenario:**

1. Medewerker kiest een seizoen.
2. Systeem haalt de gegevens van dat seizoen op.
3. Systeem toont de elftallen en spelers.

---

## UC13 – Controleren op te weinig spelers

**Actor:** Medewerker  
**Doel:** Zien welke elftallen te weinig basisspelers hebben.

**Scenario:**

1. Medewerker start de controle.
2. Systeem telt per elftal het aantal basisspelers.
3. Systeem vergelijkt dit met de ingestelde ondergrens.
4. Systeem toont welke elftallen te weinig spelers hebben.

---

## UC14 – Sessiestatistieken tonen

**Actor:** Medewerker  
**Doel:** Bekijken hoeveel wijzigingen tijdens de sessie zijn gedaan.  
**Preconditie:** De applicatie is gestart.

**Scenario:**

1. Medewerker gebruikt de applicatie.
2. Systeem houdt bij hoeveel elftallen en spelers zijn toegevoegd en hoeveel spelers zijn verwijderd.
3. Medewerker kiest voor afsluiten.
4. Systeem toont de sessiestatistieken.
5. Systeem sluit de applicatie af.