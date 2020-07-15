'''
Reverse words in a string
Given an input string, reverse the string word by word.

Input: "the sky is blue"
Output: "blue is sky the"

Input: "  hello world!  "
Output: "world! hello"

Input: "a good   example"
Output: "example good a"
'''
def reverseWords(self, s: str) -> str:
  l = s.split()
  l.reverse()
  return (' '.join(l))
