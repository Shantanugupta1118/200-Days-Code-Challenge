# Github: Shantanugupta1118
# DAY 65 of DAY 100

class Solution:
    def solve(self, arr, n):
        space = 0
        minimum_range = min(arr)
        if minimum_range<0:
            space = abs(minimum_range)
        for i in range(n):
            if arr[i]<0:
                print((space-abs(arr[i]))*" "+(abs(arr[i])+1)*"*")
            else:
                print(space*" "+(arr[i]+1)*"*")



for _ in range(int(input())):
    arr = [-3, 4, 3, 1, -4]
    print(Solution().solve(arr, len(arr)))