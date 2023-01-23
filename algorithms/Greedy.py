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

""" PSEUDO-CODE VOOR 'GREEDY' ALGORITME """
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
class Greedy:
    def __init__(self, alle_trajecten, G, max_trajecten):
        self.trajecten = alle_trajecten
        self.G = G
        self.max_trajecten = max_trajecten

    def calculate_Min(self, path):
        Min = nx.path_weight(self.G.graaf, path, weight = "weight")
        return Min

    def kies_trajecten(self):
        queue = self.trajecten
        gekozen_trajecten = []
        verbindingen_totaal = []
        trajecten_en_Min = dict()

        while len(gekozen_trajecten) < self.max_trajecten:
            langste_trajecten = list(filter(lambda x: len(x) == max(map(len,queue)), queue))

            for traject in langste_trajecten:
                Min = self.calculate_Min(traject)
                trajecten_en_Min[tuple(traject)] = Min
            langste_traject = list(min(trajecten_en_Min, key=trajecten_en_Min.get))

            verbindingen = from_paths_to_connections(langste_traject)
            overlap = False
            for verbinding in verbindingen:
                if verbinding in verbindingen_totaal or (verbinding[1], verbinding[0]) in verbindingen_totaal:
                    overlap = True
                    break
            if overlap:
                queue.remove(langste_traject)
                trajecten_en_Min.clear()
            else:
                gekozen_trajecten.append(langste_traject)
                verbindingen_totaal.extend(verbindingen)
                queue.remove(langste_traject)
                trajecten_en_Min.clear()

        score = calculate_score(self.G, gekozen_trajecten)
        
        return gekozen_trajecten, score


""" Versie waarbij meerdere langste lijsten en Min niet worden meegenomen """
# class Greedy:
#     def __init__(self, alle_trajecten, G, max_trajecten):
#         self.trajecten = alle_trajecten
#         self.G = G
#         self.max_trajecten = max_trajecten

#     def kies_trajecten(self):
#         queue = self.trajecten
#         gekozen_trajecten = []
#         verbindingen_totaal = []

#         while len(gekozen_trajecten) < self.max_trajecten:
#             langste_traject = max(queue, key=len)
#             verbindingen = from_paths_to_connections(langste_traject)
#             overlap = False
#             for verbinding in verbindingen:
#                 if verbinding in verbindingen_totaal or (verbinding[1], verbinding[0]) in verbindingen_totaal:
#                     overlap = True
#                     break
#             if overlap:
#                 queue.remove(langste_traject)
#             else:
#                 gekozen_trajecten.append(langste_traject)
#                 verbindingen_totaal.extend(verbindingen)
#                 queue.remove(langste_traject)
        
#         score = calculate_score(self.G, gekozen_trajecten)
        
#         return gekozen_trajecten, score


