def explore_size(graph,node,visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        print(visited,size)
        size += explore_size(graph,neighbor,visited)
        
    return size

def largest_component(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = explore_size(graph,node,visited)
        if size > longest:
            longest = size       
    
    return longest
    
    
