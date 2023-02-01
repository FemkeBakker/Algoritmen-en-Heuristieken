# import libraries
import random
import numpy as np

# import classes
from Score import *
from .HillClimber import HillClimber

# Maak Simulated Annealing class met HillClimber als parent
class SimAnnealing(HillClimber):
    def __init__(self, beginstate, trajecten, G, temperatuur=1):
        
        # Gebruik init van HillClimber
        super().__init__(beginstate, trajecten, G)
        self.name = "SimAnnealing"
        self.t0 = temperatuur
        self.t = temperatuur

    # Simulated Annealing algoritme 
    def run(self, iteraties):

        for i in range(iteraties):
            # Select random traject uit de state en een random traject uit alle mogelijke trajecten
            old_traject = random.choice(self.state)
            new_traject = random.choice(self.trajecten)

            # Zorg dat er geen dubbele trajecten bij zitten
            if new_traject not in self.state:

                # Maak een nieuwe staat met nieuwe traject ipv oude
                new_state = self.create_new_state(old_traject, new_traject)

                # Bereken nieuwe score
                new_score = calculate_score(self.graaf, new_state)
                
                # Bereken 'kans' voor aannemen nieuwe state
                delta =  self.score_state - new_score
                kans = np.exp(-delta / self.t)
            
                # Accepteer nieuwe state als 'kans' lager is dan een random getal tussen 0 en 1
                if random.random() < kans:
                    self.state = new_state
                    self.score_state = new_score

                # Update temperatuur (lineair)
                self.t = self.t - (self.t0 / iteraties)


