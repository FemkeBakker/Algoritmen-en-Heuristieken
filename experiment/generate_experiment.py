from algorithms.HillClimber import HillClimber
from random_solution import *
from Score import *
import pandas as pd

import os


class generate_experiment():
    def __init__(self, algorithm, iteraties, experiment_count, trajecten, aantal_trajecten, G, beginstate='random'):
        self.algorithm = algorithm
        self.iteraties = iteraties
        self.experiment_count = experiment_count
        self.trajecten = trajecten
        self.aantal_trajecten = aantal_trajecten
        self.graaf = G
        self.beginstate = beginstate

    def generate_beginstate(self):
        """
        Functie die de beginstate genereert. De default hiervoor is een random beginstate, tenzij er een voorarf vastegestelde beginstate meegegeven is. 
        """
        if self.beginstate == "random":
            beginstate = random_solution(self.trajecten, self.aantal_trajecten)

        else: 
            beginstate = list(self.beginstate.values())[0]
            print(beginstate)

        return beginstate

    def calculate_score(self, beginstate, iteratie):
        """
        Functie berekent de score van de beginstate en de score van de uiteindelijk oplossing. 
        """
        # algorithm_ = self.algorithm(beginstate, self.trajecten, self.graaf)
        self.algorithm_object = self.algorithm(beginstate, self.trajecten, self.graaf)
        # begin_score = algorithm_.score_state
        begin_score = self.algorithm_object.score_state

        # algorithm_.run(iteratie)
        self.algorithm_object.run(iteratie)

        # eind_score = algorithm_.score_state
        eind_score = self.algorithm_object.score_state

        return begin_score, eind_score 

    def test_iteraties(self, iteratie):
        """
        Functie berekent scores voor de meegegeven aantal interaties en worden opgeslagen in DataFrame.
        """

        scores = []

        for i in range(self.experiment_count):
                beginstate = self.generate_beginstate()

                scores.append(self.calculate_score(beginstate, iteratie))

        data = pd.DataFrame(scores, columns=['begin_score', 'eind_score'])
        return data


    def save_csv(self, data, iteratie):
        """
        Functie zet DataFrame in csv file.
        """
        # maak map aan als deze nog niet bestaat.
        if self.beginstate != "random":
            beginstate = list(self.beginstate.keys())[0]
        else:
            beginstate = self.beginstate

        path = "experiment/{}-{}".format(self.algorithm_object.name, beginstate)
        if not os.path.exists(path):
            os.makedirs(path)

        # sla dataframe op in csv
        file = "{}/iteratie{}.csv".format(path, iteratie)
        data.to_csv(file, index=False)
        

    def run_experiment(self):
        """
        Functie geneert de scores voor de verschillende iteraties.
        """
        for iteratie in self.iteraties:
            data = self.test_iteraties(iteratie)
            self.save_csv(data, iteratie)



            

