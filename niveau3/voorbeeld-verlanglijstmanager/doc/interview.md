# Interviewverslag: Ontwikkeling Verlanglijstmanager

**Datum:** 17 augustus 2026  
**Interviewers:** Zayn Haddad en Linde Nolet (Ontwikkelaars, Studenten ICT)  
**Geïnterviewde:** Skyler Hoekstra (Opdrachtgever, Budgetcoach bij Stichting Florijn)

<img src="img/florijn-interview.png" width="400">

---

### Het Interview

**Vraag:** Kun je wat vertellen over Stichting Florijn en jouw rol als budgetcoach?

**Antwoord:** Stichting Florijn is een organisatie die zich inzet voor mensen met financiële problemen. Als budgetcoach help ik mensen om hun financiën op orde te krijgen en te houden. We bieden ondersteuning bij het maken van budgetplannen, het beheren van uitgaven en het stellen van financiële doelen. Daarvoor organiseren we workshops waarbij deelnemers een overzicht maken van de spullen die ze nog willen kopen en waarbij ze inschatten welke budgetten ze daarvoor nodig hebben. De laatste tijd focussen we steeds meer op het helpen van studenten, omdat zij vaak te maken hebben met beperkte budgetten en veel verleidingen om geld uit te geven. Vanuit de gemeentes is de vraag bij ons neergelegd om studenten met een tool te ondersteunen, en het leek ons een goed idee om die tool te laten ontwikkelen door studenten ICT, zodat we iets krijgen dat echt aansluit bij de behoeften van studenten. Het is dus een tool die gebruikt moet kunnen worden door mensen die aan onze workshop hebben deelgenomen, maar ook door andere studenten die hun financiën beter willen beheren.

**Vraag:** Betekent dat dat wij helemaal zelf mogen bedenken wat de tool kan en hoe die eruit moet zien?

**Antwoord:** Nee, we willen graag jullie input en creativiteit gebruiken, maar we hebben ook wel wat eisen en functies in gedachten die er in elk geval in moeten zitten.

**Vraag:** Wat is voor jou de kern van dit systeem? Hoe gaan de studenten het gebruiken?

**Antwoord:** **Het draait om overzicht.** Nu hebben studenten vaak overal lijstjes van dingen die ze nog willen kopen: op hun telefoon, in een schriftje dat op hun kamer rondslingert, of gewoon in hun hoofd. **Ik wil dat ze al die wensen op één plek verzamelen. Gewoon een programma waarin ze een nieuw ding kunnen toevoegen, maar ook weer weg kunnen strepen als ze het toch niet meer willen of natuurlijk als ze het gekocht hebben. En heel belangrijk: prijzen veranderen continu. Ze moeten dus ook de prijs van iets op hun lijstje kunnen bijwerken als er een aanbieding is.** Ook willen we graag dat de items in verschillende lijstjes gezet kunnen worden, bijvoorbeeld een lijstje met spullen voor hun sport, een lijstje met studiebenodigdheden, of een lijstje met hobbyspullen, enzovoort. **Dat maakt het overzichtelijker en helpt ze om hun budgetten beter te beheren. Want we willen graag met budgetten per lijstje werken.** Zo kunnen ze bijvoorbeeld een budget van 100 euro instellen voor hun studiebenodigdheden, en dan zien ze meteen of ze nog binnen dat budget zitten als ze iets toevoegen of aanpassen.Er kan bij een item worden aangegeven bij welke winkel het gaat worden gekocht, als daat bekend is.

**Vraag:** Je noemde dat je nu vaak met Excel-lijstjes werkt. Hoe sluit dat hierop aan?

**Antwoord:** Klopt, ik heb voor samen met mijn team al wat lijstjes met voorbeelden klaarstaan met veelgekochte spullen door ICT-studenten. Dit soort Excel-lijstjes maken we nu al met studenten tijdens onze workshops. Gewoon simpele Excel-bestandjes met wat simpele gegevens per item. Het zou handig zijn als een student zo'n bestand in één keer in de app kan laden nadat ze bij ons die workshop hebben gevolgd. Dat scheelt saai overtypwerk en dan kunnen ze meteen echt aan de slag met wat ze in de workshop gedaan hebben. Zet de budgetten per lijstje standaard maar op iets van 100 euro, dat is een mooi uitgangspunt. **Ze moeten dat budget per lijstje natuurlijk wel kunnen aanpassen in de app.** Ik zal je straks zo'n voorbeeldbestand sturen, dan kun je zien hoe het eruit ziet. 

