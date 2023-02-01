# Algoritmen-en-Heuristieken
Case: RailNL

## Wat we nog moeten doen:
- overal comments toegevoegd + in het nederlands
- main opschonen. Alle uitgecommende code er uithalen
- read.me. 
- requirements.text -> Tijn
- git.ignore file. Femke
- tijd tabellen. Soufiane
- vergelijken algoritmes -> twee boxplot van Holland en Nederland met daarin de optimale versies van 3x HillClimber, 2x Greedy, 1x Random, 1 Simulated Annealing. Femke
- visualizaties van de beste oplossingen van elk algoritme. Femke
- berekenen maximum score. Tijn 

Main opbouw:
- laden data
- aanmaken graven
- genereer alle mogelijke paden
- Random baseline -> moet opgeslagen worden in csv
- Runnen van Greedy
- Experiment Hill Climber -> opslaan van de data + TIJD TABELLEN
- Experiment Hill Climber -> maken van de boxplots van de iteraties
- Experiment Sim Annealing -> opslaan van de data + TIJD TABELLEN
- Experiment Sim Annealing -> maken van de boxplots van de iteraties en tempratuur
- Experiment vergelijking van de algoritmes
- Visualizatie van de kaart van de beste oplossingen.

### Runnen van de code
De code kan gerund worden door de command: py main.py te runnen. Alles wat gegenereerd wordt is al opgeslagen in de mappen. 
Er zijn delen van de code gecomment, zoals het runnen van de HillClimber. Dit is gedaan omdat het runnen van de uitgecommente code lang duurt en/of het belangrijk is dat er constant met dezelfde waardes gewerkt wordt (zoals bij de random baseline). De data die uit de gecommente code gegeneert wordt is opgeslagen in csv files. 

### Alle mogelijke trajecten
Er is voor gekozen om de functie nx.all_simple_paths (uit de networkx library) te gebruiken om alle mogelijke trajecten te generen. Dit zijn NIET daadwerkelijk alle mogelijk trajecten. Aan de functie zit het constraint dat een station niet meer dan 1 keer in een traject kan voorkomen. Hierdoor zijn er 207 mogelijke trajecten in Holland en 2633 mogelijke trajecten in Nederland. 

### Hill Climber
De manier waarop de Hill Climber kleine aanpassingen doet is door een random traject te selecteren uit de huidige state en deze te vervangen met een random traject uit alle mogelijke trajecten. Er worden dus geen aanpassingen gedaan binnen de trajecten. 

Er worden drie verschillende beginstates van de Hill Climber getest. (1) random beginstate, deze wordt gegenereerd door het gebruik van de random baseline. (2) 7 langste trajecten, de 7 langste trajecten uit alle mogelijke trajecten worden geselecteerd. (3) Greedy constructive, de oplossing die uit het Greedy constructive algoritme komt (deze is altijd het zelfde). 

#### Generate Experiment
Generate experiment zorgt er voor dat alle data voor het experimenteren voor het Hill Climber algoritme en het Simulated Annealing algoritme gegeneert worden. Alle berekende eindscores per iteratie worden opgeslagen. Er wordt ook een info_data.csv aangemaakt. Daarin staat een samenvatting van de iteraties van het algoritme, zoals het gemiddelde de runtime en de best gevonden oplossing.

#### Vergelijking algoritmes
Er is voor gekozen om per algoritme de meest optimale parameters (bv. iteraties, temperatuur) te kiezen en deze te vergelijken met de andere algoritmes. Dit betekent voor Holland het volgende:
- Hill-Climber met beginstate random: 8000 iteraties.
- Hill-Climber met beginstate 7 langste: 10000 iteraties.
- Hill-Climber met beginstate Greedy constructive: 200 iteraties. Er is gekozen voor 200 iteraties omdat de HillClimber hier in een lokaal optimum vast zit. Door de afweging te maken tussen tijd en score is 200 iteraties optimaal. 
- Simulated Annealing:
                - Temperatuur parameter: 30
                - 20.000 iteraties

Voor Nederland geldt:
- Hill-Climber met beginstate random: 15000 iteraties.
- Hill-Climber met beginstate 7 langste: 15000 iteraties.
- Hill-Climber met beginstate Greedy constructive: 200 iteraties. Er is gekozen voor 200 iteraties omdat de HillClimber hier in een lokaal optimum vast zit. Door de afweging te maken tussen tijd en score is 200 iteraties optimaal. 
- Simulated Annealing:
                - Temperatuur parameter: 30
                - 20.000 iteraties

Alle algoritmes worden geplot in een boxplot: Greedy constructive, 3 verschillende Hill Climber, random baseline & Simulated Annealing.
In het boxplot van Nederland is er gekozen om de random baseline weg te laten. Doordat de random baseline ver onder de andere scores ligt, verstoort dit de duidelijkheid van de visualisatie. 


#### Milestone: Representatie
Toegevoegd: Classes en Visualisatie

##### Classes
De Classes die we hebben toegevoegd zijn Graph en Station. 
- De class Graph wordt gebruikt voor het creëren en opslaan van een directed graaf van de stations en connecties. Er is gebruik gemaakt van een directed graph zodat er met de Networkx library later gewerkt kan worden als de algoritmes worden geimplementeerd. 
- De class Station wordt gebruikt voor het creëren en opslaan van de stations. Er zijn verschillende attriburen, zoals connection_graph, begin_station en end_station, die later gebruikt zouden kunnen worden bij het implementeren van de algoritmes.

De class Traject wordt in principe niet gebruikt. De code hebben we laten staan voor het geval we deze later toch nodig hebben.

##### Visualisatie van de kaarten
In de map Visualisatie/kaarten staan de kaarten van de beste oplossing opgeslagen in html links. Deze links kunnen naar een wbebrowser gesleept worden om de te bekijken. In de kaarten is echter niet te zien wanneer trajecten voor een deel overlappen. 


####
Tot runtime 30k iteraties SA: 6621.65 (110+ minuten)
Tot runtime 20k iteraties SA: 892.22 (15- minuten)


