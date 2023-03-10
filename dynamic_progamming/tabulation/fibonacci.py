def fibonacci(n:int):
    value = [0 for _ in range(n+1)]
    value[1] = 1
    for i in range(n+1):
        if i < n-1:
            value[i+1] += value[i]
            value[i+2] += value[i]
        elif i == n-1:
            value[i+1] += value[i]
        else:
            return value[n]
        
        
        


        

