import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt 
import math as math

class Graph():
    def __init__(self, df_connecties, df_stations):
        self.stations = self.get_stations(df_stations)
        self.connections = self.get_connections(df_connecties)
        self.graaf = self.make_graph()

    def get_stations(self, df_stations):
        return [station for station in df_stations['station'].values]

    def get_connections(self, df_connecties):
        station1=[station for station in df_connecties['station1'].values]
        station2=[station for station in df_connecties['station2'].values]
        reistijd=[tijd for tijd in df_connecties['distance'].values]

        connections = list(zip(station1, station2, reistijd)) 
        return connections

    # function that creates a directed Graph with edges and nodes
    def make_graph(self):
        graaf = nx.DiGraph()
        graaf.add_nodes_from(self.stations)
        graaf.add_weighted_edges_from(self.connections)
        return graaf

# ---- Draw a graph - to check funtion, not relevant for the solution ---- #

# # load data Deel 1 - Noord-Holland & Zuid-Holland
# ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
# StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# # # load data deel 2 - Heel NL
# ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
# StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# G = Graph(ConnectiesHolland, StationsHolland)

# # # Teken de graaf en sla op als png in project map
# nx.draw(G.graaf, with_labels=True)
# label_weights = nx.get_edge_attributes(G.graaf,'weight')

# pos=nx.spring_layout(G.graaf, seed=7, k=5/math.sqrt(G.graaf.order()))
# nx.draw_networkx_edge_labels(G.graaf, pos, edge_labels=label_weights)
# plt.savefig("graph1.png")
    
