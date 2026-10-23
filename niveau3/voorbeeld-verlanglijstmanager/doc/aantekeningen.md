## Kwaliteitseisen Use Cases

- De actor en precondities zijn duidelijk.
- De normale flow beschrijft stap voor stap wat de gebruiker en het systeem doen.
- Een alternatieve flow verwijst naar de stap waar het anders loopt.
- Bij een fout is duidelijk welke melding volgt, of de use case stopt en of gegevens veranderen.

## Kwaliteitseisen testplan

- Elk scenario heeft een concrete voorbereiding of preconditie.
- De invoer en de uit te voeren stappen zijn duidelijk.
- Het verwachte resultaat is controleerbaar, ook in de opgeslagen gegevens.
- De normale flow en de alternatieve flows uit de Use Case hebben testscenario's.

## Voorstel kwaliteitseisen domeinmodellen (nog met de groep bespreken)

1. De entiteittypen komen uit de casus en hebben duidelijke namen.
2. Attributen staan bij het entiteittype waar ze bij horen.
3. Elk entiteittype heeft een primary identifier; die is onderstreept.
4. Een zwak entiteittype heeft een complete identificatie via zijn eigen attribuut en het entiteittype waarvan het afhankelijk is.
5. Relaties hebben een naam en verbinden de juiste entiteittypen.
6. Bij beide kanten van elke relatie staat de minimale en maximale kardinaliteit.
7. Verplichte en optionele relaties kloppen met het interview en de voorbeelden.
8. Het model bevat geen technische koppelingattributen of databasetermen.
9. Het model is leesbaar en gebruikt overal dezelfde notatie.

## Oefening kunstacademie (voorbeeld om samen te bespreken)

- Afstudeerwerk: titel (primary identifier), type, naam maker en optioneel beschrijving.
- Afbeelding: volgnummer (deel van de identificatie) en bestandsnaam.
- Een afstudeerwerk heeft 1 of meer afbeeldingen; een afbeelding hoort bij precies 1 afstudeerwerk.
- Afbeelding is zwak: afstudeerwerktitel en volgnummer identificeren samen een afbeelding. De pijl loopt van Afbeelding naar Afstudeerwerk.

## Les 3.4 - Increment 2 en Python modules

### Vraag: Waarom komt User Story 9 (totale kosten = prijs + verzendkosten) in drie Use Cases voor?

Omdat de totale kosten niet een losse menu-optie zijn, maar een berekening die op meerdere plekken nodig is om goede financiele keuzes te maken:
- Bij **UC5 (Zoeken op budget)** om te zien wat een item echt kost binnen je restbudget.
- Bij **UC6 (Persoonlijk spaarplan berekenen)** om het juiste totaalbedrag te sparen.
- Bij **UC7 (Uitgaven per lijst inzien)** om te controleren of het totaalbedrag inclusief verzendkosten het lijstbudget overschrijdt.

### Use Case-matrix Increment 2 QuestComposer

| User Story | UC5 | UC6 | UC7 | UC8 |
|---|---|---|---|---|
| **US6.** (Totale kosten: prijs + transportkosten) | X | X | X | |
| **US7.** (Kosten per scenario en budgetoverschrijding) | | | X | |
| **US8.** (Onderdelen zoeken binnen prijsrange) | X | | | |
| **US9.** (Maandelijks inkoopritme voor sleutelonderdeel) | | X | | |
| **US10.** (Sessieoverzicht bij afsluiten) | | | | X |

### Orientatie op Python modules

**Drie problemen als alle functies in een enkel bestand staan:**
1. **Slecht overzicht:** Het bestand wordt erg lang, waardoor je lang moet scrollen en moeilijk terugvindt waar een bepaalde functie staat.
2. **Lastiger te onderhouden:** Functies voor verschillende onderdelen (zoals klanten, bestellingen, facturen en de database) staan door elkaar. Bij een aanpassing maak je sneller fouten in andere onderdelen.
3. **Lastig samenwerken in Git:** Als meerdere groepsleden tegelijk in hetzelfde grote bestand werken, ontstaan er snel merge-conflicten.

**Oplossing:**
De code opsplitsen in aparte Python-bestanden (modules) per onderwerp, bijvoorbeeld `klantbeheer.py`, `bestellingbeheer.py`, `factuurbeheer.py` en een hoofdmodule voor het menu. Met `import` kun je de functies vanuit de hoofdmodule aanroepen.

## Les 3.5 - Software Architectuur, import en SQL

### Wat is een module in Python?
Een module is een los Python-bestand (met de extensie `.py`) waarin functies en variabelen staan die bij hetzelfde onderwerp horen. Door die module te importeren in een ander bestand kun je de code hergebruiken en blijft het hoofdprogramma overzichtelijk.

