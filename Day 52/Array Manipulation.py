# Github: Shantanugupta1118
# DAY 52 of DAY 100
# Array Manipulation    -  Hackerrank

class Solution:
    def fnc(self, n, m):
        res = [0 for _ in range(n+2)]
        for i in range(m):
            a, b, c = map(int, input().split())
            res[a] += c
            res[b+1] -= c

        for i in range(1,n+1):
            res[i] += res[i-1]

        return res[res.index(max(res))]
        

size, n = map(int, input().split())
print(Solution().fnc(size, n))