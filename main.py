# CASE: RailNL - Team: RailNL-STF

# libraries
import pandas as pd
import networkx as nx
import folium
import random

# import class functions from the class files
from classes.station import Station
from classes.Graph import Graph
from Visualisatie.plot import create_boxplot, create_plot, generate_data
from random_solution import *
from Score import *
from algorithms.HillClimber import HillClimber
from algorithms.Greedy_Constructive import *
from algorithms.Greedy_Iterative import Greedy_Iterative
from algorithms.SimAnnealing import SimAnnealing
from experiment.generate_experiment import *


# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
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
<<<<<<< Updated upstream
# hill_climber = HillClimber(random_sol_holland, alle_trajecten_holland, G_holland)
# print(hill_climber.score_state)
# hill_climber.run(200)
=======
#hill_climber = HillClimber(random_sol_holland, alle_trajecten_holland, G_holland)
# print(hill_climber.score_state)
#hill_climber.run(200)
>>>>>>> Stashed changes
# print(hill_climber.score_state)

# run Simulated Annealing
#sim_annealing = SimAnnealing(random_sol_holland, alle_trajecten_holland, G_holland)
# print(sim_annealing.score_state)
#sim_annealing.run(2000)
# print(sim_annealing.score_state)

# create instance of Greedy Constructive Holland
greedy_contructief_holland = Greedy_Constructive(alle_trajecten_holland, G_holland, 7)
greedy_con_holland_solution, greedy_con_holland_solution_score = greedy_contructief_holland.kies_trajecten()

# create instance of Greedy Constructive NL
greedy_contructief_nl = Greedy_Constructive(alle_trajecten_nl, G_nederland, 20)
greedy_con_nl_solution, greedy_con_nl_solution_score = greedy_contructief_nl.kies_trajecten()


# ----------- Experiment Hill-Climber -------------------#

iteraties = [200, 500, 1000, 2000, 5000, 8000, 10000, 12000, 14000, 15000]
experiment_count = 150
holland_aantal_trajecten = 7
nl_aantal_trajecten = 20

# 7 langste trajecten in Holland
# copy_alle_trajecten_holland = alle_trajecten_holland.copy()
# langste_trajecten_holland = sorted(copy_alle_trajecten_holland, key = len, reverse=True)[0:holland_aantal_trajecten]

# 20 langste trajecten in NL
# copy_alle_trajecten_nl = alle_trajecten_nl.copy()
# langste_trajecten_nl = sorted(copy_alle_trajecten_nl, key = len, reverse=True)[0:nl_aantal_trajecten]

# Greedy constructive Holland
# greedy_contructief_holland = Greedy_Constructive(alle_trajecten_holland, G_holland, 7)
# greedy_con_holland_solution, greedy_con_holland_solution_score = greedy_contructief_holland.kies_trajecten()

# Greedy constructive Nederland
# greedy_contructief_nl = Greedy_Constructive(alle_trajecten_nl, G_nederland, nl_aantal_trajecten)
# greedy_con_nl_solution, greedy_con_nl_solution_score = greedy_contructief_nl.kies_trajecten()

# Random beginstate - Holland
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_holland, holland_aantal_trajecten, "Holland", G_holland)
# experiment.run_experiment()

# Random beginstate - Nederland
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_nl, nl_aantal_trajecten, "Nederland", G_nederland)
# experiment.run_experiment()

# 7 langste trajecten beginstate - Holland
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_holland, holland_aantal_trajecten, "Holland", G_holland, {"7langste":langste_trajecten_holland})
# experiment.run_experiment()

<<<<<<< Updated upstream
# 7 langste trajecten beginstate - Nederland
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_nl, nl_aantal_trajecten, "Nederland", G_nederland, {"7langste":langste_trajecten_nl})
# experiment.run_experiment()

# Constructieve Greedy beginste - Holland
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_holland, holland_aantal_trajecten, "Holland", G_holland, {"Greedy_con":greedy_con_holland_solution})
# experiment.run_experiment()

# Constructieve Greedy beginste - Nederland
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_nl, nl_aantal_trajecten, "Nederland", G_nederland, {"Greedy_con":greedy_con_nl_solution})
# experiment.run_experiment()


#plot data in boxplot
# data_HC = pd.read_csv('experiment\HillClimber-random-Holland\iteratie1000.csv')
# data_SA = pd.read_csv('experiment\SimAnnealing-random-Holland\iteratie2s000.csv')
# # creëer tuple voor data argument
# data =data_HC.iloc[:,1], data_SA.iloc[:,1]
# print(data)
# create_boxplot(data,'Holland')
=======

iteraties = [200,500, 1000, 2000, 5000, 10000, 15000]
# experiment = generate_experiment(SimAnnealing, iteraties, 150, alle_trajecten_nl, 20, "Nederland", G_nederland)
#
# experiment.run_experiment()

data = generate_data(iteraties, "experiment\SimAnnealing-random-Nederland\iteratie")

print(data)
create_boxplot(data,'SA, Nederland', 'Iteraties', iteraties, 'Simulated Annealing')
>>>>>>> Stashed changes

# print(pd.read_csv("experiment/SimAnnealing-random/info_data.csv"))

# create instance of Greedy Constructive for holland
# greedy_constructive_holland = Greedy_Constructive(alle_trajecten_holland, G_holland, 7)
# print greedy constructive trajecten and score for holland
# print(greedy_constructive_holland.kies_trajecten())

# create instance of Greedy Iterative for holland
#greedy_iterative_holland = Greedy_Iterative(G_holland, stations_holland, connecties_holland, 7, 120)
#greddu = greedy_iterative_holland.kies_trajecten()
# print greedy iterative trajecten en score holland
#print(greedy_iterative_holland.kies_trajecten())
# print(connecties_holland)