**Vraag:** Moet de app alleen de productprijs laten zien, of komt er meer bij kijken?

**Antwoord:** Daar noem je wat. Veel studenten maken de fout alleen naar het prijskaartje te kijken. Ze zien een laptop voor 600 euro, maar vergeten de verzendkosten. Ik wil dat de app altijd de totale kosten laat zien. Dus de prijs plus wat de winkel rekent voor het opsturen. Zo kom je nooit voor verrassingen te staan bij het afrekenen. In het prototype mag je er van uitgaan dat de verzendkosten per winkel altijd hetzelfde zijn, dus dat kunnen we gewoon als een vast bedrag instellen per winkel.  Dat maakt het ook makkelijker om te implementeren. En zet dat standaard maar op 0 euro, want dat is vaak toch wel de praktijk. Het zou mooi zijn als die verzendkosten per winkel nog kunnen worden aangepast, maar op dit moment is dat niet het allerbelangrijkst.

**Vraag:** Hoe zit het nou precies met die lijstjes en budgetten waar je het eerder over had, kun je dat nog een keer uitleggen?

**Antwoord:** Ik leer studenten om hun geld in potjes te verdelen, in lijstjes dus, zeg maar. Bijvoorbeeld 'Studie', 'Hobby' of 'Huisvesting'. **Voor elk lijstje spreken we een maximumbedrag af.** De tool moet per potje kunnen laten zien wat erin zit, wat het goedkoopste en duurste item is en wat de gemiddelde prijs per item is. En ook of ze nog binnen dat budget blijven. **Soms veranderen die afspraken, dus ze moeten dat maximumbedrag van een lijstje ook zelf kunnen aanpassen.**

**Vraag:** Hoe zie je de techniek voor je? Moet het een website worden?

**Antwoord:** Privacy is voor ons echt een dingetje. We willen niet dat die gevoelige financiële data op een server op internet zweeft. Het moet gewoon veilig op de eigen computer van de student draaien. En eerlijk gezegd: het hoeft geen flitsende grafische interface te zijn. **Gewoon een overzichtelijk menu waar je met letters of cijfers doorheen wandelt is voor ons prima, zolang het maar doet wat het moet doen.** Het gaat er ook om dat we nu een eerste versie hebben die we kunnen testen en feedback op kunnen krijgen. We willen vooral dat het functioneel is, niet dat het er supermooi uitziet, **maar de data moet er wel netjes in worden opgeslagen natuurlijk.** Als het blijkt te werken, kunnen we subsidies aanvragen om het later nog beter uit te laten werken, maar dat zal dan wel gebaseerd zijn op jullie versie, dus jullie hebben echt wel invloed op het eindproduct.

**Vraag:** Betekent privacy voor jullie ook dat niet iedereen meteen in de applicatie moet kunnen?

**Antwoord:** Ja, dat zou ik wel prettig vinden. Zeker als studenten hun laptop ergens open laten staan of in een gedeelde ruimte werken. Voor deze eerste versie hoeft dat geen uitgebreid accountsysteem te zijn, maar een eenvoudige toegangscode bij het opstarten zou heel passend zijn. Dat moet natuurlijk wel op een veilig manier gebeuren.

**Vraag:** Zijn er nog specifieke manieren waarop studenten hun lijstje moeten kunnen filteren?

**Antwoord:** Ja, twee dingen. Ten eerste: zoeken op prijs. Soms heeft een student aan het eind van de maand nog een bepaald bedrag over. Dan is het handig als ze kunnen vragen: "Wat staat er op mijn lijstje tussen de 10 en 50 euro?" zodat ze gericht iets nuttigs kunnen kopen. Natuurlijk vinden we het belangrijk dat studenten hun budgetten in de gaten houden, maar het moet ook leuk blijven, dus af en toe iets aanschaffen als het budget dat toestaat, hoort er ook gewoon bij natuurlijk.

Ten tweede: het sparen zelf. Sommige dingen zijn te duur om in één keer te kopen. Ik wil dat ze kunnen uitrekenen hoeveel ze elke maand opzij moeten leggen om iets over bijvoorbeeld een half jaar te kunnen kopen. Een soort spaarplan per item. Stel bijvoorbeeld dat ze weten dat over een half jaar een nieuwe iPhone uitkomt, en ze weten al ongeveer hoeveel die gaat kosten, dan is het handig als ze een soort spaarplan kunnen maken. De app rekent dan voor ze uit hoeveel ze per maand moeten sparen om dat ding te kunenn kopen als-ie eenmaal uitgekomen is. Dat helpt ze om een realistisch beeld te krijgen van hun financiële situatie en om beter te plannen. En het is ook gewoon motiverend om te zien dat ze elke maand een stapje dichter bij hun doel komen. Het maakt het sparen tastbaarder en leuker. We hopen dat studenten hiermee ook beter een soort gevoel ontwikkelen van hoe ze kunnen omgaan met hun geld, zodat ze daar later in hun leven ook profijt van hebben.