**Waar moet je op letten bij het maken van een module (zoals `belasting.py`)?**
- **De naam:** Een duidelijke naam in kleine letters zonder spaties (en niet dezelfde naam als een standaard Python-module).
- **De plek:** Het bestand moet in dezelfde map (`src/`) staan als het hoofdprogramma, zodat Python het bestand kan vinden.
- **De import:** Bovenaan in `main.py` zet je `import belasting` (aanroep: `belasting.bereken_btw(100)`) of `from belasting import bereken_btw` (aanroep: `bereken_btw(100)`).

### Indeling van de voorbeeldfuncties in 5 modules

1. **`main.py` (Hoofdmodule):**
   - `start_applicatie()`
   - `toon_menu()`
   - `maak_verbinding()`
2. **`klantbeheer.py`:**
   - `voeg_klant_toe(klanten, klantgegevens)`
   - `zoek_klant(klanten, klant_id)`
3. **`bestellingbeheer.py`:**
   - `maak_bestelling(klant_id, producten)`
   - `annuleer_bestelling(bestelling_id)`
   - `beheer_voorraad(producten, product_id, wijziging)`
4. **`factuurbeheer.py`:**
   - `maak_factuur(bestelling_id)`
   - `bereken_btw(bedrag, btw_percentage)`
5. **`rapportagebeheer.py`:**
   - `toon_omzet(bestellingen, periode)`
   - `haal_statistieken_op_uit_database(verbinding)`

### Overzicht importvormen

| Importvorm in `main.py` | Aanroep in `main.py` | Voordeel | Nadeel |
|---|---|---|---|
| `import belasting` | `belasting.bereken_btw(100)` | Je ziet direct uit welke module de functie komt. | Je moet steeds de modulenaam ervoor typen. |
| `from belasting import bereken_btw` | `bereken_btw(100)` | Kortere aanroep en je ziet bovenin precies welke functie gebruikt wordt. | Kans op naamconflict als `main.py` zelf ook een functie met die naam heeft. |
| `from belasting import *` | `bereken_btw(100)` | Alles uit de module is in een keer beschikbaar. | Onoverzichtelijk: je ziet niet meer waar functies vandaan komen en namen kunnen elkaar overschrijven. |
| `import belasting as bel` | `bel.bereken_btw(100)` | Korter typen bij lange modulenamen en toch duidelijk waar het vandaan komt. | Een onduidelijke afkorting maakt de code minder leesbaar. |
| `from belasting import bereken_btw as btw` | `btw(100)` | Handig om een lange functienaam in te korten of een naamconflict op te lossen. | De functie heet in `main.py` anders dan in `belasting.py`, wat verwarrend kan zijn. |

### Foutmeldingen bij importeren

- **`ModuleNotFoundError: No module named 'belasting'`**: Het bestand `belasting.py` bestaat niet, heeft een spelfout in de bestandsnaam of staat in een verkeerde map. Oplossing: controleer de bestandsnaam en zorg dat het in dezelfde map staat.
- **`ImportError: cannot import name 'bereken_btw' from 'belasting'`**: De module `belasting.py` bestaat wel, maar de functie `bereken_btw` staat er niet in (of is verkeerd gespeld). Oplossing: controleer de functienaam in `belasting.py`.
- **`NameError: name 'bereken_btw' is not defined`**: Je roept `bereken_btw(100)` direct aan terwijl je helemaal niets hebt geimporteerd, of alleen `import belasting` hebt gedaan (dan moet het `belasting.bereken_btw(100)` zijn).
- **`SyntaxError: invalid syntax`**: Er zit een schrijffout in het `import`-statement zelf (bijvoorbeeld `import from belasting`). Oplossing: verbeter de Python-syntax.
- **`AttributeError: module 'belasting' has no attribute 'bereken_btw'`**: Je hebt `import belasting` gedaan en roept `belasting.bereken_btw(100)` aan, maar die functie bestaat niet in `belasting.py`. Oplossing: controleer de functienaam in `belasting.py`.
- **Circulaire import (module A doet `import B` en module B doet `import A`)**: Python raakt in een cirkel terecht tijdens het inladen, waardoor een module nog niet volledig geladen is als de andere er al een functie uit probeert te gebruiken (`ImportError` of `AttributeError`). Oplossing: zorg dat de aanroepen maar een kant op gaan (vanuit de hoofdmodule naar de sub-modules).

### Kwaliteitseisen voor Software Architectuur

- Als er pijlen heen en weer gaan tussen modules, zijn de modules onderling afhankelijk van elkaar. Dit is niet verstandig en heet **spaghetticode**.
- **Kwaliteitseisen:**
  1. Elke module bevat alleen functies die logisch bij hetzelfde onderwerp horen.
  2. Er is een duidelijke hoofdmodule die de andere modules aanroept.
  3. Pijlen lopen van boven naar beneden (geen circulaire imports of pijlen heen en weer tussen alle modules).
  4. Modules en functies hebben duidelijke Nederlandse namen.

