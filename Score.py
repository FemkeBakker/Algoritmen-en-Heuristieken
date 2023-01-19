# import libraries
import pandas as pd
from random import sample
import networkx as nx
import random

# import classes and functions
from classes.Graph import Graph
from random_solution import *

# load data Holland
# ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
# StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# # load data NL
# ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
# StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# create Graphs
# G_holland = Graph(ConnectiesHolland, StationsHolland)
# G_nederland = Graph(ConnectiesNationaal, StationsNationaal)

# function for removing duplicate tuples in list of tuples
def removeDuplicates(lst):
    return [j for j in (set(tuple(i) for i in lst))]

#function for calculating total score
def calculate_score(G, paths):
    Min = 0
    verbindingen = list()

    for path in paths:
        Min += nx.path_weight(G.graaf, path, weight = "weight")
        for station1, station2 in zip(path[0::], path[1::]):
            verbindingen.append((station1, station2))
    verbindingen = removeDuplicates(verbindingen)

    # fraction of total available connections
    p = len(verbindingen) / len(G.graaf.edges)

    # Total trajectories
    T = len(paths)
    
    # calculating score with formula
    K = (p * 10000 - (T * 100 + Min))
    return K


# generate all possible simple paths in graph
# alle_trajecten_holland = generate_all_trajecten(G_holland, 120)
# alle_trajecten_nl = generate_all_trajecten(G_nederland, 180)

# # get random solution, chosen from all possible simple paths in graph
# random_sol_holland = random_solution(alle_trajecten_holland, 7)
# random_sol_nl = random_solution(alle_trajecten_nl, 20)

# calculate score for Holland dataset
# random_score_holland = calculate_score(G_holland, random_sol_holland)
# print(random_score_holland)

# # # calculate score for Holland dataset
# random_score_nl = calculate_score(G_nederland, random_sol_nl)
# print(random_score_nl)