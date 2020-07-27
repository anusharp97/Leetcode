'''
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
'''
def countOdds(self, low: int, high: int) -> int:
  if (high-low+1)&1 == 0: #even numbers
      # If the range (high - low + 1) is even, the number of even and odd numbers in this range will be the same.
      return (high-low+1)//2
  else:
      # If the range (high - low + 1) is odd, the solution will depend on the parity of high and low.
      if high&1 == 0:
          return (high-low+1)//2
      else:
          return (high-low)//2 + 1
