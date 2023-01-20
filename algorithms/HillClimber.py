from Score import *
import random
import copy

""" Pseudo code Hill Climber (Random exchange select)"""
# selecteer beginstate -> beginstate opties: random, 7 langste trajecten, 6 langste trajecten met de 6 endconnecties + 1 langste, uitkomst Greedy
# bereken score
# for i iteraties:
# selecteer random traject uit beginstate
# while (nog geen nieuw traject gevonden)
# selecteer traject uit alle trajecten
# if traject overlap met al geselecteerde trajecten -> opnieuw selecteren
# bereken score
# if nieuwe score > oude score -> accepteer nieuw traject, verwijder oud traject, break out loop

class HillClimber:
    def __init__(self, beginstate, trajecten, G):
        self.state = copy.deepcopy(beginstate)
        self.trajecten = trajecten
        self.graaf = copy.deepcopy(G)
        self.score_state = calculate_score(self.graaf, self.state)

    def create_new_state(self, old_traject, new_traject):

        """
        Creates a new state, in which the old traject has been removed and the new traject has been added.
        """
        
        new_state = copy.deepcopy(self.state)
        new_state.remove(old_traject)
        new_state.append(new_traject)
        return new_state

    def climbing_hill(self, iteraties):

        """
        Climbing Hill algorithm. Keeps the best presented score, will run for x iterations.
        """

        for i in range(iteraties):
            # select random traject from state and random traject from all possible trajecten
            old_traject = random.choice(self.state)
            new_traject = random.choice(self.trajecten)

            # do not allow duplicates in solution
            if new_traject not in self.state:

                # remove old traject and add new traject to state
                new_state = self.create_new_state(old_traject, new_traject)

                # keep the new state if the score is better, else keep old state
                new_score = calculate_score(self.graaf, new_state)
                if new_score > self.score_state:
                    self.state = new_state
                    self.score_state = new_score




        




            





