'''
Given an integer, write a function to determine if it is a power of three.

Input: 27
Output: true

Input: 45
Output: false
'''
  def isPowerOfThree(self, n: int) -> bool:
  if n<1:
      return False
  while n%3 == 0:
      n /= 3
  if n==1:
      return True
  else:
      return False
