# Github: Shantanugupta1118
# DAY 113 of DAY 200
# 268. Missing Number



class Solution:
    def solve(self, nums):
        for i in range(len(nums)+1):
            if i not in nums: return i
    
    
print(Solution().solve([3,0,1,5,4]))

