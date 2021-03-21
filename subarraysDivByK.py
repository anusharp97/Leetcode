'''
974. Subarray Sums Divisible by K

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
'''

def subarraysDivByK(self, nums: List[int], K: int) -> int:
  n = len(nums)
  count = 0
  remainder = collections.defaultdict(lambda:0)
  remainder[0] = 1
  curSum = 0
  for i,num in enumerate(nums):
      curSum += num
      r = curSum%K
      count += remainder[r]
      remainder[r] +=1
  return count

'''
Time Complexity = O(n)
Space Complexity = O(n)
Reference: https://www.youtube.com/watch?v=QM0klnvTQzk&ab_channel=Pepcoding
'''
