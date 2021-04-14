'''
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Example 4:
Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4

Example 5:
Input: nums = [0,0,0]
Output: 0
'''
def longestSubarray(self, nums: List[int]) -> int:
  left = 0
  maxLen = 0
  count = 0
  i = 0
  n = len(nums)
  idx = -1
  # corner case - if all the elements equal to 1
  if sum(nums) == n:
      return n-1
  # sliding window approach
  while i<n:
      if nums[i]==0:
          count += 1
          while count>1:
              if nums[left]==0:
                  count-=1
              left+=1
          idx = left
      else:
          maxLen = max(maxLen,i-idx)
      i+=1
  return maxLen
