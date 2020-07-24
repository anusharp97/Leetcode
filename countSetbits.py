'''
191. Number of 1 Bits
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Input: 00000000000000000000000000001011
Output: 3

Input: 00000000000000000000000010000000
Output: 1

Input: 11111111111111111111111111111101
Output: 31
'''

def hammingWeight(self, n: int) -> int:
  count = 0
  bit = 1
  while n>=bit:
      if n & bit:
          count += 1
      bit = bit<<1
  return count
