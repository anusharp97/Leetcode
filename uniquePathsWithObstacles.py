'''
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?

Note: m and n will be at most 100.

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
  m = len(obstacleGrid)
  n = len(obstacleGrid[0])
  dp = [[1 for i in range(n)]for j in range(m)]
  #print(dp)
  if obstacleGrid[0][0]:
      return 0
  for i in range(0,m):
      for j in range(0,n):
          if obstacleGrid[i][j] == 0:
              if i>0 and j>0:
                  dp[i][j] = dp[i-1][j] + dp[i][j-1]
              elif i>0:
                  dp[i][j] = dp[i-1][j]
              elif j>0:
                  dp[i][j] = dp[i][j-1]
          else:
              dp[i][j] = 0
  #print(dp)
  return dp[m-1][n-1]

'''
Time complexity = O(mn)
Space complexity = O(mn)
'''
