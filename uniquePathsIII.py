'''
980. Unique Paths III
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
'''
def uniquePathsIII(self, grid: List[List[int]]) -> int:
  rows = len(grid)
  cols = len(grid[0])
  nonObstacle = 0
  for i in range(rows):
      for j in range(cols):
          if grid[i][j] == 1:
              start = [i,j]
          if grid[i][j] == 2:
              end = [i,j]
          if grid[i][j]==0:
              nonObstacle+=1
  count = 0
  directions = [[0,-1],[-1,0],[1,0],[0,1]]
  stack = []
  nonObsCount = 0
  stack.append((start, [start],nonObsCount ))
  grid[start[0]][start[1]] = -1  # mark start node as visited
  while stack:
      [r,c], path,nonObsCount  = stack.pop()
      for d in directions:
          ni,nj = r+d[0],c+d[1]
  #traverse only for non obstacle nodes
          if 0<=ni<rows and 0<=nj<cols and grid[ni][nj]!=-1:
              if grid[ni][nj] == 2:
      #if you've reached the end node, check if you've visited all non obstacle nodes
                  if nonObsCount==nonObstacle:
                      #print('One of the paths',path)
                      count += 1
                  continue
              elif grid[ni][nj] == 1:
                  continue
              else:
                 #if [ni,nj] not in path, it's not visited yet, add it to the path
                  if [ni,nj] not in path:
                      stack.append(([ni,nj],path+[[ni,nj]], nonObsCount+1))
                  else:
         #check if [ni,nj] already in path, if so continue as its visited already
                      continue
  return count
