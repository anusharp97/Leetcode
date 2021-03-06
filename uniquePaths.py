'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
'''
def uniquePaths(self, m: int, n: int) -> int:
  dp = [[1 for i in range(n)]for j in range(m)]
  for i in range(m-2,-1,-1):
      for j in range(n-2,-1,-1):
          dp[i][j] = dp[i+1][j] + dp[i][j+1]
  return dp[0][0]
  
'''
m = 3, n= 2
dp = [[6,3,1],
      [3,2,1],
      [1,1,1]]

Time complexity = O(mn)
Space complexity = O(mn)
'''
