# Testplan: Platenbak

## Voorbereiding

Voor alle testcases wordt de volgende voorbereiding verwacht:

* Zorg dat de juiste tabellen zijn aangemaakt in de database (`genre`, `artiest`, `track`).
* Verwijder eventueel alle aanwezige data in de database.
* Zorg dat de standaard testdata is ingeladen met [db/inserts.sql](db/inserts.sql).

---

## UC1: Testen "Nieuwe track toevoegen"

### Testscenario: Succesvolle toevoeging van nieuwe track

**Precondities:**
* De artiest `Kayak` bestaat in de database.
* Het genre `Rock` bestaat in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 1 ("Track toevoegen").
3. Voer in:
   * **Artiest:** `Kayak`
   * **Titel:** `Frozen Flame`
   * **Genre:** `Rock`
   * **Duur:** `240`
   * **Jaar:** `2000`

**Verwacht resultaat:**
* Het systeem toont: `Frozen Flame is toegevoegd`.
* Het systeem verhoogt de sessieteller voor toegevoegde tracks met 1.
* In de database staat een nieuwe track met bovengenoemde gegevens.

**Resultaat:**
* Het returned: `Frozen Flame is toegevoegd`.

---

### Testscenario: Track toevoegen met onbekende artiest

**Precondities:**
* Het genre `Rock` bestaat in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 1 ("Track toevoegen").
3. Voer als artiest `BestaatNiet` in.
4. Vul de overige gegevens geldig in.

**Verwacht resultaat:**
* Het systeem toont `Artiest of genre bestaat niet`.
* De track wordt niet toegevoegd.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Track toevoegen met onbekend genre

**Precondities:**
* De artiest `Kayak` bestaat in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 1 ("Track toevoegen").
3. Voer als artiest `Kayak` in.
4. Voer als genre `BestaatNiet` in.
5. Vul de overige gegevens geldig in.

**Verwacht resultaat:**
* Het systeem toont `Artiest of genre bestaat niet`.
* De track wordt niet toegevoegd.

**Resultaat:**
* Geslaagd.

---

## UC10: Testen "Statistieken bekijken"

### Testscenario: Statistieken van de collectie bekijken

**Precondities:**
* De standaard testdata is aanwezig in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 5 ("Statistieken bekijken").

**Verwacht resultaat:**
* Het systeem toont het aantal tracks.
* Het systeem toont de gemiddelde duur van de tracks.
* Het systeem toont de totale duur van de tracks.
* De waarden komen overeen met de gegevens in de database.

**Resultaat:**
* Geslaagd.

---

## UC10: Testen "Artiesten per land bekijken"

### Testscenario: Artiesten groeperen per land

**Precondities:**
* De standaard testdata is aanwezig in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 6 ("Artiesten per land bekijken").

**Verwacht resultaat:**
* Elk land wordt één keer weergegeven.
* Bij ieder land wordt het aantal artiesten uit dat land weergegeven.
* De aantallen komen overeen met de gegevens in de database.

**Resultaat:**
* Geslaagd.

---

## UC11: Testen "Genreoverzicht bekijken"

### Testscenario: Tracks groeperen per genre

**Precondities:**
* De standaard testdata is aanwezig in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 7 ("Genreoverzicht bekijken").

**Verwacht resultaat:**
* Elk genre wordt één keer weergegeven.
* Bij ieder genre wordt het aantal tracks binnen dat genre weergegeven.
* Bij ieder genre wordt de totale duur van de tracks weergegeven.
* De aantallen en totale duur komen overeen met de gegevens in de database.

**Resultaat:**
* Geslaagd na hertest.

---

## UC4: Testen "Sessiestatistieken bekijken"

### Testscenario: Aantal toegevoegde en verwijderde tracks bij afsluiten

**Precondities:**
* De artiest `Kayak` bestaat in de database.
* Het genre `Rock` bestaat in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 1 ("Track toevoegen").
3. Voeg de track `Frozen Flame` van `Kayak` toe.
4. Verwijder een bestaande track.
5. Kies in het menu voor optie 0 ("Afsluiten").

**Verwacht resultaat:**
* Het systeem toont dat tijdens de huidige sessie 1 track is toegevoegd.
* Het systeem toont dat tijdens de huidige sessie 1 track is verwijderd.

**Resultaat:**
* Geslaagd.

---

## UC5 en UC6: Testen "Genres beheren"

### Testscenario: Nieuw genre toevoegen

**Precondities:**
* Het genre `Techno` bestaat nog niet in de database.

**Testscenario:**
1. Kies in het menu voor optie 9 ("Genre toevoegen").
2. Voer als naam `Techno` in.
3. Voer als omschrijving `Technomuziek` in.

**Verwacht resultaat:**
* Het systeem toont `Techno is toegevoegd`.
* Het genre staat in de database.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Bestaand genre toevoegen

**Precondities:**
* Het genre `Rock` bestaat in de database.

**Testscenario:**
1. Kies in het menu voor optie 9 ("Genre toevoegen").
2. Voer als naam `Rock` in.
3. Voer een omschrijving in.

**Verwacht resultaat:**
* Het systeem toont `Genre bestaat al`.
* Het genre wordt niet opnieuw toegevoegd.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Ongebruikt genre verwijderen

**Precondities:**
* Het genre `Techno` bestaat in de database.
* Er zijn geen tracks aan `Techno` gekoppeld.

**Testscenario:**
1. Kies in het menu voor optie 10 ("Genre verwijderen").
2. Voer `Techno` in.

