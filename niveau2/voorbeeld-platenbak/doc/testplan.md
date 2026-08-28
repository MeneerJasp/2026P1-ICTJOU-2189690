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
2. Kies in het menu voor optie 2 ("Nieuwe track toevoegen").
3. Voer in:
   * **Artiest:** `Kayak`
   * **Genre:** `Rock`
   * **Titel:** `Frozen Flame`
   * **Duur:** `240`
   * **Jaar:** `2000`

**Verwacht resultaat:**
* Het systeem toont een bevestiging: `Track 'Frozen Flame' van Kayak toegevoegd!`.
* Het systeem verhoogt de sessieteller voor toegevoegde tracks met 1.
* In de database staat een nieuwe track met bovengenoemde gegevens.



---

## Opmerkingen

* Testscenario's kunnen in willekeurige volgorde worden uitgevoerd, behalve wanneer een preconditie expliciet afhankelijk is van een eerder scenario.
* Bij foutscenario's moet de database ongewijzigd blijven.
* _Door de willekeur in playlistgeneratie kunnen exacte tracklijsten tussen testuitvoeringen verschillen; de duurgrens moet altijd gerespecteerd worden._
