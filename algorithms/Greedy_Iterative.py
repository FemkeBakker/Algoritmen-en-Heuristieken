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
# Neem

""" Versie waarbij meerdere langste lijsten worden gefilterd op laagste Min """
class Greedy_Iterative:
    def __init__(self, G, alle_stations, alle_connecties, max_trajecten, max_Min):
        self.G = G
        self.stations = alle_stations
        self.connecties = alle_connecties
        self.max_trajecten = max_trajecten
        self.max_Min = max_Min

    def kies_trajecten(self):
        
