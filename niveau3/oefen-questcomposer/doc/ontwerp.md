# Ontwerp Verlanglijstmanager

## Inleiding

Dit document beschrijft het ontwerp van Verlanglijstmanager. Dit ontwerp biedt de technische basis voor de realisatie van de applicatie.

## Technische eisen

### TE1. Data-integriteit
De applicatie maakt gebruik van een SQLite-database. Tabellen worden voorzien van primaire sleutels en waar nodig vreemde sleutels om relaties tussen scenario's en onderdelen af te dwingen. Budgetwaarden worden opgeslagen als numerieke datatypes en invoer wordt gevalideerd voordat deze wordt opgeslagen.

### TE2. Toegangsbeveiliging
Bij het opstarten van de applicatie moet de gebruiker een toegangscode invoeren. Alleen na succesvolle verificatie wordt toegang verleend tot de functionaliteiten van de applicatie.

### TE3. Bescherming van gevoelige configuratie
Gevoelige configuratiegegevens worden opgeslagen in een `.env`-bestand. Dit bestand wordt opgenomen in `.gitignore`, zodat het niet in versiebeheer terechtkomt. De applicatie leest deze waarden in via omgevingsvariabelen.

### TE4. Veilige opslag van toegangscode
De toegangscode wordt niet in platte tekst opgeslagen. Voor opslag en verificatie wordt een cryptografische hashfunctie gebruikt, zoals bcrypt of Argon2.

### TE5. Gebruikersinterface
De applicatie biedt een command-line interface (CLI) met duidelijke menuopties, invoerprompts en foutmeldingen. De gebruiker moet scenario's en onderdelen kunnen beheren zonder kennis van de interne datastructuur.

### TE6. Uitbreidbaarheid
De software wordt modulair opgebouwd met een scheiding tussen gebruikersinterface, bedrijfslogica en datalaag. Nieuwe functionaliteiten moeten kunnen worden toegevoegd zonder grote wijzigingen aan bestaande componenten.

### TE7. Budgetcontrole en haalbaarheidsanalyse
De applicatie berekent automatisch de totale kosten van een scenario op basis van de gekoppelde onderdelen. Tijdens het aanmaken of wijzigen van een scenario wordt het beschikbare budget vergeleken met de berekende kosten en wordt direct een melding gegeven wanneer het budget wordt overschreden.

### TE8. Uitvoerbaarheid
De applicatie wordt ontwikkeld in Python 3 en kan vanaf een standaard Linux-omgeving worden gestart via één terminalcommando. Externe afhankelijkheden worden vastgelegd in een `requirements.txt`-bestand.

### TE9. Gegevensportabiliteit
Bestandslocaties worden niet hardcoded in de broncode. De applicatie werkt met configureerbare bestandspaden en moet gegevens kunnen lezen en schrijven op verschillende opslaglocaties, waaronder andere schijven, externe opslagmedia en gemounte bestandssystemen.

## Tabelontwerp

De drie entiteittypen uit het domeinmodel worden de tabellen `Lijst`, `Winkel` en `Item`. In dit technische ontwerp heet het attribuut budget uit het domeinmodel `budget_limiet`, zoals in het bestaande `db/inserts.sql`.

### Lijst

| Kolom | Datatype | Sleutel | Leeg toegestaan? |
|---|---|---|---|
| naam | TEXT | `<pk>` | NOT NULL |
| budget_limiet | REAL | | NOT NULL |

### Winkel

| Kolom | Datatype | Sleutel | Leeg toegestaan? |
|---|---|---|---|
| naam | TEXT | `<pk>` | NOT NULL |
| verzendkosten | REAL | | NOT NULL |

### Item

| Kolom | Datatype | Sleutel | Leeg toegestaan? |
|---|---|---|---|
| lijst | TEXT | `<pk> <fk1>` | NOT NULL |
| titel | TEXT | `<pk>` | NOT NULL |
| prijs | REAL | | NOT NULL |
| winkel | TEXT | `<fk2>` | NULL |
| prioriteit | INTEGER | | NOT NULL |

De pijlen voor de relaties zijn:

- `Item.lijst <fk1>` → `Lijst.naam <pk>`
- `Item.winkel <fk2>` → `Winkel.naam <pk>`

