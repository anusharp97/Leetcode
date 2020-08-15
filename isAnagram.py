'''
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

def isAnagram(self, s: str, t: str) -> bool:
  sLength = len(s)
  tLength = len(t)
  counter = [0] * 26
  if sLength != tLength:
      return False
  for i in range(sLength):
      counter[ord(s[i]) - 97] += 1
      counter[ord(t[i]) - 97] -= 1
  for i in range(26):
      if counter[i] != 0:
          return False
  return True
  
  '''
  Time complexity = O(n)
  Space complexity = O(1)
  '''
