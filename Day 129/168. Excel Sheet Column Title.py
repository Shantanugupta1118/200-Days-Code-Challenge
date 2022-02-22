# Github: Shantanugupta1118
# Day 128 of day 200
# 168. Excel Sheet Column Title


from cgitb import reset


class Solution:
    def toTitle(self, n):
        res = ""
        while n:
            n -= 1
            res = chr(n%26+ord('A')) + res
            n //=26
        return res

print(Solution().toTitle(701))