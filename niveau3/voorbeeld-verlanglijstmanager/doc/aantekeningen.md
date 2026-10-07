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