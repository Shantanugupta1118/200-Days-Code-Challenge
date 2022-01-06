# Github: Shantanugupta1118
# DAY 91 of DAY 100
# 312. Burst Balloons - Leetcode
# https://leetcode.com/problems/burst-balloons/


class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for gap in range(len(nums)):
            for left in range(len(nums)-gap):
                right = left + gap
                res = 0
                for i in range(left+1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    res = max(res, coins + dp[left][i] + dp[i][right])
                dp[left][right] = res
        return dp[0][len(nums)-1]

    def solve(self, nums):
        return self.maxCoins(nums)

for _ in range(int(input())):
    print(Solution().solve([3,1,5,8]))