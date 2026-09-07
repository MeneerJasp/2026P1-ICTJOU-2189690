# Analyse

## Introductie

In dit document staan de requirements voor de WorkoutTracker. De WorkoutTracker is bedoeld om workouts op te slaan en later terug te kunnen kijken. De gebruiker moet onder andere workouts kunnen invoeren, workouts kunnen filteren op soort sport en kunnen zien hoeveel tijd er in totaal aan sporten is besteed.

De requirements hieronder zijn opgesteld op basis van het interview met de opdrachtgever.

## Requirements

Een **User Story** beschrijft wat een gebruiker met het systeem wil kunnen doen en waarom die functionaliteit nodig is.

Een **User Concern** beschrijft iets wat de gebruiker belangrijk vindt of waar een risico zit. Dit gaat bijvoorbeeld over betrouwbaarheid, beveiliging of de juistheid van gegevens.

### User Stories

| ID      | User Story                                                                                                                                                                                                   |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1** | Als **sporter** wil ik **een workout kunnen invoeren met een workouttype, datum/tijd en duur in minuten** zodat **ik kan bijhouden welke workouts ik heb gedaan**.                                           |
| **2** | Als **sporter** wil ik **een overzicht van al mijn workouts kunnen bekijken** zodat **ik later terug kan zien wat ik wanneer heb gedaan**.                                                                   |
| **3** | Als **sporter** wil ik **mijn workouts kunnen filteren op hardlopen, krachttraining en overige sporten** zodat **ik per soort sport mijn workouts kan bekijken**.                                            |
| **4** | Als **sporter** wil ik **kunnen zien hoeveel tijd ik in totaal heb gesport** zodat **ik inzicht krijg in hoeveel tijd ik aan sporten heb besteed**.                                                          |
| **5** | Als **sporter** wil ik **een overzicht kunnen bekijken van alle workouttypes die ik eerder heb gebruikt** zodat **ik dezelfde benamingen kan blijven gebruiken en kan zien welke sporten ik al heb gedaan**. |

### User Concerns

| ID     | Categorie       | User Concern                                                                                                                                                                 |
| ------ | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Reliability** | De opgeslagen workouts mogen niet verdwijnen wanneer de applicatie wordt afgesloten of de computer wordt uitgezet.                                                           |
| **2** | **Security**    | De workoutgegevens moeten privé blijven en mogen niet via het internet toegankelijk zijn voor andere personen.                                                               |
| **3** | **Integrity**   | Workouttypes moeten op een consistente manier worden ingevoerd, zodat bijvoorbeeld `kracht`, `krachttraining` en `sportschool` niet als verschillende sporten worden gezien. |
| **4** | **Integrity**   | De berekening van de totale sportduur moet kloppen. De ingevoerde minuten moeten correct worden omgerekend naar uren en minuten.                                             |
| **5** | **Reliability** | De applicatie moet lokaal en stand-alone op de computer kunnen draaien, zonder afhankelijk te zijn van internet of een externe clouddienst.                                  |
| **6** | **Usability**   | De belangrijkste overzichten en filters moeten makkelijk bereikbaar zijn vanuit het menu.                                                                                    |

## Gebruikersinterface

De applicatie draait in een terminalscherm. De gebruiker krijgt een menu te zien en kan door het invoeren van een cijfer een keuze maken.

Hieronder staan een aantal voorbeelden van hoe de schermen eruit kunnen zien.

### Schermontwerp menu

```text
+--------------------------------------+
| WORKOUTTRACKER                       |
|                                      |
| Maak je keuze:                       |
| 1. Toon alle workouts                |
| 2. Toon alle hardloop-workouts       |
| 3. Toon alle krachttraining-workouts |
| 4. Toon alle overige workouts        |
| 5. Workout invoeren                  |
| 6. Totale duur tonen                 |
| 7. Toon alle gebruikte workouttypes  |
| X. Afsluiten                         |
+--------------------------------------+
```

### Schermontwerp overzicht