**Vraag:** Je gaf aan dat de data "netjes" moet blijven. Wat bedoel je daar precies mee?

**Antwoord:** **Ik wil voorkomen dat het een rommeltje wordt. Als de student de ene keer 'Studie' invult en de andere 'studeren' of 'school' of zoiets,, dan kloppen de overzichten niet meer. De app moet ervoor zorgen dat winkels en lijstjes herkenbaar blijven.** **Ook moeten we kunnen werken met belangrijkheid; sommige dingen heb je volgende week nodig voor je tentamen of zo, andere zijn voor 'ooit'. Die prioriteit moet je kunnen aangeven. Iets met "laag", "midden" en "hoog" of zoiets.** Het zou leuk zijn als jullie ook nog een functie kunnen maken om die prioriteiten zinnig te gebruiken in het budget, bijvoorbeeld door te laten zien hoeveel geld er nog over is binnen het budget van een lijstje als je alleen de "hoge" prioriteit items zou kopen, maar dat is niet per se echt nodig voor deze versie, dus kijk maar of dat lukt. En als jullie nog andere dingen kunnen bedenken, voeg die dan zeker toe. Ik zei al: we hebben er bewust voor gekozen om studenten deze eerste versie te laten maken, dus het zou jammer zijn als we jullie creativiteit niet zouden benutten. Jullie weten zelf ook wel wat handig zou zijn, dus voel je vrij om dat toe te voegen als je denkt dat het een goede toevoeging is.

**Vraag:** Zijn er nog andere dingen die er in moeten zitten die we nog niet besproken hebben?

**Antwoord:** Het zou leuk zijn als ze bij het afsluiten nog even een kort overzichtje krijgen van wat ze die sessie hebben gedaan, bijvoorbeeld hoeveel items ze hebben toegevoegd of verwijderd. Een soort motivatie dat ze goed bezig zijn met hun geldzaken!

---

## Nagestuurd door Skyler per e-mail:

To: Zayn Haddad <z.haddad@student.han.nl>; Linde Nolet <l.nolet2@student.han.nl>
From: Skyler Hoekstra <skyler@budgetcoach.florijn.nl>
Subject: Voorbeeldbestand voor Verlanglijstmanager

Beste Zayn en Linde,

Ik had jullie beloofd om nog een voorbeeldbestand te sturen met wat voorbeeldgegevens. Ik heb het Excelbestand zoals jullie na het interview vroegen omgezet naar een CSV-bestand (dat kostte me nog best wel wat moeite, haha, maar ik ben dan ook geen ICT-student). Hopelijk is dit wat jullie bedoelen en kunnen jullie hier iets mee. Zo niet: laat maar weten!

Trouwens, die bestanden staan vaak op een usb-stick of zo, dus het zou fijn zijn als jullie ervoor kunnen zorgen dat de app ook gewoon vanaf een externe schijf kan werken. Dat is voor ons wel een belangrijk punt, want we werken vaak met gedeelde computers en dan is het handig als we die bestanden gewoon kunnen meenemen.

Groet,
Skyler Hoekstra
Budgetcoach bij Stichting Florijn -€f-

```text
naam,prijs,winkel,lijst,prioriteit
Toetsenbord,129.99,Azerty,Hardware,1
Draadloze muis,45.50,Azerty,Hardware,2
USB-C Hub,29.95,Bol.com,Hardware,2
Monitor 27 inch,249.00,Coolblue,Hardware,1
HDMI-kabel,9.99,Bol.com,Hardware,3
Office 365,69.00,Microsoft,Software,3
Gamenstoel,199.50,IKEA,Gaming,3
Bureaumat,25.00,IKEA,Gaming,3
LED-bureaulamp,35.00,Coolblue,Gaming,2
Geheugenstick 64GB,15.99,Bol.com,Hardware,3
Koptelefoon,179.00,Coolblue,Hardware,1
Webcam 1080p,59.95,Azerty,Hardware,2
Python Cursusboek,39.99,Bol.com,Boeken,2