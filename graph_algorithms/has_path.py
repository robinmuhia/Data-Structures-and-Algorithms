def has_path_directed(graph,src,dst):
    if src == dst:
        return True
    
    for i in graph[src]:
        if has_path_directed(graph,i,dst) == True:
            return True
        
    return False

#The first two formulas are helper functions
def buildgraph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph
        
def has_path(graph,src,dst,visited):
    if src in visited:
        return False
    if src == dst:
        return True
    visited.add(src)
    for neighbor in graph:
        if has_path(graph,neighbor,dst,visited) == True:
            return True
    return False


def has_path_undirected(edges,nodeA,nodeB):
    graph = buildgraph(edges)
    return has_path(graph,nodeA,nodeB,visited = set())
    
    
