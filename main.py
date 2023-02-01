# CASE: RailNL - Team: RailNL-STF

# libraries
import pandas as pd
import networkx as nx
import folium
import random
import numpy as np

# import class functions from the class files
from classes.station import Station
from classes.Graph import Graph
from Visualisatie.plot import *
from random_solution import *
from Score import *
from algorithms.HillClimber import HillClimber
from algorithms.Greedy_Constructive import *
from algorithms.Greedy_Iterative import Greedy_Iterative
from algorithms.SimAnnealing import SimAnnealing
from experiment.generate_experiment import *

# ------- Haal data op ------ #
# Laad data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# Laad data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# creër Graph instances
G_holland = Graph(ConnectiesHolland, StationsHolland)
G_nederland = Graph(ConnectiesNationaal, StationsNationaal)

# genereer alle mogelijke simple paths in graaf
alle_trajecten_holland = generate_all_trajecten(G_holland, 120)
alle_trajecten_nl = generate_all_trajecten(G_nederland, 180)

# ----- Random Baseline ------- #

# Uitkomsten worden opgeslagen in experiment/Random_baseline. Code is uitgecomment, zodat het maar 1 keer gerunt wordt.
# De baseline wordt 150 keer getest. 
""" Random Baseline Holland """
# random_to_csv(alle_trajecten_holland, 7, G_holland, "Holland", 150)

""" Random Baseline Nederland """
# random_to_csv(alle_trajecten_nl, 7, G_nederland, "Nederland", 150)


<<<<<<< Updated upstream
=======
# example input for plot visualization
trajecten = [["Beverwijk", "Castricum", "Alkmaar", "Hoorn", "Zaandam"], 
["Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Amsterdam Zuid", "Schiphol Airport"], 
["Rotterdam Alexander", "Gouda", "Alphen a/d Rijn", "Leiden Centraal"," Schiphol Airport", "Amsterdam Zuid"]]

# creates plot of trajecten, return None, map can be found in Visualisatie/map.html
#create_plot(trajecten, StationsHolland, "Holland") 
#create_plot(trajecten, StationsNationaal, "NL")

# generate all possible simple paths in graph
alle_trajecten_holland = generate_all_trajecten(G_holland, 120)
alle_trajecten_nl = generate_all_trajecten(G_nederland, 180)

# get random solution, chosen from all possible simple paths in graph
random_sol_holland = random_solution(alle_trajecten_holland, 7)
random_sol_nl = random_solution(alle_trajecten_nl, 20)


#create_plot(random_sol_holland, StationsHolland, "Random_sol_Holland") 


# calculate and print scores from random/baseline algorithm for both holland and NL datasets
random_score_holland = calculate_score(G_holland, random_sol_holland)
random_score_nl = calculate_score(G_nederland, random_sol_nl)

>>>>>>> Stashed changes
# --------- Greedy Constructive algoritme ----------- #
# create instance of Greedy Constructive Holland
# greedy_contructief_holland = Greedy_Constructive(alle_trajecten_holland, G_holland, 7)
# greedy_con_holland_solution, greedy_con_holland_solution_score = greedy_contructief_holland.kies_trajecten()
# greedy_to_csv(greedy_con_holland_solution_score, greedy_con_holland_solution, "Holland")

# create instance of Greedy Constructive NL
# greedy_contructief_nl = Greedy_Constructive(alle_trajecten_nl, G_nederland, 20)
# greedy_con_nl_solution, greedy_con_nl_solution_score = greedy_contructief_nl.kies_trajecten()
# greedy_to_csv(greedy_con_nl_solution_score, greedy_con_nl_solution, "Nederland")


# --------- Greedy Iterative algoritme ----------- #
# save stations and connections from holland dataframes in lists
stations_holland = list(StationsHolland['station'])
connecties_holland = [(station1, station2) for station1, station2 in zip(ConnectiesHolland['station1'], ConnectiesHolland['station2'])]

# Bereken Greedy iterative score in Holland
greedy_iterative_holland = Greedy_Iterative(G_holland, stations_holland, connecties_holland, 7, 120)
greedy_iterative_holland_solution = greedy_iterative_holland.kies_trajecten()
# greedy_iterative_holland_score = calculate_score(G_holland, greedy_iterative_holland_solution)

# save stations and connections from national dataframes in lists
stations_nationaal = list(StationsNationaal['station'])
connecties_nationaal = [(station1, station2) for station1, station2 in zip(ConnectiesNationaal['station1'], ConnectiesNationaal['station2'])]