### SQL WHERE met BETWEEN, LIKE en IN

**1. BETWEEN:**
- Vraag: Tellen items met een prijs van 10 en 50 mee bij `WHERE prijs BETWEEN 10 AND 50`?
- Antwoord: **Ja**, `BETWEEN` is inclusief de ondergrens (10) en de bovengrens (50).

**2. LIKE oefeningen:**
```sql
-- Alle items waarvan de naam eindigt op 'er'
SELECT *
FROM Item
WHERE titel LIKE '%er';

-- Alle items waarvan de naam 'a' bevat
SELECT *
FROM Item
WHERE titel LIKE '%a%';

-- Alle items waarvan de naam precies 5 tekens lang is
SELECT *
FROM Item
WHERE titel LIKE '_____';

## Voorbereiding Les 6 - UC7, UC8 en INNER JOIN over drie tabellen

### Vergelijking UC7 en UC8 (Verlanglijstmanager vs QuestComposer)

**Use Case 7 (Uitgaven per lijst inzien vs Haalbaarheid per scenario inzien):**
- **Hetzelfde:** Beide use cases tonen per groep (lijst of scenario) het aantal items/onderdelen, de laagste prijs, de hoogste prijs, de gemiddelde prijs, het totaalbedrag inclusief bijkomende kosten (verzendkosten of transportkosten), het budget en een waarschuwing als het budget wordt overschreden.
- **Anders:** De entiteiten en termen verschillen: Verlanglijstmanager gebruikt `Lijst`, `Item` en `Winkel` (met `verzendkosten`), terwijl QuestComposer `Scenario`, `Onderdeel` en `Leverancier` (met `transportkosten`) gebruikt.
- **Benodigde SQL-SELECT-componenten:** `SELECT`, aggregatiefuncties (`COUNT`, `MIN`, `MAX`, `AVG`, `SUM`), `JOIN` over drie tabellen, `GROUP BY` en `ORDER BY`.

**Use Case 8 (Afsluiten met sessiestatistieken):**
- **Hetzelfde:** Beide tonen bij het kiezen van optie 8 een afsluitbericht, het aantal toegevoegde en verwijderde items/onderdelen tijdens de huidige sessie, en sluiten daarna het programma af.
- **Anders:** Alleen de tekst van het afsluitbericht en het woord "items" vs "onderdelen".
- **Soort Python-variabelen:** Een **globale variabele** (bijvoorbeeld een dictionary `sessiestatistieken = {'toegevoegd': 0, 'verwijderd': 0}`), zodat de tellers gedurende de hele sessie bewaard blijven en vanuit meerdere functies/modules aangepast en uitgelezen kunnen worden.

### Vragen bij INNER JOIN over drie tabellen (Muziekdatabase)

**Voorbeeld 1 (join tussen A en B en tussen B en C: `Stuk` -> `Componist` -> `Muziekschool`):**
- **Waarom staat alleen bij `B.naam`, `B.schoolId` en `C.naam` de alias ervoor?**
  Omdat de kolomnamen `naam` en `schoolId` in meerdere gekoppelde tabellen voorkomen (`Componist` en `Muziekschool` hebben allebei een kolom `naam` en `schoolId`). Zonder alias weet SQL niet welke kolom je bedoelt. De andere kolommen (`stuknr`, `titel`, `plaatsnaam`) komen maar in een tabel voor.
- **Wat gebeurt er als een componist geen `schoolId` heeft (`NULL`)?**
  Dan worden die componist en alle stukken van die componist **niet** getoond in het resultaat, omdat een `INNER JOIN` alleen rijen toont die in alle gekoppelde tabellen een overeenkomst hebben.

**Voorbeeld 2 (join tussen A en B en tussen A en C: `Stuk` -> `Componist` en `Stuk` -> `Niveau`):**
- **Waarom staat alleen bij `A.niveaucode` de alias ervoor?**
  Omdat `niveaucode` zowel in tabel `Stuk` (`A`) als in tabel `Niveau` (`C`) voorkomt. De overige gevraagde kolommen komen in deze drie tabellen maar een keer voor (`Componist` heeft `naam`, `Niveau` heeft `omschrijving`).
- **Wat gebeurt er als een stuk geen `niveaucode` heeft (`NULL`)?**
  Dan wordt dat stuk **niet** getoond in het resultaat, omdat `INNER JOIN Niveau` vereist dat `A.niveaucode` overeenkomt met een bestaande `C.niveaucode`.

### Opdracht: SELECT query over drie tabellen voor Verlanglijstmanager

> Geef van alle items de titel, de prijs, de lijstnaam, de winkelnaam en van de lijst de bijbehorende budget_limiet en van de winkel de verzendkosten.

```sql
SELECT
    Item.titel,
    Item.prijs,
    Item.lijst AS lijstnaam,
    Item.winkel AS winkelnaam,
    Lijst.budget_limiet,
    Winkel.verzendkosten
