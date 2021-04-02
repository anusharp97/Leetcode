'''
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
  intervals.sort(key=lambda x:x[0])
  print(intervals)
  res = []
  n = len(intervals)
  if n<=1:
      return intervals
  start = intervals[0][0]
  end = intervals[0][1]
  for i in range(1,n):
      interval = intervals[i]
      if interval[0]>end:
          res.append([start,end])
          start = interval[0]
          end = interval[1]
      else:
          end = max(end,interval[1])
          start = min(start, interval[0])
  res.append([start,end])
  return res
  
  '''
  Time complexity = O(nlogn)
  Space complexity = O(n)
  '''
