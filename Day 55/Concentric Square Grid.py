# Github: Shantanugupta1118
# DAY 55 of DAY 100
# Concentric Square Grid  - InterviewBit
# https://www.interviewbit.com/problems/prettyprint/

class Solution:
    def concentric_grid(self, n):
        grid = n*2 - 1
        dp = [[0 for x in range(grid)] for x in range(grid)]
        for i in range(grid):
            for j in range(grid):
                if abs(i-(n-1)) > abs(j - (n-1)):
                    dp[i][j] = abs(i-(n-1)) + 1
                else:
                    dp[i][j] = abs(j-(n-1)) + 1
        return dp

res = Solution().concentric_grid(3)
for x in res:
    print(*x)