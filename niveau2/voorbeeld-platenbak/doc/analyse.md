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

## User concerns

- **C1. Reliability:** Gegevens moeten persistent worden opgeslagen in een lokale database zodat ze bewaard blijven na het afsluiten.
- **C2. Integrity:** De data moet consistent blijven; tracks mogen alleen gekoppeld worden aan bestaande artiesten en genres.