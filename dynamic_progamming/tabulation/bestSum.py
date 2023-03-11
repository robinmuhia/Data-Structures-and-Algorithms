def bestSum(x,y):
    arr = [None for _ in range(x+1)]
    arr[0] = []
    for i in range(x+1):
        if arr[i] != None:
            for j in y:
                if i + j <= x:
                    if arr[i+j] == None:
                        b = arr[i].copy()
                        b.append(j)
                        arr[i+j] = b
                    else:
                        b = arr[i].copy()
                        b.append(j)
                        if len(b) < len(arr[i+j]):
                            arr[i+j] = b
                    
    return arr[-1]



print(bestSum(100,[1,2,3,4,5,25]))
