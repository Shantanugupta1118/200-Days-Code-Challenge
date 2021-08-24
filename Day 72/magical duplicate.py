# Github: Shantanugupta1118
# DAY 72 of DAY 100
# Magical String[Duplicate Problem]  - GFG
# https://practice.geeksforgeeks.org/problems/magical-string3653/0/

class Solution:
    def solve(self, s):
        res = ""
        for i in s:
            asci = ord(i)
            suffix = asci - 97
            prefix = 122 - suffix
            res += chr(prefix)
        return res

for _ in range(int(input())):
    s = input()
    print(Solution().solve(s))