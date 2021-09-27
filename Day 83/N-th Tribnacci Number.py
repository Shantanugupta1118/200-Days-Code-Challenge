# Github: Shantanugupta1118
# DAY 83 of DAY 100


from functools import lru_cache

class Solution:
    # ----------- Iterative Method - 28ms Runtime --------
    '''
    def tribonacci(self, n: int) -> int:
        if n<1: return 0
        if n==0 or n==1: return 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
        return dp[-1]
        '''
    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n<1: return 0
        if n==1 or n==2: return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
            
for _ in range(int(input())):
    n = int(input())
    print(Solution().tribonacci(n))