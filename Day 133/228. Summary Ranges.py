# Github: Shantanugupta1118
# Day 133 of day 200
# 228. Summary Ranges

class Solution:
    def summaryrange(self, nums):
        res = []
        i = j = 0
        while i<len(nums):
            while j < len(nums)-1 and nums[j+1]==nums[j]+1:
                j += 1
            s = str(nums[i])
            if j > i:
                s += "->"+str(nums[j])
            res.append(s)
            j += 1
            i = j
        return res


print(Solution().summaryrange([0,1,2,4,5,7]))
print(Solution().summaryrange([0,2,3,4,6,8,9]))