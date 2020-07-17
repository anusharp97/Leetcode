"""
451. Given a string, sort it in decreasing order based on the frequency of characters.

Input: "tree"
Output: "eert"
"eetr" is also a valid answer.

Input: "cccaaa"
Output: "cccaaa"
"aaaccc" is also a valid answer.

"""
def frequencySort(self, s: str) -> str:
  freq = {}
  for i in s:
      if i not in freq:
          freq[i] = 1
      else:
          freq[i] += 1
  res = sorted(freq.items(), key = lambda item: item[1], reverse =True)
  length = len(res)
  string = ""
  for i in range(length):
      key,value = res[i][0], res[i][1]
      for j in range(value):
          string += key
  return string