`Item.lijst` hoort bij de samengestelde primary key van Item, omdat een item alleen binnen een lijst met zijn titel wordt geïdentificeerd. `Item.winkel` mag leeg zijn: volgens het interview is een winkel soms nog niet bekend.

## Afhankelijkheden

De applicatie "Verlanglijstmanager" is afhankelijk van de volgende bibliotheken:

- `csv` - Voor het importeren van items uit CSV-bestanden.
- `hashlib` - Voor het hashen van de toegangscode.


## Detailontwerp

De applicatie "Verlanglijstmanager" bestaat uit de onderstaande elementen.

### Globale variabelen module "Verlanglijstmanager"

- `sessiestatistieken` in `itembeheer.py`: Teller met aantallen toegevoegde en verwijderde items tijdens de huidige sessie.
- `STANDAARD_VERZENDKOSTEN` in `importbeheer.py`: Standaardwaarde voor verzendkosten bij nieuw aangemaakte winkels via CSV-import.
- `STANDAARD_LIJSTBUDGET` in `importbeheer.py`: Standaardbudget voor nieuw aangemaakte lijsten via CSV-import.

### Software-architectuur
[Opstellen Software-architectuurdiagram]


### Functies module "verlangslijstmanager.py"

- `maak_verbinding()`: Maakt een SQLite-verbinding met `db/verlanglijstmanager.db`, activeert foreign keys en retourneert de verbinding.
- `toon_menu()`: Toont het hoofdmenu en vraagt de gebruiker om een keuze.
- `main()`: Start de applicatie, controleert toegangscode, maakt de databaseverbinding en stuurt de menu-acties aan.

### Overige functies

[Deze lijst is niet compleet, en de functies moeten nog verdeeld worden over de modules]

- `haal_alle_items_op(verbinding)`: Haalt alle items op inclusief winkel- en lijstnaam via een JOIN-operatie.
- `haal_lijsten_op(verbinding)`: Haalt alle lijsten op inclusief budget.
- `update_prijs(verbinding, lijstnaam, titel, nieuwe_prijs)`: Past de prijs van een item aan.
- `verwijder_item_uit_db(verbinding, lijstnaam, titel)`: Verwijdert een item op basis van lijst en titel.
- `voeg_item_toe_aan_db(verbinding, titel, prijs, winkel_naam, lijst_naam, prio)`: Voegt een item toe aan de tabel `Item`.
- `haal_items_binnen_budget(verbinding, min_budget, max_budget)`: Haalt items op binnen een budgetrange.
- `check_winkel_bestaat(verbinding, winkelnaam)`: Controleert of een winkel bestaat.
- `toon_beschikbare_verlanglijsten(verbinding)`: Toont beschikbare lijsten voor gebruikerskeuze.
- `kies_verlanglijst(verbinding)`: Laat de gebruiker een lijst selecteren op nummer.
- `toon_verlanglijst(verbinding)`: Toont de volledige verlanglijst inclusief totaalprijs per item.
- `voeg_item_toe(verbinding)`: Registreert handmatig een nieuw item.
- `toon_items_binnen_budget(verbinding)`: Toont items tussen twee budgetgrenzen.
- `pas_itemprijs_aan(verbinding)`: Past de prijs van een geselecteerd item aan.
- `verwijder_item(verbinding)`: Verwijdert een geselecteerd item.
- `haal_verlanglijst_op(verbinding)`: Haalt items op inclusief winkel- en lijstnaam.
- `haal_lijsten_op(verbinding)`: Haalt alle lijsten op met budget.
- `haal_prijzen_op_van_lijst(verbinding, lijstnaam)`: Haalt alle itemprijzen op voor een lijst.
- `update_lijstbudget(verbinding, lijstnaam, nieuw_budget)`: Werkt het budget van een lijst bij.
- `bereken_spaarplan(verbinding)`: Toont een persoonlijk spaarplan op basis van itemprijs en maanden.
- `pas_lijstbudget_aan(verbinding)`: Vraagt een nieuw budget en slaat dit op.
- `toon_overzicht_per_lijst(verbinding)`: Toont statistieken en budgetcontrole per lijst.