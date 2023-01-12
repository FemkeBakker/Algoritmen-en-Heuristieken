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

#classes: stations, verbindingen, trajecten

class Station:
    def __init__(self, station, x=np.nan, y=np.nan):
        self.station = station
        self.x = x
        self.y = y
        self.neighbors_incoming = {} # dict with all stations and corresponding distance of all incoming connections
        self.neighbors_outgoing = {} # dict with all station and corresponding distance of all outgoing connections

    # will add all connections the station has to other stations. Distingushed between outgoing and incoming connections.
    def add_neighborhood(self, df):

        # outgoing connection: where station1 is the station and station2 the station where the train travels too.
        n_outgoing = df.loc[df['station1'] == self.station]
        n_outgoing_dict = {}
        for index, row in n_outgoing.iterrows():
            n_outgoing_dict[row['station2']] = row['distance']

        self.neighbors_outgoing = n_outgoing_dict

        # incoming connection: where station2 is the station and station1 the station where the train travels too.
        n_incoming = df.loc[df['station2'] == self.station]
        n_incoming_dict = {}
        for index, row in n_incoming.iterrows():
            n_incoming_dict[row['station1']] = row['distance']

        self.neighbors_incoming = n_incoming_dict







    
