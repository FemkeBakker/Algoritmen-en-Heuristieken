import networkx as nx
import pandas as pd
import numpy as np 

# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# load data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

class Graph():
    def __init__(self, df_connecties, df_stations):
        # self.graaf = nx.Graph()
        self.stations = self.get_stations(df_stations)
        self.connections = self.get_connections(df_connecties)
        self.graaf = self.make_graph()

    def get_stations(self, df_stations):
        return [station for station in df_stations['station'].values]

    def get_connections(self, df_connecties):
        station1=[station for station in df_connecties['station1'].values]
        station2=[station for station in df_connecties['station2'].values]
        connections = list(zip(station1, station2)) 
        return connections

    def make_graph(self):
        graaf = nx.Graph()
        graaf.add_nodes_from(self.stations)
        graaf.add_edges_from(self.connections)
        return graaf

G = Graph(ConnectiesHolland, StationsHolland)
print(G.graaf)
    
# G = nx.Graph()
# graaf = Graph(ConnectiesHolland, StationsHolland)
# G.add_nodes_from(graaf.stations)
# G.add_edges_from(graaf.connections)
# print(G)



# class Graph():
#     def __init__(self, df_connecties, df_stations):
#         self.stations = self.get_stations(df_stations)
#         self.connections = self.get_connections(df_connecties)


#     def get_stations(self, df_stations):
#         return [station for station in df_stations['station'].values]

#     def get_connections(self, df_connecties):
#         station1=[station for station in df_connecties['station1'].values]
#         station2=[station for station in df_connecties['station2'].values]
#         connections = list(zip(station1, station2)) 
#         return connections
    
    

# G = nx.Graph()
# graaf = Graph(ConnectiesHolland, StationsHolland)
# G.add_nodes_from(graaf.stations)
# G.add_edges_from(graaf.connections)
# print(G)