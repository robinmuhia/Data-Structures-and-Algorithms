def grid_traveler(x:int,y:int,memo={}):
    key = (x,y)
    if key in memo:
        return memo[key]
    elif x == 0 or y == 0:
        return 0
    elif x == 1 and y == 1:
        return 1
    else:
        memo[key] = grid_traveler(x-1,y,memo) + grid_traveler(x,y-1,memo)
    return memo[key]


print(grid_traveler(2,3))
    
    
    


