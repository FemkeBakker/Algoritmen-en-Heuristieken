# CASE: RailNL - Team: RailNL-STF

# libraries
import pandas as pd

# import class functions from the class files
from classes.station import Station
from classes.graph import Graph

# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# load data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# create Graph instances
G_holland = Graph(ConnectiesHolland, StationsHolland)
G_nederland = Graph(ConnectiesNationaal, StationsNationaal)

# return dict with station as key and value as the Station class instance of that station
def make_instances_station(df_stations, df_connecties):
    stations = dict()
    for station in df_stations['station'].values:
        stations[station] = Station(station, df_connecties)
    return stations

# create Station instances
stations_holland_class = make_instances_station(StationsHolland, ConnectiesHolland)
stations_nl_class = make_instances_station(StationsNationaal, ConnectiesNationaal)