**Verwacht resultaat:**
* Het systeem toont `Techno is verwijderd`.
* Het genre staat niet meer in de database.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Genre met tracks verwijderen

**Precondities:**
* Het genre `Rock` bestaat in de database.
* Er zijn tracks aan `Rock` gekoppeld.

**Testscenario:**
1. Kies in het menu voor optie 10 ("Genre verwijderen").
2. Voer `Rock` in.

**Verwacht resultaat:**
* Het systeem toont `Genre kan niet worden verwijderd omdat er tracks aan gekoppeld zijn`.
* Het genre blijft in de database.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Niet-bestaand genre verwijderen

**Testscenario:**
1. Kies in het menu voor optie 10 ("Genre verwijderen").
2. Voer `BestaatNiet` in.

**Verwacht resultaat:**
* Het systeem toont `Genre bestaat niet`.
* De database blijft ongewijzigd.

**Resultaat:**
* Geslaagd.

---

## UC2: Testen "Tracks bekijken"

### Testscenario: Alle tracks bekijken

**Precondities:**
* De standaard testdata is aanwezig in de database.

**Testscenario:**
1. Start de applicatie.
2. Kies in het menu voor optie 2 ("Tracks bekijken").

**Verwacht resultaat:**
* De tracks worden weergegeven met artiest, titel, genre, duur en jaar.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Tracks bekijken met lege collectie

**Precondities:**
* De tabel `track` is leeg.

**Testscenario:**
1. Kies in het menu voor optie 2 ("Tracks bekijken").

**Verwacht resultaat:**
* Het systeem toont `Er zijn geen tracks gevonden`.

**Resultaat:**
* Geslaagd.

---

## UC3: Testen "Tracks zoeken"

### Testscenario: Zoeken met resultaten

**Precondities:**
* De standaard testdata is aanwezig in de database.

**Testscenario:**
1. Kies in het menu voor optie 3 ("Tracks zoeken").
2. Voer als minimaal jaar `1970` in.
3. Voer als genre `Rock` in.

**Verwacht resultaat:**
* Alleen Rock-tracks uit 1970 of later worden weergegeven.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Zoeken zonder resultaten

**Precondities:**
* De standaard testdata is aanwezig in de database.

**Testscenario:**
1. Kies in het menu voor optie 3 ("Tracks zoeken").
2. Voer als minimaal jaar `3000` in.
3. Voer als genre `Rock` in.

**Verwacht resultaat:**
* Het systeem toont `Er zijn geen tracks gevonden`.

**Resultaat:**
* Geslaagd.

---

## UC7: Testen "Artiest toevoegen"

### Testscenario: Nieuwe artiest toevoegen

**Precondities:**
* De artiest `Test Artiest` bestaat nog niet in de database.

**Testscenario:**
1. Kies in het menu voor optie 4 ("Artiest toevoegen").
2. Voer als naam `Test Artiest` in.
3. Voer als land `Nederland` in.

**Verwacht resultaat:**
* Het systeem toont `Test Artiest is toegevoegd`.
* De artiest staat in de database.

**Resultaat:**
* Geslaagd.

---

## UC8: Testen "Track verwijderen"

### Testscenario: Bestaande track verwijderen

**Precondities:**
* `Ruthless Queen` van `Kayak` bestaat in de database.

**Testscenario:**
1. Kies in het menu voor optie 11 ("Track verwijderen").
2. Voer als artiest `Kayak` in.
3. Voer als titel `Ruthless Queen` in.

**Verwacht resultaat:**
* Het systeem toont `Ruthless Queen is verwijderd`.
* De track staat niet meer in de database.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Niet-bestaande track verwijderen

**Testscenario:**
1. Kies in het menu voor optie 11 ("Track verwijderen").
2. Voer als artiest `Kayak` in.
3. Voer als titel `BestaatNiet` in.

**Verwacht resultaat:**
* Het systeem toont `Track bestaat niet`.
* De database blijft ongewijzigd.

**Resultaat:**
* Geslaagd.

---

## UC9: Testen "Playlist samenstellen"

### Testscenario: Playlist samenstellen op tijd

**Precondities:**
* De standaard testdata is aanwezig in de database.

**Testscenario:**
1. Kies in het menu voor optie 12 ("Playlist samenstellen").
2. Voer `10` minuten in.

**Verwacht resultaat:**
* Het systeem toont willekeurige tracks.
* De totale duur is minimaal 600 seconden wanneer er voldoende tracks beschikbaar zijn.

**Resultaat:**
* Geslaagd.

---

### Testscenario: Playlist met ongeldige tijd

**Testscenario:**
1. Kies in het menu voor optie 12 ("Playlist samenstellen").
2. Voer `0` minuten in.

**Verwacht resultaat:**
* Het systeem toont `Tijd moet groter zijn dan 0`.
* Er wordt geen playlist samengesteld.

**Resultaat:**
* Geslaagd.

---

## Feedback klasgenoot

**Uitgevoerd scenario:** [invullen]

**Naam klasgenoot:** [invullen]

**Feedback:**
[invullen]

**Verwerking feedback:**
[invullen]

---

## Opmerkingen

* Testscenario's kunnen in willekeurige volgorde worden uitgevoerd, behalve wanneer een preconditie expliciet afhankelijk is van een eerder scenario.
* Bij foutscenario's moet de database ongewijzigd blijven.
* _Door de willekeur in playlistgeneratie kunnen exacte tracklijsten tussen testuitvoeringen verschillen; de duurgrens moet altijd gerespecteerd worden._