import networkx as nx
import math as math

class Graph():
    def __init__(self, df_connecties, df_stations):
        self.stations = self.get_stations(df_stations)
        self.connections = self.get_connections(df_connecties)
        self.graaf = self.make_graph()

    # functie returnt een lijst met alle stations
    def get_stations(self, df_stations):
        return [station for station in df_stations['station'].values]

    # functie returnt een lijst met alle conneties en de reistijd van de connectie
    def get_connections(self, df_connecties):
        station1=[station for station in df_connecties['station1'].values]
        station2=[station for station in df_connecties['station2'].values]
        reistijd=[tijd for tijd in df_connecties['distance'].values]

        connections = list(zip(station1, station2, reistijd)) 
        return connections

    # functie creërt een directed Graph met stations als edges, connecties als edges en reistijd als weights.
    def make_graph(self):
        graaf = nx.DiGraph()
        graaf.add_nodes_from(self.stations)
        graaf.add_weighted_edges_from(self.connections)
        return graaf

    
