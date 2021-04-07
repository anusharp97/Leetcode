'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are 
all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
def numIslands(self, grid: List[List[str]]) -> int:
  islands = 0
  stack = []
  visited = set()
  if not grid:
      return islands
  row = len(grid)
  col = len(grid[0])
  for i in range(row):
      for j in range(col):
          if grid[i][j] == '1' and (i,j) not in visited:
              islands += 1
              visited.add((i,j))
              stack.append((i,j))
              #print(islands,stack,visited)
              while stack:
                  curRow, curCol = stack.pop()
                  for new in [(1,0),(0,1),(-1,0),(0,-1)]:
                      newRow = curRow+new[0]
                      newCol = curCol+new[1]
                      if newRow<0 or newRow>=row or newCol<0 or newCol>=col:
                          continue
                      if grid[newRow][newCol] == '1' and (newRow,newCol) not in visited:
                          stack.append((newRow,newCol))
                          visited.add((newRow,newCol))
  return islands
