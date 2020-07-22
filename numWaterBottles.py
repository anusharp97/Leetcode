'''
1518. Water Bottles
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

1 <= numBottles <= 100
2 <= numExchange <= 100
'''

def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
  if numExchange > numBottles:
      return numBottles
  elif numExchange == numBottles:
      return numBottles+1
  else:
      leftBottles = numBottles
      count = leftBottles
      while leftBottles>=numExchange:
          leftBottles = leftBottles - numExchange + 1
          count += 1
      return count
