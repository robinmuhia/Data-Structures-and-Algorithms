def buildgraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def shortest_path(edges, nodeA, nodeB):
    graph = buildgraph(edges)
    visited = set()
    visited.add(nodeA)
    queue = [[nodeA, 0]]
    while len(queue) > 0:
        node, distance = queue.pop(0)
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])

    return -1


edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]

print(shortest_path(edges, "w", "z"))