# Bereken Greedy iterative score in Nederland
greedy_iterative_nl = Greedy_Iterative(G_nederland, stations_nationaal, connecties_nationaal, 20, 180)
greedy_iterative_nl_solution = greedy_iterative_nl.kies_trajecten()
# greedy_iterative_nl_score = calculate_score(G_holland, greedy_iterative_nl_solution)

# ----------- Experiment Hill-Climber -------------------#

iteraties = [200, 500, 1000, 2000, 5000, 8000, 10000, 12000, 14000, 15000]
experiment_count = 150
holland_aantal_trajecten = 7
nl_aantal_trajecten = 20

# 7 langste trajecten in Holland
copy_alle_trajecten_holland = alle_trajecten_holland.copy()
langste_trajecten_holland = sorted(copy_alle_trajecten_holland, key = len, reverse=True)[0:holland_aantal_trajecten]

# 20 langste trajecten in NL
copy_alle_trajecten_nl = alle_trajecten_nl.copy()
langste_trajecten_nl = sorted(copy_alle_trajecten_nl, key = len, reverse=True)[0:nl_aantal_trajecten]

"Greedy constructive Holland"
# greedy_contructief_holland = Greedy_Constructive(alle_trajecten_holland, G_holland, 7)
# greedy_con_holland_solution, greedy_con_holland_solution_score = greedy_contructief_holland.kies_trajecten()

"Greedy constructive Nederland"
# greedy_contructief_nl = Greedy_Constructive(alle_trajecten_nl, G_nederland, nl_aantal_trajecten)
# greedy_con_nl_solution, greedy_con_nl_solution_score = greedy_contructief_nl.kies_trajecten()

"Random beginstate - Holland"
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_holland, holland_aantal_trajecten, "Holland", G_holland)
# experiment.run_experiment()

"Random beginstate - Nederland"
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_nl, nl_aantal_trajecten, "Nederland", G_nederland)
# experiment.run_experiment()

"7 langste trajecten beginstate - Holland"
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_holland, holland_aantal_trajecten, "Holland", G_holland, {"7langste":langste_trajecten_holland})
# experiment.run_experiment()

"7 langste trajecten beginstate - Nederland"
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_nl, nl_aantal_trajecten, "Nederland", G_nederland, {"7langste":langste_trajecten_nl})
# experiment.run_experiment()

"Constructieve Greedy beginste - Holland"
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_holland, holland_aantal_trajecten, "Holland", G_holland, {"Greedy_con":greedy_con_holland_solution})
# experiment.run_experiment()

"Constructieve Greedy beginste - Nederland"
# experiment = generate_experiment(HillClimber, iteraties, experiment_count, alle_trajecten_nl, nl_aantal_trajecten, "Nederland", G_nederland, {"Greedy_con":greedy_con_nl_solution})
# experiment.run_experiment()

# ------- Visualisatie Experiment -------- #

# Plot HillClimber met Random als beginstate in Holland
data_Hol = generate_data(iteraties, "experiment\HillClimber-random-Holland\iteratie")
create_boxplot(data_Hol,'Random_Hol_iteraties', 'Iteraties', iteraties, 'HillClimber - Random Holland')

# Plot HillClimber met Random als beginstate in Nederland
data_NL = generate_data(iteraties, "experiment\HillClimber-random-Nederland\iteratie")
create_boxplot(data_Hol,'Random_NL_iteraties', 'Iteraties', iteraties, 'HillClimber - Random Nederland')

# Plot HillClimber met 7langste trajecten als beginstate in Holland
data_Hol = generate_data(iteraties, "experiment\HillClimber-7langste-Holland\iteratie")
create_boxplot(data_Hol,'7langste_Hol_iteraties', 'Iteraties', iteraties, 'HillClimber - 7 langste trajecten Holland')

# Plot HillClimber met 7langste trajecten als beginstate in Nederland
data_NL = generate_data(iteraties, "experiment\HillClimber-7langste-Nederland\iteratie")
create_boxplot(data_NL,'7langste_NL_iteraties', 'Iteraties', iteraties, 'HillClimber - 7 langste trajecten Nederland')

# Plot HillClimber met Greedy Constructive als beginstate in Holland
data_Hol = generate_data(iteraties, "experiment\HillClimber-Greedy_con-Holland\iteratie")
create_boxplot(data_Hol,'Greedy_con_Hol_iteraties', 'Iteraties', iteraties, 'HillClimber - Greedy constructive Holland')

