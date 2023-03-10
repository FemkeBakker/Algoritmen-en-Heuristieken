# import functions
from Score import *
from algorithms.random_solution import *
from connections_paths import *
import time

# libraries
import pandas as pd
import networkx as nx


""" PSEUDO-CODE VOOR CONSTRUCTIVE 'GREEDY' ALGORITME """
# neem lijst met alle mogelijke trajecten, plaats in een queue.
# pak het langste traject.
# check of er meerdere trajecten zijn met de langst voorkomende lengte.
# als dit zo is; reken Min uit voor deze trajecten en neem het langste traject met de kleinste Min waarde.
# als dit niet zo is; neem het langste traject.
# voeg het langste traject toe aan lijst van gekozen trajecten.
# ontleed dit gekozen traject in verbindingen, sla deze op in een lijst van alle verbindingen uit de gekozen trajecten.
# verwijder het gekozen traject uit de queue met trajecten die nog bekeken moeten worden.
# kijk naar de queue en pak weer het (nu) langste traject (met kleinst Min, waar nodig)
# check of er overlap is in de verbindingen tussen dit gekozen traject en de lijst met bestaande verbindingen uit de gekozen trajecten.
# als er overlap is, verwijder je het traject uit de queue en ga verder.
# als er geen overlap is, voeg je het traject aan de lijst met gekozen trajecten.
# herhaal dit proces tot het maximale aantal trajecten is bereikt of tot de queue leeg is.
# bereken score voor de gekozen set aan trajecten.

""" Versie waarbij meerdere langste lijsten worden gefilterd op laagste Min """
class Greedy_Constructive:
    def __init__(self, alle_trajecten, G, max_trajecten):
        self.trajecten = alle_trajecten
        self.G = G
        self.max_trajecten = max_trajecten

    # functie voor het berekenen van het aantal minuten van 1 traject.
    def calculate_Min(self, path):
        Min = nx.path_weight(self.G.graaf, path, weight = "weight")
        return Min

    # main functie voor greedy
    def kies_trajecten(self):
        start = time.perf_counter()
        queue = self.trajecten
        gekozen_trajecten = []
        verbindingen_totaal = []
        trajecten_en_Min = dict()

        # loop tot het max trajecten is bereikt.
        while len(gekozen_trajecten) < self.max_trajecten:

            # selecteer langste trajecten uit queu.
            langste_trajecten = list(filter(lambda x: len(x) == max(map(len,queue)), queue))

            # bereken minuten voor elk van de langste trajecten, selecteer dan het langste traject met het laagste aantal minuten.
            for traject in langste_trajecten:
                Min = self.calculate_Min(traject)
                trajecten_en_Min[tuple(traject)] = Min
            langste_traject = list(min(trajecten_en_Min, key=trajecten_en_Min.get))

            # neem alle connection uit geselecteerde traject, check of connection al bestaat in gekozen trajecten.
            verbindingen = from_paths_to_connections(langste_traject)
            overlap = False
            for verbinding in verbindingen:
                if verbinding in verbindingen_totaal or (verbinding[1], verbinding[0]) in verbindingen_totaal:
                    overlap = True
                    break

            # als connections al bestaan, verwijder traject uit quee
            if overlap:
                queue.remove(langste_traject)

                # maak dict leeg voor volgende loop
                trajecten_en_Min.clear()

            # als connecties nog niet bestaan, sla het geselecteerde tractect en de connetie op en verwijder het uit de queu. 
            else:
                gekozen_trajecten.append(langste_traject)
                verbindingen_totaal.extend(verbindingen)
                queue.remove(langste_traject)

                # maak dict leeg voor volgende loop
                trajecten_en_Min.clear()

        # bereken de totaal score van de geselecteerde trajecten
        score = calculate_score(self.G, gekozen_trajecten)
        end = time.perf_counter()
        runtime = end - start
        return gekozen_trajecten, score, runtime

# Functie slaat de scores van Greedy op in csv
def greedy_to_csv(score, solution, deel, runtime):
    greedy = pd.DataFrame(columns=['runtime','eind_score', 'solution'])
    greedy['runtime'] = [runtime]
    greedy['eind_score'] = [score]
    greedy['solution'] = [solution]

    # maak greedy map in experiment aan als deze nog niet bestaat
    path = "experiment/greedy"
    if not os.path.exists(path):
        os.makedirs(path)

    greedy.to_csv("{}/{}.csv".format(path, deel), index = False)
