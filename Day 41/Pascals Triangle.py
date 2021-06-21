# Github: Shantanugupta1118
# DAY 41 of DAY 100
# Pascal's Triangle - Leetcode/June21
# https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3786/


class Solution:
    def solution(self, n):
        res = [[1]]
        while len(res)!=n:
            temp = [1]
            for i in range(len(res[-1])-1):
                temp.append(res[-1][i] + res[-1][i+1])
            temp.append(1)
            res.append(temp)
        return res 

print(Solution().solution(5))