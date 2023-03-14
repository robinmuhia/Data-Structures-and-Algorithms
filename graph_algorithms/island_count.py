def explore(grid,row,col,visited):
    row_inbounds = 0 <= row and row < len(grid)
    col_inbounds = 0 <= col and col < len(grid[0])
    if row_inbounds == False or col_inbounds == False:
        return False
    
    if grid[row][col] == 'W':
        return False
    
    pos = (row,col)
    if pos in visited:
        return False
    visited.add(pos)
    
    explore(grid,row-1,col,visited)
    explore(grid,row+1,col,visited)
    explore(grid,row,col-1,visited)
    explore(grid,row,col+1,visited)
    
    return True
    


def island_count(grid):
    visited = set()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if explore(grid,i,j,visited) == True:
                count += 1
                
    return count


