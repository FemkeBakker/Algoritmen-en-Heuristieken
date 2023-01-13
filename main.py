# CASE: RailNL - Team: RailNL-STF

#libraries
import pandas as pd
import numpy as np 

# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# load data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# all stations in NH & NZ
# stations_Holland = set(StationsNationaal['station'])

#classes: stations, graph, trajecten

from classes.station import Station

# alkmaar = Station("Alkmaar", ConnectiesHolland)
# print(alkmaar.connection_count)

# class Graph():
#     def __init__(self, df_connecties, df_stations):
#         self.stations = self.get_stations(df_stations)


#     def get_stations(self, df_stations):
#         return {station:station for station in df_stations['station'].values}

# graaf = Graph(ConnectiesHolland, StationsHolland)
# print(graaf.stations)














    
