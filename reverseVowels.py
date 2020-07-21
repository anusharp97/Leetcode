'''
345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Input: "hello"
Output: "holle"

Input: "leetcode"
Output: "leotcede"
'''
def reverseVowels(self, s: str) -> str:
  i = 0
  j = len(s)-1
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  while(i<j):
      if s[i] in vowels and s[j] in vowels:
          temp = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
          s = temp
          i += 1
          j -= 1
      elif s[i] in vowels:
          j -= 1
      elif s[j] in vowels:
          i += 1
      else:
          i += 1
          j -= 1
  return s
