# Github: Shantanugupta1118
# DAY 71 of DAY 100
# 926. Flip string to monotype increase - Leetcode/August
# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3876/



class Solution:
    def solve(self, str):
        length = len(str)
        zeros = 0
        ones = str.count("1")
        res = ones
        for i in reversed(str):
            if i=="1":
                ones -= 1
            else:
                zeros += 1
            res = min(res, zeros+ones)
        return res


for _ in range(int(input())):
    s = input()
    print(Solution().solve(s))