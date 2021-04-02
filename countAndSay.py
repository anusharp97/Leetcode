'''
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. 
Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and 
concatenate every saying.

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

Constraints:

1 <= n <= 30
'''
def countAndSay(self, n: int) -> str:
  mp = {}
  #mp[0] = 1
  prev = "1"
  if n==1:
      return "1"
  else:
      for i in range(1,n):
          cur = prev
          size = len(cur)
          count = 1
          ans = ""
          j = 0
          while j<size:
              while j+1<size and cur[j] == cur[j+1]:
                  count += 1
                  j+=1
              ans += str(count)+cur[j]
              #print(ans)
              count = 1
              j += 1
          prev = ans
      #print(mp)
      return prev
