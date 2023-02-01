# import functions
from Score import *
from algorithms.random_solution import *
from connections_paths import *

# libraries
import networkx as nx

""" Versie 1: verbindingen gaan beide kanten op """
class Greedy_Iterative:
    def __init__(self, G, alle_stations, alle_connecties, max_trajecten, max_Min):
        self.G = G
        self.stations = alle_stations
        self.connecties = alle_connecties
        self.max_trajecten = max_trajecten
        self.max_Min = max_Min

    # functie voor het berekenen van het aantal minuten van 1 traject.
    def calculate_Min(self, path):
        Min = nx.path_weight(self.G.graaf, path, weight = "weight")
        return Min

    # functie voor transformeren van output
    def output(self, gekozen_trajecten):
        nieuwe_trajecten = []
        for traject in gekozen_trajecten:
            nieuw_traject = []
            for verbinding in traject:
                nieuw_traject.extend([verbinding[0],verbinding[1]])

            # verwijder dubbelen uit lijst
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

            # voeg connectie toe aan route
                traject.append(volgende_verbinding)
                unieke_verbindingen.add(volgende_verbinding[:2])
                totale_Min += volgende_verbinding[2]
                verbindingen.remove(volgende_verbinding[:2])
            if traject:
                gekozen_trajecten.append(traject)
            
        gekozen_trajecten = self.output(gekozen_trajecten)
        return gekozen_trajecten