```text
2025-01-01 07:15:00 - Hardlopen - 50 minuten
2025-01-02 07:15:00 - Hardl# Analyse

## Introductie

In dit document staan de requirements voor de WorkoutTracker. De WorkoutTracker is bedoeld om workouts op te slaan en later terug te kunnen kijken. De gebruiker moet onder andere workouts kunnen invoeren, workouts kunnen filteren op soort sport en kunnen zien hoeveel tijd er in totaal aan sporten is besteed.

De requirements hieronder zijn opgesteld op basis van het interview met de opdrachtgever.

## Requirements

Een **User Story** beschrijft wat een gebruiker met het systeem wil kunnen doen en waarom die functionaliteit nodig is.

Een **User Concern** beschrijft iets wat de gebruiker belangrijk vindt of waar een risico zit. Dit gaat bijvoorbeeld over betrouwbaarheid, beveiliging of de juistheid van gegevens.

### User Stories

| ID      | User Story                                                                                                                                                                                                   |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **US1** | Als **sporter** wil ik **een workout kunnen invoeren met een workouttype, datum/tijd en duur in minuten** zodat **ik kan bijhouden welke workouts ik heb gedaan**.                                           |
| **US2** | Als **sporter** wil ik **een overzicht van al mijn workouts kunnen bekijken** zodat **ik later terug kan zien wat ik wanneer heb gedaan**.                                                                   |
| **US3** | Als **sporter** wil ik **mijn workouts kunnen filteren op hardlopen, krachttraining en overige sporten** zodat **ik per soort sport mijn workouts kan bekijken**.                                            |
| **US4** | Als **sporter** wil ik **kunnen zien hoeveel tijd ik in totaal heb gesport** zodat **ik inzicht krijg in hoeveel tijd ik aan sporten heb besteed**.                                                          |
| **US5** | Als **sporter** wil ik **een overzicht kunnen bekijken van alle workouttypes die ik eerder heb gebruikt** zodat **ik dezelfde benamingen kan blijven gebruiken en kan zien welke sporten ik al heb gedaan**. |

### User Concerns

| ID     | Categorie       | User Concern                                                                                                                                                                 |
| ------ | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **C1** | **Reliability** | De opgeslagen workouts mogen niet verdwijnen wanneer de applicatie wordt afgesloten of de computer wordt uitgezet.                                                           |
| **C2** | **Security**    | De workoutgegevens moeten privé blijven en mogen niet via het internet toegankelijk zijn voor andere personen.                                                               |
| **C3** | **Integrity**   | Workouttypes moeten op een consistente manier worden ingevoerd, zodat bijvoorbeeld `kracht`, `krachttraining` en `sportschool` niet als verschillende sporten worden gezien. |
| **C4** | **Integrity**   | De berekening van de totale sportduur moet kloppen. De ingevoerde minuten moeten correct worden omgerekend naar uren en minuten.                                             |
| **C5** | **Reliability** | De applicatie moet lokaal en stand-alone op de computer kunnen draaien, zonder afhankelijk te zijn van internet of een externe clouddienst.                                  |
| **C6** | **Usability**   | De belangrijkste overzichten en filters moeten makkelijk bereikbaar zijn vanuit het menu.                                                                                    |

## Gebruikersinterface

De applicatie draait in een terminalscherm. De gebruiker krijgt een menu te zien en kan door het invoeren van een cijfer een keuze maken.

Hieronder staan een aantal voorbeelden van hoe de schermen eruit kunnen zien.

### Schermontwerp menu

```text
+--------------------------------------+
| WORKOUTTRACKER                       |
|                                      |
| Maak je keuze:                       |
| 1. Toon alle workouts                |
| 2. Toon alle hardloop-workouts       |
| 3. Toon alle krachttraining-workouts |
| 4. Toon alle overige workouts        |
| 5. Workout invoeren                  |
| 6. Totale duur tonen                 |
| 7. Toon alle gebruikte workouttypes  |
| X. Afsluiten                         |
+--------------------------------------+
```

### Schermontwerp overzicht

```text
2025-01-01 07:15:00 - Hardlopen - 50 minuten
2025-01-02 07:15:00 - Hardlopen - 120 minuten
2025-01-03 07:15:00 - Krachttraining - 50 minuten
2025-01-04 07:15:00 - Zwemmen - 60 minuten
```

### Schermontwerp gebruikte workouttypes

```text
hardlopen
krachttraining
yoga
zwemmen
```

### Schermontwerp totale duur van workouts

```text
Totale duur van workouts: 4 uur en 20 minuten.
```
2025-01-01 07:15:00 - Hardlopen - 120 minuten
2025-01-03 07:15:00 - Krachttraining - 50 minuten
2025-01-04 07:15:00 - Zwemmen - 60 minuten
```

### Schermontwerp gebruikte workouttypes

```text
hardlopen
krachttraining
yoga
zwemmen
```

### Schermontwerp totale duur van workouts

```text
Totale duur van workouts: 4 uur en 20 minuten.
```