FROM Item
INNER JOIN Lijst ON Item.lijst = Lijst.naam
INNER JOIN Winkel ON Item.winkel = Winkel.naam;
```

---

# Niveau 3, les 6 - Besturingssysteem, Bootproces en GROUP BY

## 1. Besturingssysteem en bootproces

### Stap 1 en 2: Zeven apparaten en hun kenmerken

| Nr. | Apparaat | Is het een computer? | Type systeem (Klassiek OS / Embedded OS / Firmware) |
|---|---|---|---|
| 1 | Laptop | Ja | Klassiek besturingssysteem (Windows / Linux / macOS) |
| 2 | Smartphone | Ja | Klassiek/mobiel besturingssysteem (Android / iOS) |
| 3 | Smartwatch | Ja | Embedded besturingssysteem (Wear OS / watchOS / FreeRTOS) |
| 4 | Wi-Fi router | Ja | Embedded besturingssysteem (vaak embedded Linux zoals OpenWrt) |
| 5 | Printer | Ja | Embedded besturingssysteem of uitgebreide firmware |
| 6 | Magnetron | Ja (microcontroller) | Alleen firmware (vast programma op een chip) |
| 7 | Auto-ECU (motormanagement) | Ja (microcontroller) | Firmware / Real-Time Embedded OS (RTOS) |

### Stap 3 - Groepsopdrachten

#### Opdracht A - Wat is een OS?

- **Wel een besturingssysteem:** Windows, Linux, Android, macOS, iOS.
- **Geen besturingssysteem:**
  - *Raspberry Pi*: Dit is hardware (een single-board computer) waarop je een OS zoals Raspberry Pi OS (Linux) installeert.
  - *Arduino*: Dit is een microcontrollerbordje zonder besturingssysteem; je zet er rechtstreeks gecompileerde code (firmware) op.
  - *Firefox, WhatsApp, Word*: Dit zijn applicaties (toepassingsprogramma's) die bovenop een besturingssysteem draaien.

#### Opdracht B - BIOS, UEFI, bootloader en kernel

**Logische opstartvolgorde:**
1. Firmware (algemene naam voor software op het moederbord: BIOS of UEFI)
2. BIOS / UEFI
3. Bootloader (bijv. GRUB of Windows Boot Manager)
4. Kernel (de kern van het besturingssysteem)
5. OS-services (achtergrondprocessen en drivers)
6. Gebruikersomgeving (login-scherm, desktop of terminal/shell)
7. Interpreter (Python interpreter `python3`)
8. Python-code (`verlanglijstmanager.py`)

**Verschil tussen BIOS en UEFI:**
- **BIOS** is het oudere opstartsysteem dat werkt met een tekstscherm (16-bit modus) en opstart via de MBR (Master Boot Record) met een limiet van ongeveer 2 TB per schijf.
- **UEFI** is de moderne opvolger van BIOS met ondersteuning voor grotere schijven via GPT (GUID Partition Table), snellere opstarttijden, Secure Boot en vaak een grafische interface met muisondersteuning.

#### Opdracht C - Bootproces ordenen

1. `power on`
2. `BIOS/UEFI check (POST)` (Power-On Self-Test controleert of geheugen, CPU en opslag aanwezig zijn)
3. `boot device kiezen` (bijv. SSD of USB-stick)
4. `bootloader` (startlader op de schijf wordt geladen)
5. `kernel laden` (de kern van het besturingssysteem wordt in het RAM-geheugen geladen)
6. `drivers/services starten` (hardware-aansturing en systeemdiensten starten op)
7. `login-scherm` (gebruiker kan inloggen)

#### Opdracht D - Zonder klassiek OS?

- **Magnetron:** Vooral **firmware** (een microcontroller voert een vaste loop uit voor tijd, vermogen en knopjes).
- **Router:** **Embedded OS** (vaak een kleine Linux-versie die netwerkverkeer, firewall en wifi regelt).
- **Printer:** **Embedded OS** of **firmware** (afhankelijk van hoe slim de printer is; netwerkprinters met touchscreen draaien een embedded OS).
- **Smartwatch:** **Embedded OS** (speciaal energiezuinig besturingssysteem voor horloges).
- **Auto-ECU:** **Firmware / RTOS** (moet binnen milliseconden reageren op sensoren voor brandstofinjectie en ontsteking).
- **Je telefoon:** **Klassiek (mobiel) OS** (Android of iOS met app-installatie, geheugenbeheer en gebruikersaccounts).
- **Je laptop:** **Klassiek OS** (Windows, Linux of macOS).

---

## 2. Python -> interpreter -> OS -> hardware

### Stap 1 - De keten per voorbeeld

1. **`print("Hallo")`**
   - Python-code (`print("Hallo")`) -> Python-interpreter (vertaalt `print` naar een systeemaanroep / `write` syscall) -> Besturingssysteem / Kernel (stuurt de tekst via de grafische driver of terminal-driver aan) -> Hardware (beeldscherm toont `Hallo`).
2. **`x = 3 + 4`**
   - Python-code (`x = 3 + 4`) -> Python-interpreter (vertaalt de optelling naar bytecode en machine-instructies) -> Besturingssysteem (wijst CPU-tijd en werkgeheugen toe aan het Python-proces) -> Hardware (de ALU in de CPU telt 3 en 4 op en slaat 7 op in het RAM-geheugen).
3. **`input("Naam?")`**
   - Python-code (`input("Naam?")`) -> Python-interpreter (vraagt het OS om tekst te tonen en te wachten op toetsenbordinvoer via een `read` syscall) -> Besturingssysteem / Drivers (leest de toetsaanslagen van de toetsenbord-driver en geeft ze bij Enter door aan de interpreter) -> Hardware (toetsenbord en beeldscherm).

### Uitleg in eigen woorden

- **Wat doet de interpreter?** De Python-interpreter leest jouw `.py`-bestand, controleert de syntax en vertaalt de Python-instructies stap voor stap (via bytecode) naar systeemaanroepen en machine-instructies die het besturingssysteem en de CPU begrijpen.
- **Wat doet het OS?** Het besturingssysteem beheert de hardwarebronnen (CPU-tijd, RAM-geheugen, schijven, scherm en toetsenbord) en zorgt ervoor dat verschillende programma's veilig en tegelijk kunnen draaien zonder elkaar in de weg te zitten.
- **Waarom zijn drivers nodig?** Er bestaan duizenden verschillende merken en modellen toetsenborden, schermen, netwerkkaarten en schijven. Een driver is het vertaalstukje tussen het besturingssysteem en een specifiek stuk hardware, zodat het OS niet voor elk merk aparte code hoeft te bevatten.

### Stap 2 - Hoe zit dit met onze virtuele machine (VM)?

- **Welk OS draait daar?** In onze virtuele machine draait **Linux** (bijvoorbeeld Fedora of Ubuntu) als *guest OS*, bovenop het *host OS* (zoals Windows of macOS) van de laptop.
- **Hoe ziet de complete keten er dan uit?**
  Python-code -> Python-interpreter -> Guest OS (Linux in de VM) -> Virtuele hardware / Hypervisor (bijv. VirtualBox of VMware) -> Host OS (bijv. Windows) -> Drivers -> Fysieke hardware (echte CPU, RAM, SSD en scherm van de laptop).

---

## 3. Herhaling GROUP BY en statistische functies (Verlanglijstmanager)

1. **Geef van elke lijst de lijstnaam en het aantal items dat in die lijst staat. Lijsten zonder items hoeven niet getoond.**
```sql
SELECT Lijst.naam AS lijstnaam, COUNT(Item.titel) AS aantal_items
FROM Lijst
INNER JOIN Item ON Item.lijst = Lijst.naam
GROUP BY Lijst.naam;


