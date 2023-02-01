# functie neemt een path uit een graaf en returnt een lijst met tuples met de connecties uit de path.
def from_paths_to_connections(path):
    connections = []
    for i in range(len(path)):
        if i == len(path) - 1:
            break
        connection = (path[i], path[i+1])
        connections.append(connection)

    return connections

# functie neemt een lijst met tuples met connecties en returnt een lijst van de path
def from_connections_to_paths(connections):
    path = [connection[0] for connection in connections]

    # voeg laatste station toe
    path.append(connections[-1][1])
    return path

