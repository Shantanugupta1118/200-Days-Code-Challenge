# Github: Shantanugupta1118
# Day 135 of day 200
# 976. Largest Perimeter Triangle


class Solution:
    def largestPerimeterOfTri(self, nums):
        nums.sort()
        for i in range(len(nums)-3, -1, -1):
            if nums[i]+nums[i+1] > nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0

print(Solution().largestPerimeterOfTri([2,1,2]))
print(Solution().largestPerimeterOfTri([1,2,1]))