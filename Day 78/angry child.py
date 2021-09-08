# Github: Shantanugupta1118
# DAY 78 of DAY 100
# Angry Child - Hackerrank

class Solution:
    '''
    # test Case - 4/20
    def solve(self, ar, n, k):
        # ar = list(set(arr))
        ar = sorted(ar)
        mx = []
        for i in range(k):
            mx.append(ar[i])
        return max(mx) - min(mx)
    '''
    # Full test case pass
    def solve(self, arr, n, k):
        arr = sorted(arr)
        res = arr[-1]
        
        for ind in range(n-k+1):
            res = min(res, arr[ind+k-1] - arr[ind])
        return res

n = int(input())
k = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(Solution().solve(arr, n, k))