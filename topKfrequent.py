"""
Given a non-empty array of integers, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
"""
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
  res = {}
  # res dictionary stores the frequency of every element in nums
  length = len(nums)
  for i in range(length):
      if nums[i] not in res:
          res[nums[i]] = 1
      else:
          res[nums[i]] += 1
  # sort the dictionary in descending order by value
  result = sorted(res.items(), key=lambda item:item[1], reverse = True)
  resultList = []
  # return the first k elements from dictionary as result
  for i in range(k):
      resultList.append(result[i][0])
  return resultList
