# Github: Shantanugupta1118
# DAY 108 of DAY 100
#421. Maximum XOR of Two Numbers in an Array


class Solution:
    def maxXor(self, nums):
        mx = -999
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if mx < nums[i]^nums[j]:
                    mx = nums[i]^nums[j]
        return mx
    
    
print(Solution().maxXor([3,10,5,25,2,8]))
print(Solution().maxXor([14,70,53,83,49,91,36,80,92,51,66,70]))