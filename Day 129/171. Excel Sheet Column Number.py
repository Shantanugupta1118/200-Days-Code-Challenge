# Github: Shantanugupta1118
# Day 128 of day 200
# 171. Excel Sheet Column Number


"""
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
"""

class Solution:
    def titleToNumber(self, s):
        count = 0
        n = len(s)
        for i in range(n):
            count += ((ord(s[i])-ord("A")+1)*pow(26, n-i-1))
        return count


print(Solution().titleToNumber("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(Solution().titleToNumber("AB"))
print(Solution().titleToNumber("YZ"))
print(Solution().titleToNumber("ZY"))
print(Solution().titleToNumber("FIG"))
print(Solution().titleToNumber("RTYH"))
print(Solution().titleToNumber("AA"))
print(Solution().titleToNumber("FXSHRXW"))
print(Solution().titleToNumber("YH"))
print(Solution().titleToNumber("ACKDH"))

