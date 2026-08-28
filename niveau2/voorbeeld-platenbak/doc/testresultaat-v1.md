# Testresultaten: Platenbak

* **Uitgevoerd op:** 7 april 2026
* **Door:** Tijs Veroost

## Bevindingen voor uitvoering

## Resultaten

| Testcase | Resultaat |
|---|---|
| TC1: Toon de volledige collectie | NIET geslaagd |
| TC2: Nieuwe track toevoegen (succesvol) | NIET geslaagd |
| TC3: Nieuwe track toevoegen (artiest onbekend) | Geslaagd |
| TC4: Nieuwe track toevoegen (genre onbekend) | Geslaagd |
| TC5: Track verwijderen (succesvol) | NIET geslaagd |
| TC6: Track verwijderen (niet bestaand) | Geslaagd |
| TC7: Playlist samenstellen op tijd | NIET geslaagd |
| TC8: Statistieken tonen | NIET geslaagd |
| TC9: Zoeken op criteria (met resultaten) | NIET geslaagd |
| TC10: Zoeken op criteria (geen resultaten) | NIET geslaagd |
| TC11: Toon genre-overzicht | NIET geslaagd |
| TC12: Sessiestatistieken bij afsluiten | NIET geslaagd |

## Conclusie

Bij deze test-uitvoering werden 9 van de 12 testcases direct geblokkeerd door een bug in de applicatiecode. In vijf SQL-queries werd de tabbelnaam `tracks` gebruikt, terwijl de tabel in de database `track` heet. Dit is gecorrigeerd in [ICTJOU-n2-platenbak/src/platenbak.py](ICTJOU-n2-platenbak/src/platenbak.py) voorafgaand aan de definitieve testuitvoering.

Getroffen functies:
* `haal_tracks_van_artiest_op_uit_database`
* `haal_statistieken_op_uit_database` (5 queries)
* `zoek_tracks_op_criteria_uit_database`
* `haal_genreoverzicht_op_uit_database`
* `track_bestaat_in_database`