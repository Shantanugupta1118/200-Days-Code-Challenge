# Github: Shantanugupta1118
# DAY 123 of DAY 200
# 78. Subset

from itertools import combinations as cb


class Solution:
    def solve(self, nums):
        arr = [[]]
        for i in range(len(nums)):
            arr.extend(list(map(list, cb(nums, i+1))))
        print(arr)
    
    
print(Solution().solve([1,2,3]))