'''
1209. Remove All Adjacent Duplicates in String II

Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
'''

def removeDuplicates(self, s: str, k: int) -> str:
  stack = []
  n = len(s)
  res = ""
  stack.append((s[0],1))
  for i in range(1,n):
      #print(stack)
      if not stack:
          stack.append((s[i],1))
          continue
      elif s[i] == stack[-1][0]:
          cur,count = stack.pop()
          count+=1
          stack.append((cur,count))
      else:
          stack.append((s[i],1))
      if stack[-1][1] == k:
          stack.pop()
  size = len(stack)
  for i in range(size):
      ch,length = stack[i]
      res+=ch*length
  return res
