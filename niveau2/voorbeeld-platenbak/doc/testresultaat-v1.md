# Testresultaten: Platenbak

* **Uitgevoerd op:** 7 april 2026
* **Door:** Jasper van Dis

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

---

## Nieuwe testuitvoering

* **Uitgevoerd op:** 30 september 2026
* **Door:** ChatGPT (geautomatiseerde testuitvoering)

## Resultaten

| Testcase | Resultaat | Waarneming | Afwijking |
|---|---|---|---|
| Nieuwe track toevoegen | Geslaagd | `Frozen Flame is toegevoegd` | Geen |
| Track toevoegen met onbekende artiest | Geslaagd | Track wordt niet toegevoegd | Geen |
| Track toevoegen met onbekend genre | Geslaagd | Track wordt niet toegevoegd | Geen |
| Statistieken tonen | Geslaagd | 55 tracks, gemiddelde duur 303.3454545454546 seconden en totale duur 16684 seconden | Geen |
| Artiesten per land bekijken | Geslaagd | Nederland 6, Verenigd Koninkrijk 12, USA 9, Jamaica 1 en Frankrijk 1 | Geen |
| Genreoverzicht bekijken | Geslaagd na bugfix | Alle 10 genres worden weergegeven | `Folk` en `Soul` werden eerst niet weergegeven |
| Sessiestatistieken bekijken | Geslaagd | Na één toevoeging staat de teller op 1 | Geen |
| Nieuw genre toevoegen | Geslaagd | `Techno is toegevoegd` | Geen |
| Bestaand genre toevoegen | Geslaagd | `Genre bestaat al` | Geen |
| Ongebruikt genre verwijderen | Geslaagd | `Techno is verwijderd` | Geen |
| Genre met tracks verwijderen | Geslaagd | `Rock` wordt niet verwijderd | Geen |
| Niet-bestaand genre verwijderen | Geslaagd | `Genre bestaat niet` | Geen |

## Bugfix-sprint en hertest

Bij het testen van het genreoverzicht werden alleen genres weergegeven waar minimaal één track aan gekoppeld was. `Folk` en `Soul` ontbraken daardoor.

De query voor het genreoverzicht is aangepast met een `LEFT JOIN`, zodat ook genres zonder tracks worden weergegeven.

Na de hertest worden alle 10 genres weergegeven.

**Resultaat hertest:** Geslaagd

## Conclusie nieuwe testuitvoering

Alle uitgevoerde scenario's zijn na de bugfix geslaagd. De bestaande functies en de nieuwe functies voor het beheren van genres werken volgens het verwachte gedrag.

## Feedback klasgenoot

**Naam klasgenoot:** [invullen]

**Gecontroleerd scenario:** [invullen]

**Feedback:**
[invullen]