# CASE: RailNL - Team: RailNL-STF

# libraries
import pandas as pd
import networkx as nx
import folium
import random

# import class functions from the class files
from classes.station import Station
from classes.Graph import Graph
from Visualisatie.plot import create_plot
from random_solution import *
from Score import *
from algorithms.HillClimber import HillClimber
from algorithms.Greedy import Greedy
from algorithms.SimAnnealing import SimAnnealing

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
        stations[station] = Station(station, df_connecties, df_stations)
    return stations

# create Station instances
stations_holland_class = make_instances_station(StationsHolland, ConnectiesHolland)
stations_nl_class = make_instances_station(StationsNationaal, ConnectiesNationaal)

# example input for plot visualization
trajecten = [["Beverwijk", "Castricum", "Alkmaar", "Hoorn", "Zaandam"], 
["Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Amsterdam Zuid", "Schiphol Airport"], 
["Rotterdam Alexander", "Gouda", "Alphen a/d Rijn", "Leiden Centraal"," Schiphol Airport", "Amsterdam Zuid"]]

# creates plot of trajecten, return None, map can be found in Visualisatie/map.html
create_plot(trajecten, StationsHolland, "Holland") 
create_plot(trajecten, StationsNationaal, "NL")

# generate all possible simple paths in graph
alle_trajecten_holland = generate_all_trajecten(G_holland, 120)
alle_trajecten_nl = generate_all_trajecten(G_nederland, 180)

# get random solution, chosen from all possible simple paths in graph
random_sol_holland = random_solution(alle_trajecten_holland, 7)
random_sol_nl = random_solution(alle_trajecten_nl, 20)

# calculate and print scores from random/baseline algorithm for both holland and NL datasets
random_score_holland = calculate_score(G_holland, random_sol_holland)
random_score_nl = calculate_score(G_nederland, random_sol_nl)

# print("Random score Holland: ",random_score_holland)
# print("Random score Nederland: ",random_score_nl)

# run Hill Climber
hill_climber = HillClimber(random_sol_holland, alle_trajecten_holland, G_holland)
print(hill_climber.score_state)
hill_climber.climbing_hill(2000)
print(hill_climber.score_state)

# run Simulated Annealing
sim_annealing = SimAnnealing(random_sol_holland, alle_trajecten_holland, G_holland)
# print(sim_annealing.score_state)
sim_annealing.Simulate_Annealing(2000)
# print(sim_annealing.score_state)

# create instance of Greedy
greedy_holland = Greedy(alle_trajecten_holland, G_holland, 7)

# print greedy trajecten en score holland
# print(greedy_holland.kies_trajecten())