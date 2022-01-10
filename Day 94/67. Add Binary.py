# Github: Shantanugupta1118
# DAY 94 of DAY 100
# 67. Add Binary
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=bin(int(a,2) + int(b,2))
        return s[2:]

    def solve(self,a,b):
        return self.addBinary(a,b)

print(Solution().solve("11", "1"))