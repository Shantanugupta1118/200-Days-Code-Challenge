# Github: Shantanugupta1118
# DAY 73  of DAY 100
# 283. Move Zeroes -- Leetcode/COde
# https://leetcode.com/problems/move-zeroes/


class Solution:
    def solve(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


print(Solution().solve([0,1,0,3,12]))
print(Solution().solve([0]))
