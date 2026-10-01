# Analyse

## Requirements

## User stories

| Nr | User story | Query nodig? | INNER JOIN? | Gecombineerde WHERE? | Beide? | Voorbeeldquery |
|---|---|---|---|---|---|---|
| US1 | Als DJ wil ik een track kunnen invoeren met titel, artiest, genre, duur en jaar, zodat ik een volledig digitaal overzicht kan krijgen van mijn collectie. | Ja | Nee | Nee | Nee | `INSERT INTO track (titel, artiest_id, genre_id, duur, jaar) VALUES ('Levels', 1, 2, 240, 2011);` |
| US2 | Als DJ wil ik een lijst kunnen zien van alle tracks in mijn collectie, zodat ik gemakkelijk kan bladeren en inspiratie kan opdoen. | Ja | Ja | Nee | Nee | `SELECT track.titel, artiest.naam, genre.naam, track.duur, track.jaar FROM track INNER JOIN artiest ON track.artiest_id = artiest.id INNER JOIN genre ON track.genre_id = genre.id;` |
| US3 | Als DJ wil ik tracks kunnen zoeken die vanaf een bepaald jaar uitgekomen zijn en in een bepaald genre vallen, zodat ik altijd een track kan vinden dat op dat moment goed bij me past. | Ja | Ja | Ja | Ja | `SELECT track.titel, artiest.naam, genre.naam, track.jaar FROM track INNER JOIN artiest ON track.artiest_id = artiest.id INNER JOIN genre ON track.genre_id = genre.id WHERE track.jaar >= 2020 AND genre.naam = 'House';` |
| US4 | Als DJ wil ik bij het afsluiten zien hoeveel wijzigingen ik deze sessie heb aangebracht, zodat ik overzicht houd op mijn uitgevoerde taken. | Nee | Nee | Nee | Nee | Geen SQL-query nodig; dit kan met een teller in de applicatie. |
| US5 | Als DJ wil ik nieuwe artiesten kunnen invoeren om later hun tracks te kunnen toevoegen. | Ja | Nee | Nee | Nee | `INSERT INTO artiest (naam) VALUES ('Martin Garrix');` |
| US6 | Als DJ wil ik tracks kunnen verwijderen, zodat de administratie blijft kloppen als ik platen wegdoe. | Ja | Nee | Nee | Nee | `DELETE FROM track WHERE id = 15;` |
| US7 | Als DJ wil ik een willekeurige playlist kunnen genereren op basis van een maximale tijdsduur, zodat ik precies weet welke tracks ik kan draaien in een specifieke tijdsperiode. | Ja | Nee | Nee | Nee | `SELECT titel, duur FROM track WHERE duur <= 1800 ORDER BY RANDOM();` |
| US8 | Als DJ wil ik uitgebreide statistieken inzien (zoals totale duur, gemiddelde lengte en herkomst van artiesten), zodat ik inzicht krijg in de diversiteit van mijn collectie. | Ja | Ja | Nee | Nee | `SELECT SUM(track.duur), AVG(track.duur), artiest.land FROM track INNER JOIN artiest ON track.artiest_id = artiest.id GROUP BY artiest.land;` |
| US9 | Als DJ wil ik genres kunnen beheren om ook tracks aan nieuwe genres te kunnen toevoegen en de lijst van genres actueel te houden. | Ja | Nee | Nee | Nee | `INSERT INTO genre (naam) VALUES ('Techno');` |
| US10 | Als DJ wil ik kunnen zien hoeveel tracks er per genre in mijn collectie zitten en hoe lang die in totaal duren, zodat ik weet hoe mijn muziekcollectie verdeeld is over de genres. | Ja | Ja | Nee | Nee | `SELECT genre.naam, COUNT(track.id), SUM(track.duur) FROM track INNER JOIN genre ON track.genre_id = genre.id GROUP BY genre.naam;` |


## Use cases

### UC1: Track toevoegen

**Actor:** DJ  
**Preconditie:** De artiest en het genre bestaan al in de database.

**Beschrijving:**

