# Github: Shantanugupta1118
# DAY 41 of DAY 100
# Pascal's Triangle II - Leetcode/June21
# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def pascal(self, n):
        res = [[1]]
        while len(res)!=n+1:
            temp = [1]
            for i in range(len(res[-1])-1):
                temp.append(res[-1][i] + res[-1][i+1])
            temp.append(1)
            res.append(temp)
        return res[-1]


for i in range(5):
    print(Solution().pascal(i))