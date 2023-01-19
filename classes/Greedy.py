
# PSEUDO-CODE VOOR 'GREEDY' ALGORITME

# alle trajecten af gaan
# selecteer alle trajecten met de grootst voorkomende lengte
# als het er één is, selecteer je die
# als het er meer zijn, kijk je naar de eerst volgende belangrijkste constraint (na het aantal verbindingen, p, komt het aantal minuten: Min. Want door steeds de langste trajecten te nemen minimaliseer je ook al een beetje het aantal trajecten)
# bereken Min voor de trajecten, kies het traject met kleinste Min
# Verwijder het gekozen traject uit de lijst met alle trajecten
# ontleed het traject in verbindingen en verwijder de trajecten met dezelfde verbindingen
# herhaal het proces tot max trajecten (7 of 20) of tot alle verbindingen al inbegrepen zijn en er geen trajecten meer te kiezen zijn







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