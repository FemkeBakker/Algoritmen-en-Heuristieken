# import functions
from Score import *
from random_solution import *
from connections_paths import *

# libraries
import pandas as pd
import networkx as nx

# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# load data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# create Graph instances
G_holland = Graph(ConnectiesHolland, StationsHolland)
G_nederland = Graph(ConnectiesNationaal, StationsNationaal)

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

    # function for calculating Min for a single traject
    def calculate_Min(self, path):
        Min = nx.path_weight(self.G.graaf, path, weight = "weight")
        return Min

    # main function for greedy
    def kies_trajecten(self):
        queue = self.trajecten
        gekozen_trajecten = []
        verbindingen_totaal = []
        trajecten_en_Min = dict()

        # loop until max trajectories is reached
        while len(gekozen_trajecten) < self.max_trajecten:
            # select longest trajectories from queue
            langste_trajecten = list(filter(lambda x: len(x) == max(map(len,queue)), queue))

            # calculate Min for each of the longest trajects, then select the longest trajectory with the smallest Min value
            for traject in langste_trajecten:
                Min = self.calculate_Min(traject)
                trajecten_en_Min[tuple(traject)] = Min
            langste_traject = list(min(trajecten_en_Min, key=trajecten_en_Min.get))

            # extract all connections from the selected traject, check if connections already exist within chosen trajectories
            verbindingen = from_paths_to_connections(langste_traject)
            overlap = False
            for verbinding in verbindingen:
                if verbinding in verbindingen_totaal or (verbinding[1], verbinding[0]) in verbindingen_totaal:
                    overlap = True
                    break
            # if connections already exist, remove trajectory from queue and empty dict for next loop
            if overlap:
                queue.remove(langste_traject)
                trajecten_en_Min.clear()
            # if connections do not exist yet, save the selected trajectory and its connections and remove it from the queue. Also empty dict for next loop.
            else:
                gekozen_trajecten.append(langste_traject)
                verbindingen_totaal.extend(verbindingen)
                queue.remove(langste_traject)
                trajecten_en_Min.clear()

        # calculate the score for the combination of selected trajectories
        score = calculate_score(self.G, gekozen_trajecten)
        
        return gekozen_trajecten, score

def greedy_to_csv(score, solution, deel):
    greedy = pd.DataFrame(columns=['eind_score', 'solution'])
    greedy['eind_score'] = [score]
    greedy['solution'] = [solution]

    path = "experiment/greedy"
    if not os.path.exists(path):
        os.makedirs(path)

    greedy.to_csv("{}/{}.csv".format(path, deel), index = False)


""" Versie waarbij meerdere langste lijsten en Min niet worden meegenomen """
# class Greedy:
#     def __init__(self, alle_trajecten, G, max_trajecten):
#         self.trajecten = alle_trajecten
#         self.G = G
#         self.max_trajecten = max_trajecten

    # main function for greedy
#     def kies_trajecten(self):
#         queue = self.trajecten
#         gekozen_trajecten = []
#         verbindingen_totaal = []

        # loop until max trajectories is reached
#         while len(gekozen_trajecten) < self.max_trajecten:
            # select longest trajectory from queue
#             langste_traject = max(queue, key=len)
            # extract all connections from the selected traject, check if connections already exist within chosen trajectories
#             verbindingen = from_paths_to_connections(langste_traject)
#             overlap = False
#             for verbinding in verbindingen:
#                 if verbinding in verbindingen_totaal or (verbinding[1], verbinding[0]) in verbindingen_totaal:
#                     overlap = True
#                     break
            # if connections already exist, remove trajectory from queue
#             if overlap:
#                 queue.remove(langste_traject)
            # if connections do not exist yet, save the selected trajectory and its connections and remove it from the queue.
#             else:
#                 gekozen_trajecten.append(langste_traject)
#                 verbindingen_totaal.extend(verbindingen)
#                 queue.remove(langste_traject)
        # calculate the score for the combination of selected trajectories
#         score = calculate_score(self.G, gekozen_trajecten)
        
#         return gekozen_trajecten, score


