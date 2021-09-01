# Github: Shantanugupta1118
# DAY 74 of DAY 100 - Leetcode/Aug
# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def solve(self, arr):
        miss = 0
        mn = min(arr)
        if mn < 0: return mn
        for i in range(mn):
            if i not in arr:
                miss += 1
        return mn

print(Solution().solve([3,4,5,1,2]))