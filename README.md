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

#### Runnen van de code
De code kan gerund worden door de command: py main.py te runnen. Alles wat gegenereerd wordt is al opgeslagen in de mappen. 
Er zijn delen van de code gecomment, zoals het runnen van de HillClimber. Dit is gedaan omdat het runnen van de uitgecommente code lang duurt en/of het belangrijk is dat er constant met dezelfde waardes gewerkt wordt (zoals bij de random baseline). De data die uit de gecommente code gegeneert wordt is opgeslagen in csv files. 
Er zijn delen van de code gecomment, zoals het runnen van de HillClimber. Dit is gedaan omdat het runnen van de uitgecommente code lang duurt en/of het belangrijk is dat er constant met dezelfde waardes gewerkt wordt (zoals bij de random baseline). De data die uit de gecommente code gegeneert wordt is opgeslagen in csv files. 

#### Alle mogelijke trajecten
Er is voor gekozen om de functie nx.all_simple_paths (uit de networkx library) te gebruiken om alle mogelijke trajecten te generen. Dit zijn NIET daadwerkelijk alle mogelijk trajecten. Aan de functie zit het constraint dat een station niet meer dan 1 keer in een traject kan voorkomen. Hierdoor zijn er 207 mogelijke trajecten in Holland en 2633 mogelijke trajecten in Nederland.

#### Baseline
Er worden random trajecten geselecteerd uit alle mogelijke trajecten. Dubbele trajecten worden niet toegestaan.

#### Greedy
Greedy (constructief): In dit algoritme wordt eerst naar alle mogelijke trajecten gekeken en hieruit de langste gekozen, omdat deze zo veel mogelijk verbindingen meeneemt en zo wordt p (en daarmee de score) verhoogd. In het geval dat er meerdere trajecten voorkomen met de maximale lengte, wordt er vervolgens gekeken naar de Min van de trajecten en wordt het langste traject met de kleinste waarde voor Min gekozen. Vervolgens word dit proces herhaald, maar worden trajecten die verbindingen bevatten die al in de gekozen traject(en) voorkomt niét meer meegenomen, om zo zoveel mogelijk verbindingen mee te nemen en p te maximaliseren, terwijl Min als tweede factor wordt geminimaliseerd. Dit proces wordt herhaald tot het maximum van T (max aantal trajecten) wordt bereikt of tot er geen trajecten meer zijn om uit te kiezen. Ten slotte wordt de score van de gekozen trajecten berekend. 

#### Hill Climber
De manier waarop de Hill Climber kleine aanpassingen doet is door een random traject te selecteren uit de huidige state en deze te vervangen met een random traject uit alle mogelijke trajecten. Er worden dus geen aanpassingen gedaan binnen de trajecten. 

Er worden drie verschillende beginstates van de Hill Climber getest. (1) random beginstate, deze wordt gegenereerd door het gebruik van de random baseline. (2) 7 langste trajecten, de 7 langste trajecten uit alle mogelijke trajecten worden geselecteerd. (3) Greedy constructive, de oplossing die uit het Greedy constructive algoritme komt (deze is altijd het zelfde). 

#### Generate Experiment
Generate experiment zorgt er voor dat alle data voor het experimenteren voor het Hill Climber algoritme en het Simulated Annealing algoritme gegeneert worden. Alle berekende eindscores per iteratie worden opgeslagen. Er wordt ook een info_data.csv aangemaakt. Daarin staat een samenvatting van de iteraties van het algoritme, zoals het gemiddelde de runtime en de best gevonden oplossing.

#### Experiment Hill Climber
Voor de Hill Climber wordt er geëxperimenteert met verschillende iteraties. De iteraties die getest zijn: 200, 500, 1000, 5000, 8000, 10000, 12000, 14000, 15000. Deze iteraties worden 150 keer getest. Bij alle verschillende beginstate wordt er gekeken naar het optimale altijd iteraties. Er wordt hierbij een afweging gemaakt tussen score en tijd. 

#### Vergelijking algoritmes
Er is voor gekozen om per algoritme de meest optimale parameters (bv. iteraties, temperatuur) te kiezen en deze te vergelijken met de andere algoritmes. Dit betekent voor Holland het volgende:
- Hill-Climber met beginstate random: 8000 iteraties.
- Hill-Climber met beginstate 7 langste: 10000 iteraties.
- Hill-Climber met beginstate Greedy constructive: 200 iteraties. Er is gekozen voor 200 iteraties omdat de HillClimber hier in een lokaal optimum vast zit. Door de afweging te maken tussen tijd en score is 200 iteraties optimaal. 
- Simulated Annealing: 20000 iteraties en tempratuur=30

Voor Nederland geldt:
- Hill-Climber met beginstate random: 15000 iteraties.
- Hill-Climber met beginstate 7 langste: 15000 iteraties.
- Hill-Climber met beginstate Greedy constructive: 200 iteraties. Er is gekozen voor 200 iteraties omdat de HillClimber hier in een lokaal optimum vast zit. Door de afweging te maken tussen tijd en score is 200 iteraties optimaal. 
- Simulated Annealing:
                - Temperatuur parameter: 30
                - 20.000 iteraties
- Simulated Annealing: 20000 iteraties en tempratuur=30

Alle algoritmes worden geplot in een boxplot: Greedy constructive, 3 verschillende Hill Climbers, random baseline & Simulated Annealing.
In het boxplot van Nederland is er gekozen om de random baseline weg te laten. Doordat de random baseline ver onder de andere scores ligt, verstoort dit de duidelijkheid van de visualisatie. 

#### Visualisatie van de kaarten
In de map Visualisatie/kaarten staan de kaarten van de beste oplossing opgeslagen in html links. Deze links kunnen naar een webbrowser gesleept worden om de te bekijken. In de kaarten is echter niet te zien wanneer trajecten voor een deel overlappen. 

#### Conclusie
Uit de boxplots waarin alle algoritmes met elkaar vergeleken worden blijkt dat voor beide Nederland en Holland het Simulated Annealing algoritme het beste werkt. 


####
Tot runtime 30k iteraties SA: 6621.65 (110+ minuten)
Tot runtime 20k iteraties SA: 892.22 (15- minuten)

#### Milestone: Representatie
Toegevoegd: Classes en Visualisatie





####
Tot runtime 30k iteraties SA: 6621.65 (110+ minuten)
Tot runtime 20k iteraties SA: 892.22 (15- minuten)


