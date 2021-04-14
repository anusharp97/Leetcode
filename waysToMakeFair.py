'''
1664. Ways to Make a Fair Array
You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:

Choosing to remove index 1 results in nums = [6,7,4,1].
Choosing to remove index 2 results in nums = [6,1,4,1].
Choosing to remove index 4 results in nums = [6,1,7,4].
An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.

Example 1:
Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.

Example 2:

Input: nums = [1,1,1]
Output: 3
Explanation: You can remove any index and the remaining array is fair.

Example 3:
Input: nums = [1,2,3]
Output: 0
Explanation: You cannot make a fair array after removing any index.
 
Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
'''

'''
Solution Approach:

Maintain PrefixSum and SuffixSum for odd and even index seperately.
Let consider the following variable:
leftOdd[i] : Denote the prefixSum of element on odd index till i-1.
leftEven[i] : Denote the prefixSum of element on even index till i-1.
rightOdd[i] : Denote the SuffixSum of element of odd index till i+1.
rightEven[i] : Denote the SuffixSum of element of even index till i+1.

Now, check if the ith element is the special or not.

If leftOdd[i] + rightEven[i] == leftEven[i] + rightOdd[i], then ith element is special, so we increase the count.
'''

def waysToMakeFair(self, A: List[int]) -> int:
  n = len(A)
  count = 0
  leftOdd = [0]*n
  leftEven = [0]*n
  rightOdd =[0]*n
  rightEven = [0]*n
  for i in range(1,n):
      #odd index 
      if i&1:
          leftOdd[i] = leftOdd[i-1]
          leftEven[i] = leftEven[i-1]+A[i-1]

      else:
          leftEven[i] = leftEven[i-1]
          leftOdd[i] = leftOdd[i-1]+A[i-1]

  for i in range(n-2,-1,-1):
      if i&1:
          rightOdd[i] = rightOdd[i+1]
          rightEven[i] = rightEven[i+1]+A[i+1]
      else:
          rightEven[i] = rightEven[i+1]
          rightOdd[i] = rightOdd[i+1]+A[i+1]
  for i in range(n):
      if leftOdd[i]+rightEven[i] == rightOdd[i]+leftEven[i]:
          count+=1
  return count
