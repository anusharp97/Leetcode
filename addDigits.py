'''
258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
             
Refrenece: https://en.wikipedia.org/wiki/Digital_root
'''

#function to add digits untill the result has only one digit
def addDigits(self, num: int) -> int:
  if num <10:
      return num
  return (1+((num-1)%9))
