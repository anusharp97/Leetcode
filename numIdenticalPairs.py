'''
1512. Number of Good Pairs

Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Input: nums = [1,2,3]
Output: 0
'''
def numIdenticalPairs(self, nums: List[int]) -> int:
#  If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.
  goodpairs = 0
  countDict = {}
  for i in nums:
      if i not in countDict:
          countDict[i] = 1
      else:
          countDict[i] += 1
  for key,value in countDict.items():
      if value>1:
          goodpairs += value*(value-1)//2
  return goodpairs
