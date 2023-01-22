from Score import *
from random_solution import *
from connections_paths import *

# libraries
import pandas as pd
import networkx as nx

# load data Deel 1 - Noord-Holland & Zuid-Holland
ConnectiesHolland = pd.read_csv("Data-deel1/ConnectiesHolland.csv")
StationsHolland = pd.read_csv("Data-deel1/StationsHolland.csv")

# load data deel 2 - Heel NL
ConnectiesNationaal = pd.read_csv("Data-deel2/ConnectiesNationaal.csv")
StationsNationaal = pd.read_csv("Data-deel2/StationsNationaal.csv")

# create Graph instances
G_holland = Graph(ConnectiesHolland, StationsHolland)
G_nederland = Graph(ConnectiesNationaal, StationsNationaal)

""" PSEUDO-CODE VOOR 'GREEDY' ALGORITME """
# alle trajecten af gaan
# selecteer alle trajecten met de grootst voorkomende lengte
# als het er één is, selecteer je die
# als het er meer zijn, kijk je naar de eerst volgende belangrijkste constraint (na het aantal verbindingen, p, komt het aantal minuten: Min. Want door steeds de langste trajecten te nemen minimaliseer je ook al een beetje het aantal trajecten. Als je kijkt per verbinding en je filtert de lange trajecten er uit, blijven er korte over met de missende verbindingen die niet in de lange trajecten zitten?)
# bereken Min voor de trajecten, kies het traject met kleinste Min
# Verwijder het gekozen traject uit de lijst met alle trajecten
# ontleed het traject in verbindingen en verwijder de trajecten met dezelfde verbindingen
# herhaal het proces tot max trajecten (7 of 20) of tot alle verbindingen al inbegrepen zijn en er geen trajecten meer te kiezen zijn
# -----

# neem lijst met alle trajecten. Langer traject is 'beter' dus order van lang naar kort.
# pak de langste/bovenstaande traject. voeg toe aan lijst van gekozen trajecten, deze neemt namelijk de meeste verbindingen mee in één traject.
# ontleed dit gekozen traject in verbindingen, sla deze op in een lijst van lijstjes aan verbindingen
# verwijder het gekozen traject uit de 'queue' met trajecten die nog bekeken moeten worden
# kijk naar de queue en pak weer het (nu) langste/bovenstaande traject
# ontleed dit traject en check of er overeenkomende verbindingen zijn met de eerste/langste traject
# als dit zo is, verwijder je het traject uit de queue en ga je verder
# als dit niet zo is voeg je het traject aan de lijst met gekozen trajecten, en ontleed

""" Versie waarbij meerdere langste lijsten worden gefilterd op laagste Min """
# class Greedy:
#     def __init__(self, alle_trajecten, G, max_trajecten):
#         self.trajecten = alle_trajecten
#         self.G = G
#         self.max_trajecten = max_trajecten

#     def calculate_Min(self, path):
#         Min = nx.path_weight(self.G.graaf, path, weight = "weight")
#         return Min

#     def kies_trajecten(self):
#         queue = self.trajecten
#         gekozen_trajecten = []
#         verbindingen_totaal = []

#         while queue:
#             langste_traject = max(queue, key=len)
#             verbindingen = [(langste_traject[i], langste_traject[i+1]) for i in range(0,len(langste_traject), 2)]
#             overlap = False
#             for verbinding in verbindingen:
#                 if verbinding in verbindingen_totaal or (verbinding[1], verbinding[0]) in verbindingen_totaal:
#                     overlap = True
#                     break
#             if overlap:
#                 queue.remove(langste_traject)
#             else:
#                 gekozen_trajecten.append(langste_traject)
#                 verbindingen_totaal.extend(verbindingen)
#                 queue.remove(langste_traject)
        
#         return gekozen_trajecten 

