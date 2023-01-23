import random
import numpy as np

from Score import *
from .HillClimber import HillClimber
 
"""
The Simulated Annealing class that changes a random node in the graph to a random valid value.
Each improvement or equivalent solution is kept for the next iteration.
Also sometimes accepts solutions that are worse, depending on the current temperature.
Most of the functions are similar to those of the HillClimber class, which is why
we use that as a parent class.
"""

# maak Simulated Annealing class met HillClimber als parent
class SimAnnealing(HillClimber):

    def __init__(self, beginstate, trajecten, G, temperatuur=1):
        # gebruik init van HillClimber
        super().__init__(beginstate, trajecten, G)

        self.t0 = temperatuur
        self.t = temperatuur

    # Simulated Annealing algoritme 
    def Simulate_Annealing(self, iteraties):

        for i in range(iteraties):
            # select random traject from state and random traject from all possible trajecten
            old_traject = random.choice(self.state)
            new_traject = random.choice(self.trajecten)

            # do not allow duplicates in solution
            if new_traject not in self.state:

                # maak een nieuwe staat met nieuwe traject ipv oude
                new_state = self.create_new_state(old_traject, new_traject)

                # bereken nieuwe score
                new_score = calculate_score(self.graaf, new_state)
                
                # kansberekening voor simulatie
                delta =  self.score_state - new_score
                kans = np.exp(-delta / self.t)
            
                # accepteer nieuwe als 'dartpijl' lager is dan 
                if random.random() < kans:
                    self.state = new_state
                    self.score_state = new_score

                # update temp
                self.t = self.t - (self.t0 / iteraties)
                # print('temperatuur:', self.t) # check



