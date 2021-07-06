# Github: Shantanugupta1118
# DAY 51 of DAY 100
# Count Vowels Permutation
# https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3802/



class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = []
        rw1 = [1]*5
        dp.append(rw1)
        MOD = 10**9 + 7
        for i in range(1, n):
            dp.append([0]*5)
            for j in range(0,5):
                if j==0:
                    dp[i][j] = dp[i-1][1]
                elif j==1:
                    dp[i][j] = dp[i-1][0] + dp[i-1][2]
                elif j==2:
                    dp[i][j] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4])
                elif j==3:
                    dp[i][j] = dp[i-1][2] + dp[i-1][4]
                elif j==4:
                    dp[i][j] = dp[i-1][0]

        return (sum(dp[n-1]))%MOD

n = int(input())
print(Solution().countVowelPermutation(n))
