'''
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".

'''
import math
def titleToNumber(self, s: str) -> int:
    n = len(s)
    if n==1:
        return ord(s[0])-64
    else:
        res = 0
        for i in range(n):
            res += (ord(s[i])-64) * int(math.pow(26,n-i-1))
        return res

'''
Space complexity = O(1)
Time complexity = O(n)
'''
