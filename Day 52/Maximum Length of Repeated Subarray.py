

import sys
class Solution:
    def findLength(self, l1, l2):
        n, m = len(l1), len(l2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_count = -sys.maxsize
        for i in range(m):
            for j in range(n):
                if l1[i]==l2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = 0
                    print(dp[i][j], end=' ')
                max_count = max(max_count, dp[i+1][j+1])
        return max_count


nums1 = [0,0,0,0,0,0,0]
nums2 = [0,0,0,0,0,0,0]
print(Solution().findLength(nums1, nums2))