---

# Niveau 3, les 6 - Samen & Zelf + Voorbereiding Les 7

## 1. Samen nadenken over de les (SQL GROUP BY vs. Python-loop)

1. **Hoeveel SQL-queries worden er in de tweede oplossing uitgevoerd?**
   - Er worden **`1 + N`** SQL-queries uitgevoerd, waarbij `N` het aantal lijsten in de tabel `Lijst` is. Eerst wordt 1 query uitgevoerd om alle lijsten op te halen, en daarna wordt in de `for`-loop voor elke lijst nog eens een aparte `SELECT`-query uitgevoerd (bij 10 lijsten dus 11 queries; bij 1000 lijsten 1001 queries).
2. **Welke oplossing vind je makkelijker? Waarom?**
   - De tweede oplossing oogt voor een beginnende Python-programmeur vaak simpeler omdat de `SELECT`-queries heel kort zijn, maar de eerste oplossing is uiteindelijk overzichtelijker zodra je `JOIN` en `GROUP BY` kent, omdat je in Python alleen nog maar de resultaten hoeft te printen.
3. **Welke oplossing is efficienter? Waarom?**
   - De **eerste oplossing** (met 1 `JOIN`- en `GROUP BY`-query) is veel efficienter. De database-engine is speciaal geoptimaliseerd om tabellen te koppelen en sommen te berekenen, en Python hoeft maar 1 keer met de database te communiceren in plaats van `1 + N` keer.
