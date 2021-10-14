# Github: Shantanugupta1118
# DAY 88 of DAY 100
# Edit Distance - InterviewBit


class Solution:
    def solve(self, A, B):
        # A, B = list(A), list(B)
        n, m = len(B), len(A)

        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i 
        for j in range(n+1):
            dp[0][j] = j 

        for i in range(m):
            for j in range(n):
                a = dp[i][j] + (0 if A[i]==B[j] else 1)   
                b = dp[i][j+1]+1
                c = dp[i+1][j]+1
                dp[i+1][j+1] = min(a, b, c)
        return dp[m][n]   


print(Solution().solve("Anshuman", "Antihuman"))