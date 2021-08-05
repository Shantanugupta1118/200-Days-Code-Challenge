# Github: Shantanugupta1118
# DAY 64 of DAY 100
# 1.-  Leetcode/August
#https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3836/



class Solution:
    def subset_fnc(self, num):
        res = [[]]
        if len(num)<=1:
            res.append(num)
        for i in range(len(num)-1):
            for j in range(i, len(num)):
                res.append(num[i:j+1])
        return res

n = [0]
print(Solution().subset_fnc(n))