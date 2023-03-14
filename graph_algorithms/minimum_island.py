import math

def explore_size(grid,row,col,visited):
    row_inbounds = 0 <= row and row < len(grid)
    col_inbounds = 0 <= col and col < len(grid[0])
    if row_inbounds == False or col_inbounds == False:
        return 0
    
    if grid[row][col] == 'W':
        return 0
    
    pos = (row,col)
    if pos in visited:
        return 0
    visited.add(pos)
    
    size = 1
    size += explore_size(grid,row-1,col,visited)
    size += explore_size(grid,row+1,col,visited)
    size += explore_size(grid,row,col-1,visited)
    size += explore_size(grid,row,col+1,visited)
    
    return size
    



def minimum_island(grid):
    visited = set()
    count = math.inf
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            size = explore_size(grid,i,j,visited)
            if size < count and size > 0:
                count = size
    
    return count         
    
    
    
