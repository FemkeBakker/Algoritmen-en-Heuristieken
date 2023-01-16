# ---- We do not use this Class, kept the code just in case ---- #
# example traject
traject = {"connecties" : ["Beverwijk", "Castricum", "Alkmaar", "Hoorn", "Zaandam"], "min": 100, "all_connections":28}

class Traject():
    def __init__(self, traject, uid):
        self.uid = uid # give id to traject
        self.connecties = traject['connecties']
        self.min = traject['min'] # total minutes of traject
        self.p = len(self.connecties) / traject['all_connections'] # fraction of stations in traject





