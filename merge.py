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
  # sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.
  res = []
  n = len(intervals)
  if n<=1:
      return intervals
  start = intervals[0][0]
  end = intervals[0][1]
  for i in range(1,n):
      curStart = intervals[i][0]
      curEnd = intervals[i][1]
      if curStart<=end:
          end = max(curEnd,end)
      else:
          res.append([start,end])
          start = curStart
          end = curEnd
  if [start,end] not in res:
      res.append([start,end])
  return res
  #   if not intervals:
#       return
#   intervals.sort(key = lambda x: x[0])
#   n = len(intervals)
#   prevStart, prevEnd = intervals[0][0], intervals[0][1]
#   res = {}
#   res[prevStart] = prevEnd
#   for i in range(1,n):
#       curStart, curEnd = intervals[i][0], intervals[i][1]
#       # if the current interval begins before the end of previous interval
#       # we merge them by updating the end of the previous interval if it is less than the end of the current interval.
#       if prevEnd >= curStart:
#           if curEnd > prevEnd:
#               res[prevStart] = curEnd
#               prevEnd = curEnd
#       else:
#       # If the current interval begins after the previous interval ends, then they do not overlap
#           res[curStart] = curEnd
#           prevStart = curStart
#           prevEnd = curEnd
#   result = []
#   for key,val in res.items():
#       result.append([key,val])
#   return result
  
  '''
  Time complexity = O(nlogn)
  Space complexity = O(n)
  '''
