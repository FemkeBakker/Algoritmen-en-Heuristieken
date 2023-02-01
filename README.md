# Algoritmen-en-Heuristieken
project - Case: RailNL



## Wat we nog moeten doen:
- overal comments toegevoegd + in het nederlands
- main opschonen. Alle uitgecommende code er uithalen
- make_instance_station functie in main.py naar andere file. Wordt deze functie gebruikt?
- example trajecten bij create_plot in main weg
- in read.me -> uitleg over wat alle mogelijke traejcten zijn
- random baseline moet nog 150 keer gerund worden. 
- hoe willen we met de random baseline vergelijken? -> algoritmes (beste versie) in box plot?
- het enkele keer runnen van HillClimber en SimAnnealing weghalen.

Main opbouw:
- laden data
- aanmaken graven
- genereer alle mogelijke paden
- Random baseline -> moet opgeslagen worden in csv
- Runnen van Greedy
- Experiment Hill Climber -> opslaan van de data + TIJD TABELLEN
- Experiment Sim Annealing -> opslaan van de data + TIJD TABELLEN
- Experiment HillClimber -> maken van de boxplots van de iteraties
- Experiment Sim Annealing -> maken van de boxplots van de iteraties en tempratuur
- Experiment vergelijking van de algoritmes
- Visualizatie van de kaart van de beste oplossingen.

#### Milestone: Representatie
Toegevoegd: Classes en Visualisatie

##### Classes
De Classes die we hebben toegevoegd zijn Graph en Station. 
- De class Graph wordt gebruikt voor het creëren en opslaan van een directed graaf van de stations en connecties. Er is gebruik gemaakt van een directed graph zodat er met de Networkx library later gewerkt kan worden als de algoritmes worden geimplementeerd. 
- De class Station wordt gebruikt voor het creëren en opslaan van de stations. Er zijn verschillende attriburen, zoals connection_graph, begin_station en end_station, die later gebruikt zouden kunnen worden bij het implementeren van de algoritmes.

De class Traject wordt in principe niet gebruikt. De code hebben we laten staan voor het geval we deze later toch nodig hebben.

##### Visualisatie
In de map Visualisatie staat een html link: map.html. Deze link kan naar de browser gesleept worden zodat de visualisatie zichtbaar wordt.




