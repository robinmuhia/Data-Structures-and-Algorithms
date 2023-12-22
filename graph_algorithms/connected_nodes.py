def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True


def connected_nodes(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count
