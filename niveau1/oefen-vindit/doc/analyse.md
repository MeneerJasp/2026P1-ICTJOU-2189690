# Analyse: Vind it! Verkoopmanager

## Introductie

In dit document worden de functionele en niet-functionele eisen van de verkoopmanager **Vind it!** beschreven. Deze applicatie stelt gebruikers in staat om verkoopgegevens van tweedehands artikelen vast te leggen. Op basis van de ingevoerde verkopen kunnen financiële statistieken worden getoond en gefilterde overzichten van de verkoopgeschiedenis worden gegenereerd.

## Requirements

### User stories

| ID  | User Story                                                                                                                                                                                          |
| :-- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Als **tweedehands verkoper** wil ik **een verkoop kunnen vastleggen met datum, tijd, categorie en verkoopbedrag** zodat **ik overzicht houd over wat ik verkocht heb en wat het heeft opgeleverd**. |
| 2 | Als **tweedehands verkoper** wil ik **mijn verkopen per categorie kunnen bekijken** zodat **ik kan zien wat ik aan kleding, boeken en overige artikelen heb verkocht**.                             |
| 3 | Als **tweedehands verkoper** wil ik **de totale opbrengst van mijn verkopen kunnen bekijken** zodat **ik weet hoeveel geld mijn verkopen samen hebben opgeleverd**.                                 |

### User concerns

| ID  | Concern                                                                                                                                                   |
| :-- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. | **Reliability**: De verkoopgegevens moeten bewaard blijven wanneer de computer wordt uitgezet en later opnieuw wordt gestart.                             |
| 2. | **Privacy**: De verkoopgegevens moeten lokaal op de eigen computer worden opgeslagen, zodat andere bedrijven de financiële gegevens niet kunnen bekijken. |
| 3. | **Usability**: De applicatie moet eenvoudig te gebruiken zijn voor iemand zonder programmeerkennis, bijvoorbeeld met een simpel keuzemenu.                |