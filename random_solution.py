import networkx as nx
import random
import pandas as pd

from Score import *
import os


# function that generates all possible simple paths in graph
def generate_all_trajecten(G, time):
    all_paths = list()
    for station1 in G.stations:
        for station2 in G.stations:
            paths = list(nx.all_simple_paths(G.graaf, station1, station2))
            for path in paths:
                if nx.path_weight(G.graaf, path, weight = "weight") <= time:
                    all_paths.append(path)
    return (all_paths)

# function that selects random trajecten from all given trajecten
def random_solution(trajecten, aantal_trajecten):
    solution = random.sample(trajecten, k = aantal_trajecten)
    return(solution)

# functie runt de random baseline voor een i aantal keer en slaat de resultaten op in csv
def random_to_csv(trajecten, aantal_trajecten, G, deel, experiment_count=150):
    scores = []
    solutions = []
    for i in range(experiment_count):
        solution = random_solution(trajecten, aantal_trajecten)
        solutions.append(solution)
        scores.append(calculate_score(G, solution))

    # creër dataframe met daarin de eind_scores en oplossingen
    data = pd.DataFrame(columns=['eind_score', 'oplossing'])
    data['eind_score'] = scores
    data['oplossing'] = solutions
    
    # creër dataframe met algemene info van de data, zoals het gemiddelde, beste score en de beste oplossing
    info = pd.DataFrame(columns=['mean', "best_score", "best_solution"])
    info['mean'] = [data['eind_score'].mean()]
    best_score = data['eind_score'].max()
    info['best_score'] = [best_score]
    info['best_solution'] = [data.loc[data['eind_score']==best_score]['oplossing'].values[0]]

    # maak map in experiment aan als deze nog niet bestaat
    path = "experiment/Random_baseline"
    if not os.path.exists(path):
            os.makedirs(path)

    # zet de dataframes om in csv files
    data.to_csv("{}/{}.csv".format(path, deel), index=False)
    info.to_csv("{}/{}_info.csv".format(path, deel), index=False)
    
    return None



