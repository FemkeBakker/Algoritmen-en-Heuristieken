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

""" PSEUDO-CODE VOOR ITERATIVE 'GREEDY' ALGORITME """
# 

""" Versie waarbij meerdere langste lijsten worden gefilterd op laagste Min """
class Greedy:
    def __init__(self, alle_trajecten, G, max_trajecten):
        self.trajecten = alle_trajecten
        self.G = G
        self.max_trajecten = max_trajecten

    def 