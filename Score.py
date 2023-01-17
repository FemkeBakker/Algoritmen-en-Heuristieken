# import libraries
import pandas as pd
from random import sample
import networkx as nx
import random

# import classes
from classes.Graph import Graph
from random_solution import *

# load dataframes from csv files
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# create graph (using Graph() function) for Holland dataset
G_holland = Graph(ConnectiesHolland, StationsHolland)

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

# calculate score for Holland dataset
random_score = calculate_score(G_holland, random_sol)
print(random_score)

# # import libraries
# import pandas as pd
# from random import sample
# import networkx as nx
# import random

# # import classes
# from classes.Graph import Graph
# from random_solution import *

# # load dataframes from csv files
# ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
# StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# # create graph (using Graph() function) for Holland dataset
# G_holland = Graph(ConnectiesHolland, StationsHolland)

# # function for removing duplicate tuples in list of tuples
# def removeDuplicates(lst):
#     return [j for j in (set(tuple(i) for i in lst))]

# #function for calculating total score
# def calculate_score(G, paths):
#     Min = 0
#     verbindingen = list()

#     for path in paths:
#         Min += nx.path_weight(G.graaf, path, weight = "weight")
#         for station1, station2 in zip(path[0::], path[1::]):
#             verbindingen.append((station1, station2))
#     verbindingen = removeDuplicates(verbindingen)

#     # fraction of total available connections
#     p = len(verbindingen) / len(G.graaf.edges)

#     # Total trajectories
#     T = len(paths)
    
#     # calculating score with formula
#     K = (p * 10000 - (T * 100 + Min))
#     return K

# # calculate score for Holland dataset
# random_score = calculate_score(G_holland, random_sol)
# print(random_score)

# # import libraries
# import pandas as pd
# from random import sample
# import networkx as nx
# import random

# # import classes
# from classes.Graph import Graph
# from random_solution import *

# # load dataframes from csv files
# ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
# StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# # create graph (using Graph() function) for Holland dataset
# G_holland = Graph(ConnectiesHolland, StationsHolland)

# # function for removing duplicate tuples in list of tuples
# def removeDuplicates(lst):
#     return [j for j in (set(tuple(i) for i in lst))]

# #function for calculating total score
# def calculate_score(G, paths):
#     Min = 0
#     verbindingen = list()

#     for path in paths:
#         Min += nx.path_weight(G.graaf, path, weight = "weight")
#         for station1, station2 in zip(path[0::], path[1::]):
#             verbindingen.append((station1, station2))
#     verbindingen = removeDuplicates(verbindingen)

#     # fraction of total available connections
#     p = len(verbindingen) / len(G.graaf.edges)

#     # Total trajectories
#     T = len(paths)
    
#     # calculating score with formula
#     K = (p * 10000 - (T * 100 + Min))
#     return K

# # calculate score for Holland dataset
# random_score = calculate_score(G_holland, random_sol)
# print(random_score) 