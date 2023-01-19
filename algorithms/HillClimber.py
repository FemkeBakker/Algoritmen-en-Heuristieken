""" Pseudo code Hill Climber (Random exchange select)"""
# selecteer beginstate -> beginstate opties: random, 7 langste trajecten, 6 langste trajecten met de 6 endconnecties + 1 langste, uitkomst Greedy
# for i iteraties:
# bereken score
# selecteer traject uit beginstate die het minst unique is -> de meeste overlap heeft met andere trajecten
# while (nog geen nieuw traject gevonden)
# selecteer traject uit alle trajecten
# if traject overlap met al geselecteerde trajecten -> opnieuw selecteren
# bereken score
# if nieuwe score > oude score -> accepteer nieuw traject, verwijder oud traject, break out loop

""" Pseudo code Hill Climber (Optimal exchange select)"""
# selecteer beginstate -> beginstate opties: random, 7 langste trajecten, 6 langste trajecten met de 6 endconnecties + 1 langste, uitkomst Greedy
# for i iteraties
# bereken score
# selecteer traject uit beginstate die het minst unique is -> de meeste overlap heeft met andere trajecten
# while (nog geen nieuw traject gevonden)
# selecteer traject die meest connecties bevat die nog niet in de oplossing zitten
# if traject overlap met al geselecteerde trajecten -> opnieuw selecteren
# bereken score
# if nieuwe score > oude score -> accepteer nieuw traject, verwijder oud traject, break out loop
# if nieuwe score <= oude score -> remove traject from copy, find new traject from copy


