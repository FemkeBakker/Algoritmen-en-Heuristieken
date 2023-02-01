# import functions
from Score import *
from algorithms.random_solution import *
from connections_paths import *

# libraries
import pandas as pd
import networkx as nx

# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# save stations and connections from holland dataframes in lists
stations_holland = list(StationsHolland['station'])
connecties_holland = [(station1, station2) for station1, station2 in zip(ConnectiesHolland['station1'], ConnectiesHolland['station2'])]

# load data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# save stations and connections from national dataframes in lists
stations_nationaal = list(StationsNationaal['station'])
connecties_nationaal = [(station1, station2) for station1, station2 in zip(ConnectiesNationaal['station1'], ConnectiesNationaal['station2'])]

# create Graph instances
G_holland = Graph(ConnectiesHolland, StationsHolland)
G_nederland = Graph(ConnectiesNationaal, StationsNationaal)

""" PSEUDO-CODE VOOR ITERATIVE 'GREEDY' ALGORITME """
# Initialiseer lege lijst 'gekozen_trajecten' om gekozen routes op te slaan
# Initialiseer set 'unieke_verbindingen' om verbindingen die al gebruikt zijn op te slaan
# Herhaal stap 4 tot 7 zolang de lengte van 'gekozen_trajecten' kleiner is dan 7:
#   Initialiseer lege lijst 'traject' om huidige route op te slaan
#   Initialiseer variabele 'totale_Min' op 0
#   Herhaal volgende stap zolang 'totale_Min' kleiner of gelijk is aan 'self.max_Min' EN 'verbindingen' niet leeg is:
#       Initialiseer variabele 'volgende_verbinding' als de verbinding met de laagste Min waarde die nog niet in 'unieke_verbindingen' voorkomt en aansluitend is op de laatst gekozen verbinding in 'traject'
#       Voeg 'volgende_verbinding' toe aan 'traject'
#       Voeg 'volgende_verbinding' toe aan 'unieke_verbinding'
#       Voeg 'volgende_verbinding' Min waarde toe aan 'totale_Min'
#       Verwijder 'volgende_verbinding' uit 'verbindingen'
#   Als 'traject' niet leeg is, voeg 'traject' toe aan 'gekozen_trajecten'
# Return 'gekozen_trajecten'


""" Versie 1: verbindingen gaan beide kanten op """
class Greedy_Iterative:
    def __init__(self, G, alle_stations, alle_connecties, max_trajecten, max_Min):
        self.G = G
        self.stations = alle_stations
        self.connecties = alle_connecties
        self.max_trajecten = max_trajecten
        self.max_Min = max_Min

    # function for calculating Min for a single traject or connection
    def calculate_Min(self, path):
        Min = nx.path_weight(self.G.graaf, path, weight = "weight")
        return Min

    # function for transforming output
    def output(self, gekozen_trajecten):
        nieuwe_trajecten = []
        for traject in gekozen_trajecten:
            nieuw_traject = []
            for verbinding in traject:
                nieuw_traject.extend([verbinding[0],verbinding[1]])
            # remove duplicates from list
            nieuw_traject = list(set(nieuw_traject))
            nieuwe_trajecten.append(nieuw_traject)
        return nieuwe_trajecten


    def kies_trajecten(self):
        verbindingen = self.connecties
        gekozen_trajecten = []
        unieke_verbindingen = set()
        while len(gekozen_trajecten) < self.max_trajecten:
            traject = []
            totale_Min = 0
            while totale_Min <= self.max_Min and verbindingen:
                # kies volgende verbinding
                volgende_verbinding = None
                for verbinding in verbindingen:
                    if nx.has_path(self.G.graaf, verbinding[0], verbinding[1]) and (verbinding[0],verbinding[1]) not in unieke_verbindingen and (verbinding[1],verbinding[0]) not in unieke_verbindingen and (len(traject)==0 or verbinding[0]==traject[-1][1]):
                        Min = nx.path_weight(self.G.graaf,verbinding, weight = "weight")
                        volgende_verbinding = (verbinding[0], verbinding[1], Min)
                        if volgende_verbinding[2] <= self.max_Min - totale_Min:
                            break
                    else:
                        volgende_verbinding = None
                if volgende_verbinding is None:
                    break
            # Add the connection to the route
                traject.append(volgende_verbinding)
                unieke_verbindingen.add(volgende_verbinding[:2])
                totale_Min += volgende_verbinding[2]
                verbindingen.remove(volgende_verbinding[:2])
            if traject:
                gekozen_trajecten.append(traject)
            
        gekozen_trajecten = self.output(gekozen_trajecten)
        # score = calculate_score(self.G, gekozen_trajecten)
        return gekozen_trajecten


# """ Versie: volgorde van lijst """
# class Greedy_Iterative:
#     def __init__(self, G, alle_stations, alle_connecties, max_trajecten, max_Min):
#         self.G = G
#         self.stations = alle_stations
#         self.connecties = alle_connecties
#         self.max_trajecten = max_trajecten
#         self.max_Min = max_Min

