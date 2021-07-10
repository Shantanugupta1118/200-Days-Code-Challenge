# Github: Shantanugupta1118
# DAY 52 of DAY 100
# Decode Way II   -   Leetcode/July
# https://leetcode.com/problems/decode-ways-ii/



class Solution:
    def numDecode(self, S):
        MOD, dp = 10**9+7, [1, 0, 0]
        for x in S:
            temp = [0, 0, 0]
            if x == '*':
                temp[0] = 9*dp[0] + 9*dp[1] + 6*dp[2]
                temp[1] = dp[0]
                temp[2] = dp[0]
            else:
                temp[0] = (x>'0')*dp[0] + dp[1] + (x<='6')*dp[2]
                temp[1] = (x=='1')*dp[0]
                temp[2] = (x=='2')*dp[0]
            dp = [i%MOD for i in temp]
        return dp[0]

St = input()
print(Solution().numDecode(St))