# Github: Shantanugupta1118
# DAY 39 of DAY 100
# 629. K Inverse Pairs Array
# https://leetcode.com/problems/k-inverse-pairs-array/


class Solution:
    def kInverse(self, n, k):
        MOD = (10**9)+7
        pre = [0]*(k+1)
        pre[0] = 1
        for i in range(2, n+1):
            curr = [0]*(k+1)
            curr[0] = 1
            for j in range(1, k+1):
                curr[j] = curr[j-1] + pre[j] - (pre[j-1] if j>=i else 0)
                if curr[j]==0:
                    break
            pre = curr
        return pre[k]%MOD

n = int(input())
k = int(input())
print(Solution().kInverse(n, k))