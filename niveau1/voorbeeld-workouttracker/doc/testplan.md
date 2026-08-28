# Testen workouttracker

### Voorbereiding

Voor alle testscases wordt de volgende voorbereiding verwacht:

* Zorg dat de juiste tabellen zijn aangemaakt in de database.
* Verwijder eventueel alle data in de database.
* Zorg dat `inserts.sql` is ingeladen.



## Testen "Toon alle workouts"

### Testscenario

1. Start de applicatie.
2. Kies in het menu voor optie 1.

### Verwacht resultaat

Er verschijnt een lijst met alle workouts. Deze ziet er als volgt uit:

Eerste regels

```
2026-03-02 07:15:00  -  hardlopen  -  45 minuten
2026-03-04 18:30:00  -  krachttraining  -  60 minuten
2026-03-06 08:05:00  -  hardlopen  -  30 minuten
```

[...]

Laatste regels

```
2026-05-14 08:55:00  -  hardlopen  -  50 minuten
2026-05-18 19:20:00  -  krachttraining  -  75 minuten
2026-05-22 07:35:00  -  hardlopen  -  40 minuten
```

## Testen "Toon alle hardloop-workouts"

### Testscenario

1. Start de applicatie.
2. Kies in het menu voor optie 2.

### Verwacht resultaat

Er verschijnt een lijst met alle hardloop-workouts. Deze ziet er als volgt uit:

Eerste regels

```
2026-03-02 07:15:00  -  hardlopen  -  45 minuten
2026-03-06 08:05:00  -  hardlopen  -  30 minuten
2026-03-12 06:50:00  -  hardlopen  -  50 minuten
```

Laatste regels

```
2026-05-06 07:25:00  -  hardlopen  -  30 minuten
2026-05-14 08:55:00  -  hardlopen  -  50 minuten
2026-05-22 07:35:00  -  hardlopen  -  40 minuten
```

## Testen "Toon alle krachttraining-workouts"

### Testscenario

1. Start de applicatie.
2. Kies in het menu voor optie 3.

### Verwacht resultaat

Er verschijnt een lijst met alle krachttraining-workouts. Deze ziet er als volgt uit:

Eerste regels

```
2026-03-04 18:30:00  -  krachttraining  -  60 minuten
2026-03-09 19:10:00  -  krachttraining  -  55 minuten
2026-03-18 17:45:00  -  krachttraining  -  65 minuten
```

Laatste regels

```
2026-05-02 18:15:00  -  krachttraining  -  55 minuten
2026-05-10 17:50:00  -  krachttraining  -  60 minuten
2026-05-18 19:20:00  -  krachttraining  -  75 minuten
```


## Testen "Toon alle andere workouts"

### Testscenario

1. Start de applicatie.
2. Kies in het menu voor optie 4.

### Verwacht resultaat

Er verschijnt een lijst met alle andere workouts. Deze ziet er als volgt uit:

```
2026-03-15 20:00:00  -  yoga  -  40 minuten
2026-04-14 16:40:00  -  zwemmen  -  45 minuten
```

## Testen "Totale duur van workouts tonen"

### Testscenario

1. Start de applicatie
2. Kies in het menu voor optie 6.

### Verwacht resultaat

Het stysteem meldt: "Totale duur van workouts: 21 uren en 25 minuten".

## Testen "Toon alle gebruikte workouttypes"

### Testscenario

1. Start de applicatie.
2. Kies in het menu voor optie 7.

### Verwacht resultaat

Er verschijnt een lijst met elk gebruikt workouttype precies een keer. Deze ziet er als volgt uit:

```text
hardlopen
krachttraining
yoga
zwemmen
```

## Testen "Nieuwe workout toevoegen"

Let op: uitvoeren van deze test beinvloedt mogelijk het resultaat van het testscenario "Totale duur van workouts tonen"!

### Testscenario

1. Start de applicatie
2. Kies in het menu voor optie 5.
3. Kies als datum van de workout: 2026-09-13
4. Kies als tijd van de workout: 15:45:55
5. Kies als type: padel
6. Kies als duur: 100

### Verwacht resultaat

* Systeem meldt "Workout toegevoegd!"
* In de database is de ingevoerde workout met correcte gegevens terug te vinden