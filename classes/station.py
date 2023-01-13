# CASE: RailNL - Team: RailNL-STF

#libraries
import pandas as pd
import numpy as np 

class Station:
    def __init__(self, station, df_connecties, x=np.nan, y=np.nan):
        self.station = station
        self.x = x
        self.y = y
        self.connection_incoming = self.add_connections_incoming(df_connecties) # dict with all stations and corresponding distance of all incoming connections
        self.connection_outgoing = self.add_connections_outgoing(df_connecties) # dict with all station and corresponding distance of all outgoing connections
        self.connection_count = len(self.connection_incoming) + len(self.connection_outgoing) # shows how central the station is 
        self.begin_station = self.is_begin_station()
        self.end_station = self.is_end_station()


    # will add all incoming connections. An incomming connection is a connection where station is station2 and the other station is station1
    def add_connections_incoming(self, df_connecties):
        c_incoming = df_connecties.loc[df_connecties['station2'] == self.station]
        c_incoming_dict = {}
        for index, row in c_incoming.iterrows():
            c_incoming_dict[row['station1']] = row['distance']
        
        return c_incoming_dict

    # will add all outgoing connections. An outgoing connection is a connection where station is station1 and the other station is station2
    def add_connections_outgoing(self, df_connecties):
        c_outgoing = df_connecties.loc[df_connecties['station1'] == self.station]
        c_outgoing_dict = {}
        for index, row in c_outgoing.iterrows():
            c_outgoing_dict[row['station2']] = row['distance']
        
        return c_outgoing_dict
          
    def is_begin_station(self):
        if len(self.connection_incoming) == 0:
            return True
        else:
            return False

    def is_end_station(self):
        if len(self.connection_outgoing) == 0:
            return True
        else:
            return False

















    