4. **Ben jij meer een database- of een Python-programmeur? Waarom?**
   - Ik combineer het liefst beide: rekenwerk over tabellen (zoals filteren met `WHERE`, koppelen met `JOIN` en groeperen met `GROUP BY`) laat ik door de database doen, en de gebruikersinteractie (menuss, validatie en weergave) programmeer ik in Python.

---

## 2. Voorbereiding op Les 7: USB-stick in Linux en UTF-8

### USB-stick gebruiken en mounten in een Linux VM

1. **USB-stick doorgeven aan de VM:** Koppel in het menu van je Virtual Machine (bijv. VirtualBox -> *Devices* -> *USB*) de ingeplugde USB-stick aan de Linux-VM.
2. **Schijven en partities bekijken:**
   ```bash
   lsblk
    ```


---

# Niveau 3, les 7 - Werking van een Operating System en Processen

## 1. De Python-module `os`

Met de standaardmodule `os` kan een Python-programma informatie opvragen bij het besturingssysteem en werken met mappen en bestanden:

- `os.name`: Geeft de naam van de besturingssysteem-familie terug.
- `os.getcwd()`: Geeft de huidige werkmap (*current working directory*) terug.
- `os.listdir()`: Geeft een lijst met alle bestanden en mappen in de huidige werkmap.
- `os.cpu_count()`: Geeft het aantal beschikbare logische processorkernen (cores) terug.
- `os.getpid()`: Geeft het unieke **PID** (*Process ID*) van het huidige draaiende Python-proces terug.

### Vraag: Waarom geeft `os.name` `'posix'` terug in Linux? Wat geeft het terug in Windows?

- **In Linux (en macOS):** `os.name` geeft `'posix'` terug. **POSIX** (*Portable Operating System Interface*) is een familie van standaarden voor Unix-achtige besturingssystemen. Omdat Linux deze standaard volgt voor processen, bestanden en rechten, valt Linux onder `'posix'`.
- **In Windows:** `os.name` geeft `'nt'` terug. Dat verwijst naar de **Windows NT**-architectuur (*New Technology*) waarop alle moderne versies van Windows zijn gebouwd.

---

## 2. Processen bekijken en beheren in Linux (`ps`, `top` en `kill`)

- Een **proces** is een programma dat op dat moment in uitvoering is. Elk proces krijgt van de kernel een uniek **PID** (*Process ID*).
- Handige Linux-commandos voor procesbeheer:
  - `ps aux` of `ps -ef`: Toont een momentopname van alle draaiende processen.
  - `top`: Toont een interactief real-time overzicht van alle processen, CPU-gebruik en geheugengebruik (afsluiten met `q`).
  - `kill <PID>`: Stuurt een beindigingssignaal (`SIGTERM`) naar het proces met het opgegeven PID.

### Vraag: Met welk Windows-onderdeel is `top` te vergelijken?

- `top` is in Windows direct te vergelijken met **Taakbeheer** (*Task Manager*, te openen met `Ctrl+Shift+Esc`).

### Opdracht: Wat gebeurt er als je Verlanglijstmanager beeindigt met `kill <PID>`?

1. Wanneer je `python3 niveau3/voorbeeld-verlanglijstmanager/src/verlanglijstmanager.py` start, wacht het programma op invoer in het menu (`Maak een keuze: `).
2. In een tweede terminal zoek je met `top` of `ps aux | grep python3` het PID van dit Python-proces op.
3. Zodra je in de tweede terminal `kill <PID>` uitvoert, stuurt het besturingssysteem een `SIGTERM`-signaal naar het Python-proces.
4. In de eerste terminal (waar Verlanglijstmanager draaide) stopt het programma onmiddellijk, verschijnt de melding **`Terminated`** (of **`Beeindigd`**), en keert de terminal direct terug naar de normale Linux-opdrachtprompt.


---

# Niveau 3, les 7 - Samen & Zelf (Voorbereiding Les 8: .env en Hashing)

## 1. Waarom mag een toegangscode nooit in de broncode staan?

- **Vraag: Waarom is `if toegangscode != "geheim":` in de Python-code niet veilig? Hoe kunnen anderen in de code kijken en de toegangscode zien?**
  - Python-bestanden (`.py`) zijn gewone tekstbestanden die voor iedereen met toegang tot de map of de Git-repository (zoals GitLab of GitHub) direct te openen en te lezen zijn. Zelfs als je de code later aanpast, blijft de oude toegangscode in de Git-commitgeschiedenis (`git log`) zichtbaar. Daarmee overtreed je direct **C3. Security** (gevoelige gegevens mogen niet zichtbaar zijn in de broncode).

