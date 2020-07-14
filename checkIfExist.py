'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j] 
'''
def checkIfExist(self, arr: List[int]) -> bool:
  res = {}
  length = len(arr)
  for i in range(length):
      if arr[i] not in res:
          res[arr[i]] = 1
      else:
          res[arr[i]] += 1
      if 2*arr[i] in res or arr[i]/2 in res:
          if arr[i] == 0 and res[arr[i]]>1:
              return True
          if arr[i] == 0:
              continue
          return True
  return False
