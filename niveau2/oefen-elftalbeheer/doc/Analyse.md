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