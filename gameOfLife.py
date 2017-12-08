import copy
import time

def generate_cell(grid,r,c):
  nbCells = 0
  for y in range(-1,2):
    for x in range(-1,2):
      row = r + y
      col = c + x    
      if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[r]) and not(x==0 and y==0):        
        nbCells += grid[row][col]
          
  newValue = grid[r][c]
  if grid[r][c]:  # cell
    # each cell with two or three neighbors survives
    if nbCells < 2 or nbCells > 3:
      newValue = 0
  else:               # empty
    # each case with three neighbors becomes populated
    if nbCells == 3:
      newValue = 1

  return newValue

# init grid
row,col = 15,15
grid = [[0 for i in range(col)] for j in range(row)]

# init cells
mid = int(row/2) 
grid[mid][mid-1],grid[mid][mid],grid[mid][mid+1]= 1,1,1
grid[mid-1][mid+1],grid[mid-2][mid]=1,1
print(grid)

# play generation
while(True):
  newGrid = copy.deepcopy(grid)
  for r in range(row):
    for c in range(col):
      newValue = generate_cell(grid,r,c)
      newGrid[r][c] = newValue
  grid = copy.deepcopy(newGrid)
  print(grid)
  time.sleep(.25)



