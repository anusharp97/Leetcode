'''
290. Word Pattern


Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''
def wordPattern(self, pattern: str, str: str) -> bool:
  res = {}
  n = len(pattern)
  words = str.split(' ')
  if n!= len(words):
      return False
  for i in range(n):
      if pattern[i] not in res and words[i] not in res.values():
          res[pattern[i]] = words[i]
      else:
          try:
              if words[i] != res[pattern[i]]:
                  return False
          except:
              return False
  return True
 
 '''
 Time complexuty: O(n) where n is the length of pattern
 Space complexity: O(m) where m is unique number of characters in pattern
 '''
