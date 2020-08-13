'''
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def generate(self, numRows: int) -> List[List[int]]:
  if numRows == 0:
      return 
  if numRows == 1:
      return [[1]]
  res = [[1] for i in range (numRows)]
  res[1].append(1)
  for i in range(2,numRows):
      for j in range(1,i):
          res[i].append(res[i-1][j]+res[i-1][j-1])
      res[i].append(1)
  return res
