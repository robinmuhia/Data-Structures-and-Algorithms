def canSum(x,y):
    arr = [False for _ in range(x+1)]
    arr[0] = True
    for i in range(x+1):
        if arr[i] == True:
            for j in y:
                if i + j <= x :
                    arr[i+j] = True
    
    return arr[-1]
        
    
    
print(canSum(7,[5,4,3,7]))
print(canSum(30000000,[7,14]))

print(None+1)