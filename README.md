# Algoritmen-en-Heuristieken
project - Case: RailNL



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
Er zijn dele van de code gecomment, zoals het runnen van de HillClimber. Dit is gedaan omdat het runnen van de uitgecommente code lang duurt. De data die uit de gecommente code gegeneert wordt is opgeslagen in csv files. 

### Alle mogelijke trajecten
Er is voor gekozen om de functie nx.all_simple_paths (uit de networkx library) te gebruiken om alle mogelijke trajecten te generen. Dit zijn NIET daadwerkelijk alle mogelijk trajecten. Aan de functie zit het constraint dat een station niet meer dan 1 keer in een traject kan voorkomen. Hierdoor zijn er 207 mogelijke trajecten in Holland en 2633 mogelijke trajecten in Nederland. 

####
Tot runtime 30k iteraties SA: 6621.65 (110+ minuten)
Tot runtime 20k iteraties SA: 892.22 (15- minuten)

#### Milestone: Representatie
Toegevoegd: Classes en Visualisatie

##### Classes
De Classes die we hebben toegevoegd zijn Graph en Station. 
- De class Graph wordt gebruikt voor het creëren en opslaan van een directed graaf van de stations en connecties. Er is gebruik gemaakt van een directed graph zodat er met de Networkx library later gewerkt kan worden als de algoritmes worden geimplementeerd. 
- De class Station wordt gebruikt voor het creëren en opslaan van de stations. Er zijn verschillende attriburen, zoals connection_graph, begin_station en end_station, die later gebruikt zouden kunnen worden bij het implementeren van de algoritmes.

De class Traject wordt in principe niet gebruikt. De code hebben we laten staan voor het geval we deze later toch nodig hebben.

##### Visualisatie van de kaarten
In de map Visualisatie/kaarten staan de kaarten van de beste oplossing opgeslagen in html links. Deze links kunnen naar een wbebrowser gesleept worden om de te bekijken. In de kaarten is echter niet te zien wanneer trajecten voor een deel overlappen. 




