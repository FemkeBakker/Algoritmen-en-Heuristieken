import pandas as pd
from random import sample
import networkx as nx
import random

from classes.Graph import Graph

ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

G_holland = Graph(ConnectiesHolland, StationsHolland)

def generate_all_trajecten(G):
    all_paths = list()
    for station1 in G.stations:
        for station2 in G.stations:
            paths = list(nx.all_simple_paths(G.graaf, station1, station2))
            for path in paths:
                if nx.path_weight(G.graaf, path, weight = "weight") <= 120:
                    all_paths.append(path)
    return (all_paths)

all_trajecten = generate_all_trajecten(G_holland)

def random_solution(trajecten):
    solution = random.sample(trajecten, k=7)
    return(solution)

random_sol = random_solution(all_trajecten)
