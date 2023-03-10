def gridTraveler(x,y):
    if x < 1 or y < 1:
        return 0
    arr = [[0 for i in range(x+1)] for j in range(y+1)]
    arr[1][1]=1
    for i in range(y+1):
        for j in range(x+1):
            if j + 1 <= x :
                arr[i][j+1] += arr[i][j]
            if i + 1 <= y:
                arr[i+1][j] += arr[i][j]
                

    return arr[y][x]


print(sum([]))