1. De DJ kiest "Nieuwe track toevoegen".
2. De DJ voert de artiest, het genre, de titel, de duur en het jaar in.
3. Het systeem controleert de artiest en het genre.
4. Het systeem slaat de track op in de database.
5. Het systeem bevestigt de toevoeging.

### UC2: Tracks bekijken

**Actor:** DJ  
**Preconditie:** Er staan tracks in de collectie.

**Beschrijving:**

1. De DJ kiest "Tracks bekijken".
2. Het systeem haalt alle tracks op.
3. Het systeem toont de titel, artiest, genre, duur en het jaar.

### UC4: Wijzigingen bekijken

**Actor:** DJ  
**Preconditie:** De applicatie is gebruikt.

**Beschrijving:**

1. De DJ sluit de applicatie af.
2. Het systeem telt de wijzigingen van de sessie.
3. Het systeem toont het aantal wijzigingen.
4. De applicatie wordt afgesloten.


### UC5: Genre toevoegen

**Actor:** DJ

**Beschrijving:**

1. De DJ kiest "Genre toevoegen".
2. De DJ voert de naam en omschrijving van het genre in.
3. Het systeem controleert of het genre al bestaat.
4. Het systeem voegt het genre toe.
5. Het systeem bevestigt de toevoeging.

### UC6: Genre verwijderen

**Actor:** DJ

**Beschrijving:**

1. De DJ kiest "Genre verwijderen".
2. De DJ voert de naam van het genre in.
3. Het systeem controleert of het genre bestaat.
4. Het systeem controleert of er tracks aan het genre gekoppeld zijn.
5. Het systeem verwijdert het genre als er geen tracks aan gekoppeld zijn.


### UC3: Tracks zoeken

**Actor:** DJ

**Beschrijving:**

1. De DJ kiest "Tracks zoeken".
2. De DJ voert een minimaal jaar en een genre in.
3. Het systeem zoekt tracks die aan beide voorwaarden voldoen.
4. Het systeem toont de gevonden tracks.

**Uitzondering:**
Als er geen tracks voldoen, toont het systeem `Er zijn geen tracks gevonden`.

### UC7: Artiest toevoegen

**Actor:** DJ

**Beschrijving:**

1. De DJ kiest "Artiest toevoegen".
2. De DJ voert de naam en het land van de artiest in.
3. Het systeem slaat de artiest op.
4. Het systeem bevestigt de toevoeging.

### UC8: Track verwijderen

**Actor:** DJ

**Beschrijving:**

1. De DJ kiest "Track verwijderen".
2. De DJ voert de artiest en titel in.
3. Het systeem controleert of de track bestaat.
4. Het systeem verwijdert de track.

**Uitzondering:**
Als de track niet bestaat, toont het systeem `Track bestaat niet`.

### UC9: Playlist samenstellen

**Actor:** DJ

**Beschrijving:**

1. De DJ kiest "Playlist samenstellen".
2. De DJ voert de gewenste tijd in minuten in.
3. Het systeem kiest tracks in een willekeurige volgorde.
4. Het systeem toont tracks totdat de gewenste tijd is bereikt of overschreden.
5. Het systeem toont de totale duur van de playlist.

**Uitzondering:**
Als de tijd 0 of lager is, toont het systeem `Tijd moet groter zijn dan 0`.

### UC10: Statistieken bekijken

**Actor:** DJ

**Beschrijving:**

1. De DJ kiest een statistiek uit het menu.
2. Het systeem haalt de benodigde gegevens uit de database.
3. Het systeem toont de statistieken.

### UC11: Genreoverzicht bekijken

**Actor:** DJ

**Beschrijving:**

1. De DJ kiest "Genreoverzicht bekijken".
2. Het systeem groepeert de collectie per genre.
3. Het systeem toont per genre het aantal tracks en de totale duur.

## User concerns

- **C1. Reliability:** Gegevens moeten persistent worden opgeslagen in een lokale database zodat ze bewaard blijven na het afsluiten.
- **C2. Integrity:** De data moet consistent blijven; tracks mogen alleen gekoppeld worden aan bestaande artiesten en genres.