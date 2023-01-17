import pandas as pd
from random import sample
import networkx as nx
import random

from classes.Graph import Graph
from random_solution import *

ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

G_holland = Graph(ConnectiesHolland, StationsHolland)

def removeDuplicates(lst):
    return [j for j in (set(tuple(i) for i in lst))]

def calculate_score(G, paths):
    Min= 0
    verbindingen = list()
    for path in paths:
        Min += nx.path_weight(G.graaf, path, weight = "weight")
        for station1, station2 in zip(path[0::], path[1::]):
            verbindingen.append((station1, station2))
    verbindingen = removeDuplicates(verbindingen)

    p = len(verbindingen) / len(G.graaf.edges)
    T = len(paths)
    # print(p, Min, T)
    
    K = p * 1000 - (T * 100 + Min)
    return K


random_score = calculate_score(G_holland, random_sol)
print(random_score)

# def score(G, paths):
#     Min = 0
#     stations = list()
#     for path in paths:
#         Min += nx.path_weight(G.graaf, path, weight = "weight")
#         stations.extend(path)
#     stations = set(stations)
#     p = len(stations) / len(G.graaf.edges)

#     print(p, stations, len(G.graaf.edges), Min)