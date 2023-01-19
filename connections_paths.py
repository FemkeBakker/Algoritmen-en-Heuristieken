# function takes a path and returns a list of tuples with the connections in the path, in order
def from_paths_to_connections(path):
    connections = []
    for i in range(len(path)):
        if i == len(path) - 1:
            break
        connection = (path[i], path[i+1])
        connections.append(connection)

    return connections

# function takes a list of tuples with connections, return a list of the path
def from_connections_to_paths(connections):
    path = [connection[0] for connection in connections]

    # add last station
    path.append(connections[-1][1])
    return path