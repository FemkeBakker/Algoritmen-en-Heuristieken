from algorithms.HillClimber import HillClimber
from random_solution import *
from Score import *
import pandas as pd

import os
import time


class generate_experiment():
    def __init__(self, algorithm, iteraties, experiment_count, trajecten, aantal_trajecten, deel, G, beginstate='random'):
        self.algorithm = algorithm # De class van het algoritme dat gerund moet worden. 
        self.iteraties = iteraties # Lijst met de iteraties die getest worden.
        self.experiment_count = experiment_count # Aantal keer een iteratie getest wordt.
        self.trajecten = trajecten # Alle mogelijke trajecten.
        self.aantal_trajecten = aantal_trajecten # Aantal trajecten in de oplossing.
        self.graaf = G # Graaf met alle stations en connecties.
        self.beginstate = beginstate # Standaard is random. Andere beginstates -> is een dict met de naam van de beginstate als key en de trajecten als value. Ex: {"Greedy":state}
        self.deel = deel # String met de naam van het deel, is of "Holland" of "Nederland".

    def generate_beginstate(self):
        """
        Functie die de beginstate genereert. De default hiervoor is een random beginstate, tenzij er een voorarf vastegestelde beginstate meegegeven is. 
        """
        if self.beginstate == "random":
            beginstate = random_solution(self.trajecten, self.aantal_trajecten)

        else: 
            beginstate = list(self.beginstate.values())[0]
        return beginstate

    def calculate_score(self, beginstate, iteratie):
        """
        Functie berekent de score van de beginstate en de score van de uiteindelijk oplossing. 
        """
        # Maak een instance aan van de class van het algoritme
        self.algorithm_object = self.algorithm(beginstate, self.trajecten, self.graaf)

        # Bereken begins score
        begin_score = self.algorithm_object.score_state

        # Run het algoritme. Zorg ervoor dat de functie hiervoor in de gebruikte class de naam run heeft. 
        self.algorithm_object.run(iteratie)

        # Bereken nieuwe score
        eind_score = self.algorithm_object.score_state

        return begin_score, eind_score 

    def single_runtime(self, beginstate, iteratie):
        """
        Berekent runtime van 1 keer runnen van het algoritme. Returnt ook de berekende scores.
        """
        start_time = time.time()
        begin_score, eind_score = self.calculate_score(beginstate, iteratie)
        end_time = time.time()-start_time

        return end_time, begin_score, eind_score

    def test_iteraties(self, iteratie):
        """
        Functie berekent scores voor de meegegeven aantal interaties en worden opgeslagen in DataFrame.
        """

        scores = []

        # get runtime of total testing of the iteration
        start_time_tot = time.time()

        for i in range(self.experiment_count):
            beginstate = self.generate_beginstate()

            # get runtime of running algorithm one time
            if i == 0:
                single_runtime, begin_score, eind_score = self.single_runtime(beginstate, iteratie)
                scores.append((begin_score, eind_score))

            else:
                scores.append(self.calculate_score(beginstate, iteratie))

        # calculate runtime of total testing of the iteration
        end_time_tot = time.time()-start_time_tot
            
        data = pd.DataFrame(scores, columns=['begin_score', 'eind_score'])

        return data, single_runtime, end_time_tot

    def create_directory(self):
        # maak map aan als deze nog niet bestaat.
        if self.beginstate != "random":
            beginstate = list(self.beginstate.keys())[0]
        else:
            beginstate = self.beginstate

        path = "experiment/{}-{}-{}".format(self.algorithm_object.name, beginstate, self.deel)
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

    def get_info_data(self, iteratie, data, single_runtime, tot_runtime):
        # create list with iteratie, mean, max and min of the iteration

        info_data_list = []
        info_data_list.append(iteratie)
        info_data_list.append(data["eind_score"].mean())
        info_data_list.append(data['eind_score'].max())
        info_data_list.append(data['eind_score'].min())
        info_data_list.append(single_runtime)
        info_data_list.append(tot_runtime)
        return(info_data_list)

    def create_info_data_csv(self):
        # create DataFrame from data about the mean, max and min of all the iterations and save in csv

        info_data = pd.DataFrame(self.info_data_list, columns=["iteratie",'mean', 'max', 'min', 'single_runtime', "tot_runtime"])
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
            data, single_runtime, tot_runtime = self.test_iteraties(iteratie)

            # sla info over het gemiddelde, max en min van iteratie op
            self.info_data_list.append(self.get_info_data(iteratie, data, single_runtime, tot_runtime))

            # sla de eind en beginscores op in een csv
            self.save_csv(data, iteratie)

        # maak dataframe van het gemiddelde, max en min van alle iteraties en sla op in csv
        self.create_info_data_csv()
        



            

