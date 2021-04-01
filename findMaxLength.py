'''
525. Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

'''
def findMaxLength(self, nums: List[int]) -> int:
  map = {}
  map[0] = -1
  total = 0
  length = 0
  for i,n in enumerate(nums):
      total += -1 if n == 0 else 1
      if total in map:
          length = max(length,i-map[total])
      else:
          map[total] = i
  return length
  
  '''
  The idea is to replace 0 with -1 and then find the longest subarray with sum 0. 
  Time complexity = O(n)
  Space complexity = O(1)
  '''