## 2. Het `.env`-bestand uitlezen in Python

- **Vraag: Wat gebeurt er op de regel `return regel.replace('TOEGANGSCODE=', '')`?**
  - De functie heeft een regel gevonden die begint met `'TOEGANGSCODE='` (bijvoorbeeld `'TOEGANGSCODE=geheim'`). Met `.replace('TOEGANGSCODE=', '')` wordt het voorstuk `'TOEGANGSCODE='` vervangen door een lege string `''`, zodat alleen de waarde achter het `=`-teken (`'geheim'`) overblijft en wordt teruggegeven.
- **Vraag: Voldoen we met `TOEGANGSCODE=geheim` in `.env` (en `.env` in `.gitignore`) aan de User Concerns C2, C3 en C4? Waarom wel of niet?**
  - **C2 (Toegangscode bij starten):** Ja, de applicatie vraagt om een toegangscode.
  - **C3 (Niet zichtbaar in broncode):** Ja, de toegangscode staat niet meer in de `.py`-broncode of in GitLab.
  - **C4 (Veilig verwerkt en opgeslagen):** **Nee**, nog niet. De toegangscode staat nog als leesbare platte tekst (*plain text*) in het `.env`-bestand op de schijf. Iedereen die op de computer in het `.env`-bestand kijkt, ziet direct het wachtwoord.

---

## 3. Hashing van de toegangscode

### Wat is hashing en hoe werkt het?

- **Hashing** zet een invoer (zoals een wachtwoord of toegangscode) via een wiskundige functie om in een reeks tekens van een vaste lengte: de **hash**.
- Een goede cryptografische hashfunctie heeft drie belangrijke eigenschappen:
  1. **Deterministisch:** Dezelfde invoer levert altijd exact dezelfde hash op.
  2. **Eenrichtingsverkeer (One-way):** Je kunt van een wachtwoord wel de hash berekenen, maar je kunt vanuit de hash **nooit** terugrekenen wat het oorspronkelijke wachtwoord was.
  3. **Avalanche-effect:** Als er maar 1 letter in de invoer verandert, ziet de hele hash er compleet anders uit.

### Verschil tussen hashing en encryptie

- **Encryptie (versleuteling)** is **tweerichtingsverkeer**: je versleutelt data met een sleutel zodat je het later met een sleutel weer kunt ontsleutelen naar de originele tekst (bijvoorbeeld bij HTTPS-verkeer of het versleutelen van een harde schijf).
- **Hashing** is **eenrichtingsverkeer**: er is geen sleutel om een hash weer terug te draaien naar de originele tekst. Om een wachtwoord te controleren, hash je het zojuist ingetypte wachtwoord opnieuw en vergelijk je de twee hashes met elkaar.

### Drie voorbeelden van veelgebruikte hash-algoritmes

1. **SHA-256 (Secure Hash Algorithm 256-bit):**
   - Maakt altijd een hash van 64 hexadecimale tekens (256 bits).
   - **Toepassing:** Controleren of gedownloade bestanden niet aangepast zijn (checksums), digitale handtekeningen, en in ons project het hashen van de toegangscode met `hashlib.sha256(...).hexdigest()` voor opslag in het `.env`-bestand.
2. **bcrypt:**
   - Een hash-algoritme dat speciaal voor wachtwoorden is ontworpen. Het voegt automatisch een *salt* (willekeurige extra tekens) toe en is bewust traag gemaakt.
   - **Toepassing:** Wachtwoordopslag in webapplicaties en databases, zodat aanvallers niet miljoenen wachtwoorden per seconde kunnen raden (*brute-force*).
3. **Argon2:**
   - De moderne winnaar van de Password Hashing Competition. Gebruikt naast CPU-tijd ook een instelbare hoeveelheid RAM-geheugen om aanvallen met snelle videokaarten (GPUs) tegen te gaan.
   - **Toepassing:** Moderne authenticatiesystemen en wachtwoordmanagers.

### Vraag: Voldoen we met `TOEGANGSCODE_HASH` in `.env` nu wel aan C2, C3 en C4?

- **Ja, nu voldoen we aan alle drie de User Concerns:**
  - **C2:** De gebruiker moet bij het opstarten een geldige toegangscode invoeren voordat het menu verschijnt.
  - **C3:** De toegangscode staat niet in de broncode en `.env` staat in `.gitignore`, waardoor er niets in GitLab komt.
  - **C4:** De toegangscode wordt niet als platte tekst opgeslagen, maar als SHA-256 hash in `.env` bewaard en tijdens het inloggen via hashing gecontroleerd.


---

# Niveau 3, les 8 - Encryptie vs. Hashing, .env beveiligen, Integratiecheck en Sprint Review

