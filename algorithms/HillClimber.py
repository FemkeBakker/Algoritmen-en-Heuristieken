from Score import *
import random
import copy

""" Pseudo code Hill Climber (Random exchange select)"""
# selecteer beginstate -> beginstate opties: random, 7 langste trajecten, 6 langste trajecten met de 6 endconnecties + 1 langste, uitkomst Greedy
# bereken score
# for i iteraties:
# selecteer random traject uit beginstate
# selecteer traject uit alle trajecten
# check of nieuw traject niet al geselecteerd is in state
# bereken score
# if nieuwe score > oude score -> accepteer nieuw traject, verwijder oud traject

class HillClimber:
    """
    Het Hill Climber algorithme neemt een oplossing als beginstate. 
    Vervolgens worden er steeds kleine aanpassingen gedaan, als de aanpassing ervoor zorgt dat de score verbeterd wordt wordt de aanpassing geaccepteerd.
    De kleine aanpassingen die gedaan worden: een random traject uit de beginstate wordt vervangen met een random traject uit alle mogelijke trajecten.  
    """
    def __init__(self, beginstate, trajecten, G):
        self.name = "HillClimber" # De naam van het algoritme. Attribuut is nodig voor het runnen van generate_experiment.
        self.state = copy.deepcopy(beginstate) # De huidige state van de oplossing. Veranderd gedurende het runnen van het algoritme.
        self.trajecten = trajecten # Alle mogelijke trajecten.
        self.graaf = copy.deepcopy(G) # Een directed graaf met daarin de stations als nodes en de connecties als edges.
        self.score_state = calculate_score(self.graaf, self.state) # De huidige score van de state. Veranderd gedurende het runnen van het algoritme. 

    def select_traject(self, state, trajecten):
        """
        Selecteert traject uit de huidige state en een traject uit alle mogelijke trajecten.
        """

        old_traject = random.choice(state)
        new_traject = random.choice(trajecten)
        return old_traject, new_traject

    def create_new_state(self, old_traject, new_traject):

        """
        Creërt een nieuwe state, waarin het oude traject wordt verwijderd en wordt vervangen met het nieuwe traject.
        """
        
        new_state = copy.deepcopy(self.state)

        # Verwijder oude traject
        new_state.remove(old_traject)

        # Voeg nieuw traject toe
        new_state.append(new_traject)

        return new_state

    def compare_states(self, new_state):
        """
        Checkt of de potientiele nieuwe state beter is. De huidige state wordt veranderd als het een verbetering is.
        """
        new_score = calculate_score(self.graaf, new_state)
        if new_score > self.score_state:
            self.state = new_state
            self.score_state = new_score

    def run(self, iteraties):

        """
        Hill Climber algorithme. Het algoritme onthoud de beste score en runt voor x iteraties.
        """

        for i in range(iteraties):
            # Selecteer random traject uit de huidige staat en random traject uit alle mogelijke trajecten.
            old_traject, new_traject = self.select_traject(self.state, self.trajecten)

            # Sta geen dubbele trajecten toe in oplossing.
            if new_traject not in self.state:

                # Verwijder het oude traject en voeg het nieuwe traject toe.
                new_state = self.create_new_state(old_traject, new_traject)

                # Vervang de huidige state met de nieuwe state als de score beter is, anders wordt de huidige state behouden.
                self.compare_states(new_state)
                




        




            





