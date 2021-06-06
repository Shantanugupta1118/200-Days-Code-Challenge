# Github: Shantanugupta1118
# DAY 26 of DAY 100
# # 78 Subsets - Leetcode/Google
# https://leetcode.com/problems/subsets/

import itertools
class Solution:
    def subsets(self, nums):
        new_arr = [[]]
        for i in range(len(nums)):
            new_arr.extend(list(map(list,itertools.combinations(nums, i+1))))
        return new_arr  

arr = [1,2,3]
arr2 = [0]
print(Solution().subsets(arr))
print(Solution().subsets(arr2))