## 1. Oefenen met hashing en encryptie

### Klassieke en moderne encryptie

- **Originele zin:** `De snelle bruine vos springt over de luie hond`
- **Versleuteld met Caesar cipher (verschuiving van +3):**
  `Gh vqhooh euxlqh yrv vsulqjw ryhu gh oxlh krqg`
  - *Hoe te achterhalen:* Door elke letter 3 posities terug te schuiven in het alfabet (`G -> D`, `h -> e`).
- **Versleuteld met Atbash cipher (alfabet gespiegeld: A <-> Z, B <-> Y):**
  `Wv hmvoor yifrmv elh hkirmtg levi wv ofrv slmw`
- **Moderne encryptie (AES - Advanced Encryption Standard):**
  - Bij AES wordt de tekst met een geheime sleutel (bijv. 128 of 256 bits) wiskundig versleuteld tot onleesbare data. Zonder de juiste sleutel is de tekst niet te ontsleutelen, maar **met** de sleutel kun je altijd weer exact de originele zin terugkrijgen (tweerichtingsverkeer).

### Hashing van een Nederlands woord (`koe`)

- **Woord:** `koe`
- **MD5-hash (via echte hash-tool / Python `hashlib`):**
  `1e06ceffa8540915d9d193832870adea`
- **SHA-256-hash:**
  `841bb7721cad851a2085604d0b0e418984764bf6356acdc69d94cc672621f33e`
- **Waarom is het achterhalen van een woord uit een hash anders dan decryptie?**
  - Je kunt een hash niet "ontsleutelen" (decrypteren), omdat informatie tijdens het hashen onomkeerbaar verloren gaat. De enige manier om te ontdekken welk woord bij een hash hoort, is door woorden te **raden**, er opnieuw de hash van te berekenen en te kijken of die overeenkomt (bijvoorbeeld met een woordenboeklijst of een *rainbow table* met vooraf berekende hashes van bekende woorden).
- **Waarom geeft een taalmodel (zoals ChatGPT zonder code-tool) vaak een foute MD5-hash?**
  - Een Large Language Model (LLM) is geen rekenmachine die bit-operaties van het MD5-algoritme stap voor stap uitvoert, maar voorspelt op basis van kansberekening een reeks van 32 hexadecimale tekens die *lijkt* op een MD5-hash (of plakt een hash die het ooit op internet bij een ander woord heeft gezien). Alleen door een echt hash-programma (zoals Python `hashlib` of `md5sum` in Linux) uit te voeren krijg je gegarandeerd de juiste hash.

---

## 2. Het `.env`-bestand beveiligen in Linux met `chmod`

Naast het opnemen van `.env` in `.gitignore` kun je in Linux voorkomen dat andere gebruikers op dezelfde computer het `.env`-bestand kunnen lezen:

```bash
chmod 600 .env
ls -la .env
```


---

# Niveau 3, les 8 - Samen & Zelf (Voorbereiding Niveau 4)

## 1. Exception-handling (try/except)

### Waarom crasht leeftijd = int(input("Wat is je leeftijd? ")) bij "achttien"?
- Het commando `int(...)` zorgt voor de crash. `input()` geeft de tekst `"achttien"` terug en `int()` kan letters niet omzetten naar een geheel getal, waardoor Python crasht met een `ValueError`.

### Met if en isdigit()
```python
leeftijd = input("Wat is je leeftijd? ")
if leeftijd.isdigit():
    print(f"Je leeftijd is {int(leeftijd)} jaar.")
else:
    print("Fout: voer een geldig getal in.")
```
- `"20"` wordt geaccepteerd, omdat het alleen uit cijfers bestaat.
- `"achttien"` en `"15.5"` worden geweigerd (letters en de punt zijn geen cijfers).
- `"-18"` wordt ook geweigerd, omdat `isdigit()` het minteken `-` niet als cijfer ziet.

### Met try/except
- We vangen specifiek de fout `ValueError` af:
```python
try:
    leeftijd = int(input("Wat is je leeftijd? "))
    print(f"Je leeftijd is {leeftijd} jaar.")
except ValueError:
    print("Fout: voer een geldig getal in.")
```

---

## 2. Interviews en User Stories van Klaskompas en Oosteling

De user stories die ik met de kennis tot nu toe nog niet kan programmeren gaan over het maken van grafieken en diagrammen (met `matplotlib`):
- **Klaskompas:** US5 / UC8 (staafdiagram van hoe ver studenten van school wonen) en US12 / UC9 (taartdiagram van populaire hobby's).
- **Oosteling:** US8 (staafdiagram met het aantal onderhoudsbeurten per attractie) en US9 (taartdiagram met het aantal onderhoudsbeurten per onderhoudstype). 