#     # function for calculating Min for a single traject or connection
#     def calculate_Min(self, path):
#         Min = nx.path_weight(self.G.graaf, path, weight = "weight")
#         return Min

#     # function for transforming output
#     def output(self, gekozen_trajecten):
#         nieuwe_trajecten = []
#         for traject in gekozen_trajecten:
#             nieuw_traject = []
#             for verbinding in traject:
#                 nieuw_traject.extend([verbinding[0],verbinding[1]])
#             # remove duplicates from list
#             nieuw_traject = list(set(nieuw_traject))
#             nieuwe_trajecten.append(nieuw_traject)
#         return nieuwe_trajecten


#     def kies_trajecten(self):
#         verbindingen = self.connecties
#         gekozen_trajecten = []
#         unieke_verbindingen = set()
#         while len(gekozen_trajecten) < self.max_trajecten:
#             traject = []
#             totale_Min = 0
#             i=0
#             while totale_Min <= self.max_Min and i < len(verbindingen):
#                 verbinding = verbindingen[i]
#                 if (len(traject) == 0 or verbinding[0] == traject[-1][1]) and (verbinding[0], verbinding[1]) not in unieke_verbindingen:
#                     Min = nx.path_weight(self.G.graaf,verbinding, weight = "weight")
#                     if Min <= self.max_Min - totale_Min:
#                         volgende_verbinding = (verbinding[0], verbinding[1], Min)
#                         # Add the connection to the route
#                         traject.append(volgende_verbinding)
#                         unieke_verbindingen.add(volgende_verbinding[:2])
#                         totale_Min += volgende_verbinding[2]
#                 i += 1
#             if traject:
#                 gekozen_trajecten.append(traject)
            
#         gekozen_trajecten = self.output(gekozen_trajecten)
#         score = calculate_score(self.G, gekozen_trajecten)
#         return gekozen_trajecten



# class Greedy_Iterative:
#     def __init__(self, G, alle_stations, alle_connecties, max_trajecten, max_Min):
#         self.G = G
#         self.stations = alle_stations
#         self.connecties = alle_connecties
#         self.max_trajecten = max_trajecten
#         self.max_Min = max_Min

#     # function for calculating Min for a single traject or connection
#     def calculate_Min(self, path):
#         Min = nx.path_weight(self.G.graaf, path, weight = "weight")
#         return Min

#     def kies_trajecten(self):
#         verbindingen = self.connecties
#         gekozen_trajecten = []
#         unieke_verbindingen = set()

#         while len(gekozen_trajecten) < self.max_trajecten:
#             traject = []
#             totale_Min = 0
#             while totale_Min <= self.max_Min and verbindingen:
#                 if len(traject) > 0:
#                     volgende_verbinding = min([verbinding for verbinding in  verbindingen if (verbinding[0]==traject[-1][1]) and self.calculate_Min(list(verbinding)) <= self.max_Min - totale_Min and verbinding not in unieke_verbindingen], key=lambda x: self.calculate_Min(x))
#                 else:
#                     volgende_verbinding = min([verbinding for verbinding in verbindingen if self.calculate_Min(verbinding) <= self.max_Min - totale_Min and verbinding not in unieke_verbindingen], key=lambda x: self.calculate_Min(x))
#                 # bereken Min voor de verbinding
#                 huidige_Min = self.calculate_Min(volgende_verbinding)
#                 totale_Min += huidige_Min
#                 if totale_Min <= self.max_Min:
#                     traject.append(volgende_verbinding)
#                     unieke_verbindingen.add(volgende_verbinding)
#                     verbindingen.remove(volgende_verbinding)
#             if traject:
#                 gekozen_trajecten.append(traject)
#         return gekozen_trajecten



    # def kies_trajecten(self):
    #     verbindingen = self.connecties
    #     gekozen_trajecten = []
    #     unieke_verbindingen = set()

    #     while len(gekozen_trajecten) < self.max_trajecten:
    #         traject = []
    #         totale_Min = 0
    #         while totale_Min <= self.max_Min and verbindingen:
    #             volgende_verbinding = min([verbinding for verbinding in verbindingen if verbinding[1] <= self.max_Min - huidige_Min and (verbinding not in unieke_verbindingen) and (len(traject) == 0 or verbinding[0] == traject[-1][1])], key=lambda x: x[1])
    #             # bereken Min voor de verbinding
    #             huidige_Min = self.calculate_Min(volgende_verbinding)
    #             totale_Min += huidige_Min
    #             if totale_Min >= self.max_Min:
    #                 break
    #             traject.append(volgende_verbinding)
    #             unieke_verbindingen.add(volgende_verbinding[:2])
    #             huidige_Min += volgende_verbinding[2]
    #             verbindingen.remove(volgende_verbinding)
    #         if route:
    #             gekozen_trajecten.append(traject)
    #     return gekozen_trajecten