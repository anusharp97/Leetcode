"""
452. Minimum Number of Arrows to Burst Balloons
There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. 
Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.
An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.
Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2

Example 4:
Input: points = [[1,2]]
Output: 1

Example 5:
Input: points = [[2,3],[2,3]]
Output: 1

Constraints:
0 <= points.length <= 104
points.length == 2
-231 <= xstart < xend <= 231 - 1
"""
def findMinArrowShots(self, points: List[List[int]]) -> int:
  n = len(points)
  if n<=1:
      return n
  points.sort(key= lambda x: x[1], reverse=True)
  prevMax = points[0][1]
  prevMin = points[0][0]
  count = 1
  for i in range(1,n):
      curStart = points[i][0]
      curEnd = points[i][1]
      """
      Check if either of previous start or end cover the current interval, for example: 
      previous start: [[10,16],[7,12]] (arrow shot up at x = 10)
      previous end: [[10,15],[13,15]] (arrow shot up at x = 15)
      Check if either of current start or end covers the previous interval, for example:
      current start: [[10,13],[11,12]] (arrow shot up at x = 11)
      current end:[[10,13],[7,12]] (arrow shot up at x = 12)
      if the interval cannot be covered by any other interval, then increment the count and update the previous values.
      """
      if (prevMin<=curEnd and prevMin>=curStart) or (prevMax>=curStart and prevMax<=curEnd) 
      or (curEnd>=prevMin and curEnd<=prevMax) or (curStart<=prevMax and curStart>=prevMin):
          prevMin = max(prevMin, curStart)
          prevMax = min(prevMax, curEnd)
          continue
      else:
          count+=1
          prevMin = curStart
          prevMax = curEnd
  return count
  
  """
  n = length(points)
  Time complexity = O(n)
  Space complexity = O(1)
  """
