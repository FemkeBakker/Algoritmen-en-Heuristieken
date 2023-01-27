# CASE: RailNL - Team: RailNL-STF

# libraries
import pandas as pd
import networkx as nx
import folium
import random

# import class functions from the class files
from classes.station import Station
from classes.Graph import Graph
from Visualisatie.plot import create_boxplot, create_plot
from random_solution import *
from Score import *
from algorithms.HillClimber import HillClimber
from algorithms.Greedy_Constructive import *
from algorithms.Greedy_Iterative import Greedy_Iterative
from algorithms.SimAnnealing import SimAnnealing
from experiment.generate_experiment import *


# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
print(ConnectiesHolland)
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# save stations and connections from holland dataframes in lists
stations_holland = list(StationsHolland['station'])
connecties_holland = [(station1, station2) for station1, station2 in zip(ConnectiesHolland['station1'], ConnectiesHolland['station2'])]
# print(connecties_holland)

# load data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# save stations and connections from national dataframes in lists
stations_nationaal = list(StationsNationaal['station'])
connecties_nationaal = [(station1, station2) for station1, station2 in zip(ConnectiesNationaal['station1'], ConnectiesNationaal['station2'])]

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

create_plot(random_sol_holland, StationsHolland, "Random_sol_Holland") 


# calculate and print scores from random/baseline algorithm for both holland and NL datasets
random_score_holland = calculate_score(G_holland, random_sol_holland)
random_score_nl = calculate_score(G_nederland, random_sol_nl)

print("Baseline score Holland: ",random_score_holland)
# print("Baseline score Nederland: ",random_score_nl)

# run Hill Climber
hill_climber = HillClimber(random_sol_holland, alle_trajecten_holland, G_holland)
# print(hill_climber.score_state)
hill_climber.run(200)
# print(hill_climber.score_state)

# run Simulated Annealing
sim_annealing = SimAnnealing(random_sol_holland, alle_trajecten_holland, G_holland)
# print(sim_annealing.score_state)
sim_annealing.run(2000)
# print(sim_annealing.score_state)

# create instance of Greedy
# greedy_holland = Greedy(alle_trajecten_holland, G_holland, 7)

# print greedy trajecten en score holland
# print(greedy_holland.kies_trajecten())

 
# beginstate = {'Greedy' : random_sol_holland} 
# iteraties = [10, 100, 200]
iteraties = [2000]
# iteraties = [200, 500, 1000, 2000,5000, 8000, 10000, 12000, 14000, 15000]
#experiment = generate_experiment(HillClimber, iteraties, 150, alle_trajecten_holland, 7, "Holland", G_holland)
#experiment = generate_experiment(SimAnnealing, iteraties, 150, alle_trajecten_holland, 7, "Holland", G_holland)
#experiment.run_experiment()

#plot data in boxplot
# data_HC = pd.read_csv('experiment\HillClimber-random-Holland\iteratie2000.csv')
# data_SA = pd.read_csv('experiment\SimAnnealing-random-Holland\iteratie2000.csv')

# data = pd.DataFrame(columns=['HillClimber', 'SimulatedAnnealing'])
# data['HillClimber'] = list(data_HC['eind_score'])
# data['SimulatedAnnealing'] = list(data_SA['eind_score'])
# # data['SimulatedAnnealing'] = data_SA['eind_score'].values()
# # creëer tuple voor data argument
# # data = (data_HC, data_SA)
# #print(data)
# create_boxplot(data,'Holland')

# print(pd.read_csv("experiment/SimAnnealing-random/info_data.csv"))

# create instance of Greedy Constructive for holland
# greedy_constructive_holland = Greedy_Constructive(alle_trajecten_holland, G_holland, 7)
# print greedy constructive trajecten and score for holland
# print(greedy_constructive_holland.kies_trajecten())

# create instance of Greedy Iterative for holland
greedy_iterative_holland = Greedy_Iterative(G_holland, stations_holland, connecties_holland, 7, 120)
greddu = greedy_iterative_holland.kies_trajecten()
# print greedy iterative trajecten en score holland
print(greedy_iterative_holland.kies_trajecten())
print(len(greedy_iterative_holland.kies_trajecten()))
# print(calculate_score(G_holland, greddu))
# print(connecties_holland)