""" Versie waarbij meerdere langste lijsten en Min niet worden meegenomen """
class Greedy:
    def __init__(self, alle_trajecten, G, max_trajecten):
        self.trajecten = alle_trajecten
        self.G = G
        self.max_trajecten = max_trajecten

    def kies_trajecten(self):
        queue = self.trajecten
        gekozen_trajecten = []
        verbindingen_totaal = []

        while len(gekozen_trajecten) < self.max_trajecten:
            langste_traject = max(queue, key=len)
            verbindingen = from_paths_to_connections(langste_traject)
            overlap = False
            for verbinding in verbindingen:
                if verbinding in verbindingen_totaal or (verbinding[1], verbinding[0]) in verbindingen_totaal:
                    overlap = True
                    break
            if overlap:
                queue.remove(langste_traject)
            else:
                gekozen_trajecten.append(langste_traject)
                verbindingen_totaal.extend(verbindingen)
                queue.remove(langste_traject)
        
        score = calculate_score(self.G, gekozen_trajecten)
        
        return gekozen_trajecten, score 


# -------------------------------------------------------------------------------------------------------------------------
# V2
# class Greedy:
#     def __init__(self, alle_trajecten, G, max_trajecten):
#         self.trajecten = alle_trajecten
#         self.G = G
#         self.max_trajecten = max_trajecten

#     def kies_trajecten(self):
#         trajecten_copy = self.trajecten
#         temp_trajecten_met_min = dict()
#         temp_trajecten = []
#         gekozen_trajecten = []

        # while len(gekozen_trajecten) < self.max_trajecten or len(trajecten_copy) > 0:
        #     for traject in trajecten_copy:
        #         if len(traject) == max(trajecten_copy, key=len):
        #             temp_trajecten.append(traject)
        #             Min = nx.path_weight(self.G.graaf, traject, weight = "weight")
        #             temp_trajecten_met_min[traject] = Min
        #             # print(temp_trajecten_met_min)
        #     if len(temp_trajecten_met_min) > 1:
        #         best_traject = min(temp_trajecten_met_min, key=temp_trajecten_met_min.get)
        #     elif len(temp_trajecten_met_min) == 0:
        #         continue
        #     else:
        #         best_traject = list(temp_trajecten_met_min.keys())[0]
            
        #     temp_trajecten_met_min = dict()
        #     gekozen_trajecten.append(best_traject)
        #     trajecten_copy = [i for i in trajecten_copy if i not in temp_trajecten]

        # return gekozen_trajecten 


# -------------------------------------------------------------------------------------------------------------------------
# V1
# class Greedy:
#     def __init__(self, alle_trajecten, G):
#         self.trajecten = alle_trajecten
#         self.graaf = G


#     # def calculate_Min(self, G, traject):
#     #     Min = nx.path_weight(G.graaf, traject, weight = "weight")
#     #     return Min

#     def kies_trajecten(self, trajecten):
#         trajecten_copy = trajecten
#         temp_trajecten = dict()
#         gekozen_trajecten = []

#         for traject in trajecten_copy:
#             if len(traject) == max(trajecten_copy, key=len):
#                 Min = self.calculate_Min(G, traject)
#                 temp_trajecten['traject'] = Min
#                 print(temp_trajecten)
#         if len(temp_trajecten) > 1:
#             best_traject = max(temp_trajecten, key=stats.get)
#         else:
#             best_traject = list(temp_trajecten.keys())[0]
            
#         gekozen_trajecten.append(best_traject)




#         return gekozen_trajecten

# -------------------------------------------------------------------------------------------------------------------------
# print(alle_trajecten_holland, alle_trajecten_nl, len(alle_trajecten_holland), len(alle_trajecten_nl))
# print(len(alle_trajecten_holland), len(alle_trajecten_nl))
# max_len = 0
# c = 0
# for traject in alle_trajecten_holland:
#     # print(len(traject))
#     if len(traject) > max_len:
#         max_len = len(traject)
#         c = 0
#     elif len(traject) == max_len:
#         c += 1
#     if len(traject) == 11:
#         print(traject)
# print(max_len, c)