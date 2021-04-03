'''
1814. Count Nice Pairs in an Array

You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. 
For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:
0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

Example 1:
Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:
Input: nums = [13,10,35,24,76]
Output: 4
 
Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''
def countNicePairs(self, nums: List[int]) -> int:
  # The condition can be rearranged to (nums[i] - rev(nums[i])) == (nums[j] - rev(nums[j])).
  revNums = [int(str(i)[::-1]) for i in nums]
  diff = {}
  n = len(nums)
  for i in range(n):
      difference = nums[i]-revNums[i]
      if difference not in diff:
          diff[difference] = 1
      else:
          diff[difference] += 1
  ans = 0
  for k,v in diff.items():
      if v>=2:
          # choose 2 numbers (a pair) out of v = nC2 = n(n-1)//2
          ans += (v*(v-1))//2
  return ans%(pow(10,9)+7)
'''
Space complexity: O(n)
Time complexity: O(n)
'''
