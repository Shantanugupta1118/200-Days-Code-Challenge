# Github: Shantanugupta1118
# DAY 81 of DAY 100

class Solution:
    def solve(self):
        mx = -99
        arr = list(map(str, input().split()))
        # print(arr, len(arr))
        if len(arr)==1: return len(arr[0])
        for i in range(len(arr)-1):
            temp = arr[i]+arr[i+1]
            mx = max(mx, len(temp))
            # print(temp)
        return mx

for _ in range(int(input())):
    print(Solution().solve())