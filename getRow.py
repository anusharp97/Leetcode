'''
119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 3
Output: [1,3,3,1]
'''

def getRow(self, rowIndex: int) -> List[int]:
  if rowIndex == 0:
      return [1]
  elif rowIndex == 1:
      return [1,1]
  elif rowIndex == 2:
      return [1,2,1]
  temp = [1,2,1]
  for i in range(2,rowIndex):
      res = [1]
      for j in range(1,len(temp)):
          res.append(temp[j]+temp[j-1])
      res.append(1)
      temp = res
  return res
