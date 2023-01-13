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

#classes: stations, graph

from classes.station import Station
















    
