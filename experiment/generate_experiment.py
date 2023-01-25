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

    def create_directory(self):
        # maak map aan als deze nog niet bestaat.
        if self.beginstate != "random":
            beginstate = list(self.beginstate.keys())[0]
        else:
            beginstate = self.beginstate

        path = "experiment/{}-{}".format(self.algorithm_object.name, beginstate)
        if not os.path.exists(path):
            os.makedirs(path)
        return(path)

    def save_csv(self, data, iteratie):
        """
        Functie zet DataFrame in csv file.
        """
        path = self.create_directory()

        # sla dataframe op in csv
        file = "{}/iteratie{}.csv".format(path, iteratie)
        data.to_csv(file, index=False)

    def get_info_data(self, iteratie, data):
        # create list with iteratie, mean, max and min of the iteration

        info_data_list = []
        info_data_list.append(iteratie)
        info_data_list.append(data["eind_score"].mean())
        info_data_list.append(data['eind_score'].max())
        info_data_list.append(data['eind_score'].min())
        return(info_data_list)

    def create_info_data_csv(self):
        # create DataFrame from data about the mean, max and min of all the iterations and save in csv

        info_data = pd.DataFrame(self.info_data_list, columns=["iteratie",'mean', 'max', 'min'])
        path = self.create_directory()
        file = "{}/info_data.csv".format(path, index=False)
        info_data.to_csv(file, index = False)

    def run_experiment(self):
        """
        Functie geneert de scores voor de verschillende iteraties.
        """
        self.info_data_list = []

        for iteratie in self.iteraties:
            # calculate begin en eindscore van de iteratie
            data = self.test_iteraties(iteratie)

            # sla info over het gemiddelde, max en min van iteratie op
            self.info_data_list.append(self.get_info_data(iteratie, data))

            # sla de eind en beginscores op in een csv
            self.save_csv(data, iteratie)

        # maak dataframe van het gemiddelde, max en min van alle iteraties en sla op in csv
        self.create_info_data_csv()
        



            

