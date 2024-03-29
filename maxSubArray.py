'''
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
 
Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
'''
def maxSubArray(self, A: List[int]) -> int:
  total = 0
  cmax = float('-inf')
  n = len(A)
  for i in range(n):
      total += A[i]
      cmax = max(total,cmax,A[i])
      total = max(total,A[i])
  return cmax
