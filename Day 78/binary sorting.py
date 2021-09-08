# Github: Shantanugupta1118
# DAY 78 of DAY 100
# 1888. Minimum Number of Flips to Make the Binary String Alternating - Leetcode
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/


class Solution:
    def solve(self, s):
        ret = len(s)
        odd1, even1 = 0, 0
        for i, digit in enumerate(s):
            if i%2 == 0 and digit == "1":
                even1 += 1
            elif i%2==1 and digit == "1":
                odd1 += 1
        total = odd1+even1
        for i in range(len(s)):
            flips = even1 + (len(s)//2 - odd1)
            ret = min(ret, flips)
            flips = (len(s) - len(s)//2 - even1) + odd1
            ret = min(ret, flips)
            if len(s)%2==0:
                break
            else:
                even1 = odd1 + (1 if s[i] == "1" else 0)
                odd1 = total - even1
        return ret


n = input()
print(Solution().solve(n))
