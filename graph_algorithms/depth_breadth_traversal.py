def depth_traversal(graph,source):
    stack = [source]
    
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for i in graph[current]:
            stack.append(i)
            

def breadth_traversal(graph,source):
    queue = [source]
    while len(queue) > 0:
        current =  queue.pop(0)
        print(current)
        for i in graph[current]:
            queue.append(i)       
        
        
        
        
