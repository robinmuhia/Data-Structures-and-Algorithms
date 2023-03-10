def howSum(x,y):
    arr = [None for _ in range(x+1)]
    arr[0] = []
    for i in range(x+1):
        if arr[i] != None:
            for j in y:
                if i + j <= x:
                    b = arr[i].copy()
                    b.append(j)
                    arr[i+j] = b
                    
    return arr[-1]





