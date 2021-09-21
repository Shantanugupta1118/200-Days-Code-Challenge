# Github: Shantanugupta1118
# DAY 79 of DAY 100

class Solution:
    def solve(self):
        arr = list(map(int, input().split()))
        k = int(input())
        if len(arr) == k: return sum(arr)
        summ = 0
        mx = 0
        for i in range(len(arr)):
            mx = max(mx, summ)
            summ = 0
            for j in range(i, k):
                summ += arr[j]
        mx = max(mx, summ)
        return mx

for _ in range(int(input())):
    print(Solution().solve())