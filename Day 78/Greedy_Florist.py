# Github: Shantanugupta1118
# DAY 78 of DAY 100

class Solution:
    def solve(self, n, k, arr):
        arr.sort(reverse=True)
        cost, prev_purchase = 0, 0
        for i in range(n):
            cost += (prev_purchase+1)*arr[i]
            if (i+1)%k==0: prev_purchase += 1
        return cost

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(Solution().solve(n, k, arr))