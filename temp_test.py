
m = 4
n = 4
targetrow = 2
targetcol = 2

grid = [[8, 8, -1, 9], 
        [4, 10, 10, 9], 
        [4, 3, 3, -2],
        [16, 16, 2, 2]]

path = []

print(grid)                 ####

def find_empty_space(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == -1:
                return [i, j]
    return None

def find_object(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == -2:
                return [i, j]
    return None

# Generates valid moves from the current position within the grid boundaries.
def valid_moves(x, y, m, n):
    if 0 <= x < m and 0 <= y < n:  # Check if the new position is within the grid
        # print(0 <= x < m and 0 <= y < n)
        return [x, y]
    else:
        return None

def left(grid, path):
    empty = find_empty_space(grid)
    leftval = valid_moves(empty[0],empty[1] - 1, m, n)
    leftmostval = valid_moves(empty[0],empty[1] - 2, m, n)
    if leftval != None and leftmostval != None:
        if grid[leftval[0]][leftval[1]] == grid[leftmostval[0]][leftmostval[1]]:
            grid[empty[0]][empty[1]] = grid[leftval[0]][leftval[1]]
            grid[leftmostval[0]][leftmostval[1]] = -1
            path += [grid[leftval[0]][leftval[1]]]
        
def down(grid,path):
    empty = find_empty_space(grid)       
    downval  = valid_moves(empty[0] + 1,empty[1], m, n)
    downmostval = valid_moves(empty[0] + 2,empty[1], m, n)
    if downval != None and downmostval != None:
        if grid[downval[0]][downval[1]] == grid[downmostval[0]][downmostval[1]]:
            grid[empty[0]][empty[1]] = grid[downval[0]][downval[1]] 
            grid[downmostval[0]][downmostval[1]] = -1
            path += [grid[downval[0]][downval[1]]]
            
        
def right(grid,path):
    empty = find_empty_space(grid)
    rightval = valid_moves(empty[0],empty[1] + 1, m, n)
    rightmostval = valid_moves(empty[0],empty[1] + 2, m, n)
    if rightval != None and rightmostval != None:
        if grid[rightval[0]][rightval[1]] == grid[rightmostval[0]][rightmostval[1]]:
            grid[empty[0]][empty[1]] = grid[rightval[0]][rightval[1]] 
            grid[rightmostval[0]][rightmostval[1]] = -1
            path += [grid[rightval[0]][rightval[1]]]
            
def up(grid,path):
    empty = find_empty_space(grid)
    upval = valid_moves(empty[0] - 1,empty[1], m, n)
    upmostval = valid_moves(empty[0] - 2,empty[1], m, n)
    if upval != None and upmostval != None:
        if grid[upval[0]][upval[1]] == grid[upmostval[0]][upmostval[1]]:
            grid[empty[0]][empty[1]] = grid[upval[0]][upval[1]] 
            grid[upmostval[0]][upmostval[1]] = -1
            path += [grid[upval[0]][upval[1]]]
            
def space_by_object(grid, target_row, target_col):

    empty = find_empty_space(grid)
    if(grid[empty[0]][empty[1]] == grid[target_row][target_col]):
        return True
    else:
        return False
    # left = valid_moves(empty[0],empty[1] - 1, m, n)
    # down = valid_moves(empty[0] + 1,empty[1], m, n)
    # right = valid_moves(empty[0],empty[1] + 1, m, n)   
    # up = valid_moves(empty[0] - 1,empty[1], m, n)
    
    # if(left):
    #     if(grid[empty[0]][empty[1] - 1] == grid[target_row][target_col]):
    #         # car_object = find_object(grid)
    #         grid[target_row][target_col]= grid[empty[0]][empty[1]]
    #         grid[empty[0]][empty[1]] = grid[target_row][target_col]
    #         return True
            
    # if(right):
    #     if(grid[empty[0]][empty[1] + 1] == grid[target_row][target_col]):
    #         # car_object = find_object(grid)
    #         grid[target_row][target_col]= grid[empty[0]][empty[1]]
    #         grid[empty[0]][empty[1]] = grid[target_row][target_col]
    #         return True
            
    # if(up):
    #     if(grid[empty[0] - 1][empty[1]] == grid[target_row][target_col]):
    #         # car_object = find_object(grid)
    #         grid[target_row][target_col]= grid[empty[0]][empty[1]]
    #         grid[empty[0]][empty[1]] = grid[target_row][target_col]
    #         return True
            
    # if(down):
    #     if(grid[empty[0] + 1][empty[1]] == grid[target_row][target_col]):
    #         # car_object = find_object(grid)
    #         grid[target_row][target_col]= grid[empty[0]][empty[1]]
    #         grid[empty[0]][empty[1]] = grid[target_row][target_col]
    #         return True
     

# print(space_by_object(grid))
        
def move():
    run = True
    while run:
        left(grid,path)
        down(grid,path)
        right(grid,path)
        up(grid,path)    
        if space_by_object(grid, targetrow, targetcol) == True:
            run = False
        


move()
print(grid)     ###
print(path)