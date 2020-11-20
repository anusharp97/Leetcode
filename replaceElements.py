'''
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 
Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''
def replaceElements(self, arr: List[int]) -> List[int]:
  tmax = -1
  n = len(arr)
  if n==1:
      return [-1]
  for i in range(n-1,0,-1):
      temp = arr[i]
      arr[i] = tmax
      tmax = max(tmax,temp)
  arr[0] = max(tmax,arr[1])
  return arr
  
  '''
  Time complexity = O(n), n = len(arr)
  Space complexity = O(1)
  '''
