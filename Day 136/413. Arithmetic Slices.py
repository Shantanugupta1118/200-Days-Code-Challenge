# Github: Shantanugupta1118
# Day 136 of day 200
# 413. Arithmetic Slices


class Solution:
    def consecutiveArithmetic(self, nums):
        if len(nums) < 3: return 0
        res = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if diff == nums[j]-nums[j-1]:
                    res += 1
                else:
                    break
        return res



        

print(Solution().consecutiveArithmetic([1,2,3,4]))
print(Solution().consecutiveArithmetic([1]))
print(Solution().consecutiveArithmetic([1,3,5,7,9]))
