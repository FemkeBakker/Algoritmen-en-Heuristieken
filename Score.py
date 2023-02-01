# import libraries
from random import sample
import networkx as nx

# import functions
from algorithms.random_solution import *

# functie voor het verwijderen van dubbelen tuples in een lijst
def removeDuplicates(lst):
    return [j for j in (set(tuple(i) for i in lst))]

# functie voor het berekenen van de totale score
def calculate_score(G, paths):
    Min = 0
    verbindingen = list()

    for path in paths:
        Min += nx.path_weight(G.graaf, path, weight = "weight")
        for station1, station2 in zip(path[0::], path[1::]):
            verbindingen.append((station1, station2))
    verbindingen = removeDuplicates(verbindingen)

    # fractie van alle connecties
    p = len(verbindingen) / len(G.graaf.edges)

    # Totaal trajecten
    T = len(paths)
    
    # score bereken met de gegeven score formule
    K = (p * 10000 - (T * 100 + Min))
    return K