# Plot HillClimber met Greedy Constructive als beginstate in Nederland
data_NL = generate_data(iteraties, "experiment\HillClimber-Greedy_con-Nederland\iteratie")
create_boxplot(data_NL,'Greedy_con_NL_iteraties', 'Iteraties', iteraties, 'HillClimber - Greedy constructive Nederland')

# --------- Vergelijking algoritmes ---------- #

# Plot alle algoritmes met de optimale waardes voor Holland
data, labels = generate_data_vergelijking_holland()
create_boxplot(data,'Vergelijking Holland', 'Algoritmes', labels, 'Vergelijking Holland')

# Plot alle algoritmes met de optimale waardes voor Nederland
data, labels = generate_data_vergelijking_nl()
create_boxplot(data,'Vergelijking Nederland', 'Algoritmes', labels, 'Vergelijking Nederland')


# -------- Visualisatie op kaart van de beste oplossingen -------- #
# Kaart van beste oplossing Hill Climber met beginstate 7 langste in Holland
HC_7 = pd.read_csv("experiment/HillClimber-7langste-Holland/info_data.csv")
best_solution_map(HC_7, StationsHolland, 10000, "Holland", "best_HC_7_Holland")

# Kaart van beste oplossing Hill Climber met beginstate random in Holland
HC_random = pd.read_csv("experiment/HillClimber-random-Holland/info_data.csv")
best_solution_map(HC_random, StationsHolland, 8000, "Holland", "best_HC_random_Holland")

# Kaart van beste oplossing Simulated Annealing met 20000 iteraties en temp=30 in Holland


# Kaart van beste oplossing Hill Climber met beginstate 7 langste in Nederland
HC_7 = pd.read_csv("experiment/HillClimber-7langste-Nederland/info_data.csv")
best_solution_map(HC_7, StationsNationaal, 15000, "Nederland", "best_HC_7_NL")

# Kaart van beste oplossing Hill Climber met beginstate random in Nederland
HC_random = pd.read_csv("experiment/HillClimber-random-Nederland/info_data.csv")
best_solution_map(HC_random, StationsNationaal, 15000, "Nederland", "best_HC_random_NL")

# Kaart van beste oplossing Simulated Annealing met 20000 iteraties en temp=30 in Nederland




# --------------- Simulated Annealing ------------------ #

#iteraties = [200, 500, 1000, 2000, 5000, 10000, 20000]
#experiment = generate_experiment(SimAnnealing, iteraties, 150, alle_trajecten_nl, 20, "Nederland", G_nederland, 'random', temperatuur=5)
#experiment.run_experiment()
#data_SA_temp = generate_data(iteraties, "experiment\SimAnnealing-random-Nederland\iteratie")
#create_boxplot(data_SA_temp,'SA, Nederland', 'Iteraties', iteraties, 'Simulated Annealing')

<<<<<<< Updated upstream
#iteraties = [20000]
# temp = [0.1, 1, 5, 10, 20, 30, 40, 50]
#for i in temp:
#    experiment = generate_experiment(SimAnnealing, iteraties, 150, alle_trajecten_nl, 20, "temptest2", G_nederland, 'random', temperatuur=i)
#    experiment.run_experiment()

# data_SA_temp = generate_data(temp, "experiment\SimAnnealing-random-temptest\iteratie20000+temp")
# create_boxplot(data_SA_temp,'SA_temp2, Nederland', 'Temperatuur', temp, 'Simulated Annealing')
=======
#   "Vergelijking Holland"
#experiment = generate_experiment(SimAnnealing, iteraties, 150, alle_trajecten_nl, 20, "Nederland", G_nederland, 'random', temperatuur=5)
#experiment.run_experiment()
#data_SA_temp = generate_data(iteraties, "experiment\SimAnnealing-random-Nederland\iteratie")
#create_boxplot(data_SA_temp,'SA, Nederland', 'Iteraties', iteraties, 'Simulated Annealing')


iteraties = [5000, 10000, 15000, 20000]
temp = [30]
for i in temp:
    experiment = generate_experiment(SimAnnealing, iteraties, 150, alle_trajecten_holland, 7, "Holland, temp30", G_holland, 'random', temperatuur=30)
    experiment.run_experiment()

data_SA_hol = generate_data(iteraties, "experiment\SimAnnealing-random-temptest\iteratie")
create_boxplot(data_SA_hol,'SA_hol, Holland', 'Iteraties', iteraties, 'Simulated Annealing')
>>>>>>> Stashed changes

#print(pd.read_csv("experiment/SimAnnealing-random/info_data.csv"))

# ------------------------------------------------------- #

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
