# Github: Shantanugupta1118
# DAY 38 of DAY 100
# Range Sum Query - Mutable - Leetcode/June21
# https://leetcode.com/problems/range-sum-query-mutable/


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.sums = sum(nums)


    def update(self, index, val):
        if val >= self.nums[index]:
            self.sums += (val - self.nums[index])
        else:
            self.sums -= (self.nums[index] - val)
        self.nums[index] = val


    def sumRange(self, left, right):
        left_sum = sum(self.nums[:left])
        right_sum = sum(self.nums[right + 1:])
        return self.sums - left_sum - right_sum


nums = [1,5,6,3,2,4]
ans = Solution(nums)
print(ans.sumRange(1,4))
ans.update(3, 8)
print(ans.sumRange(2,5))
