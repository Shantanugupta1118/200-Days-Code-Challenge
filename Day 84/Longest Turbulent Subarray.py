# Github: Shantanugupta1118
# DAY 84 of DAY 100

class Solution:
    def solve(self, arr):
        if len(arr) is 0: return 0
        if len(arr)<2: return 1
        ls = [1]
        n = len(arr)
        for i in range(n):
            pass

arr = list(map(int, input().split()))
print(Solution().solve(arr))