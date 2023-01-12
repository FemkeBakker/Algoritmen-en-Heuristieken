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
        self.connection_count = 0
        self.connection_incoming = {} # dict with all stations and corresponding distance of all incoming connections
        self.connection_outgoing = {} # dict with all station and corresponding distance of all outgoing connections

    # will add all connections the station has to other stations. Distingushed between outgoing and incoming connections.
    def add_connections(self, df):

        # outgoing connection: where station1 is the station and station2 the station where the train travels too.
        c_outgoing = df.loc[df['station1'] == self.station]
        c_outgoing_dict = {}
        for index, row in c_outgoing.iterrows():
            c_outgoing_dict[row['station2']] = row['distance']

        self.connection_outgoing = c_outgoing_dict

        # incoming connection: where station2 is the station and station1 the station where the train travels too.
        c_incoming = df.loc[df['station2'] == self.station]
        c_incoming_dict = {}
        for index, row in c_incoming.iterrows():
            c_incoming_dict[row['station1']] = row['distance']

        self.connection_incoming = c_incoming_dict

        # add connection_count, shows how central the station is
        self.connection_count = len(c_outgoing_dict) + len(c_incoming_dict)  

    def is_begin_station(self):
        if len(self.connection_incoming) == 0:
            self.begin_station = True
        else:
            self.begin_station = False

    def is_end_station(self):
        if len(self.connection_outgoing) == 0:
            self.end_station = True
        else:
            self.end_station = True









    
