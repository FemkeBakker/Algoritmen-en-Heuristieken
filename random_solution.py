import networkx as nx
import random


def generate_all_trajecten(G, time):
    all_paths = list()
    for station1 in G.stations:
        for station2 in G.stations:
            paths = list(nx.all_simple_paths(G.graaf, station1, station2))
            for path in paths:
                if nx.path_weight(G.graaf, path, weight = "weight") <= time:
                    all_paths.append(path)
    return (all_paths)

def random_solution(trajecten, aantal_trajecten):
    solution = random.sample(trajecten, k = aantal_trajecten)
    return(solution)

