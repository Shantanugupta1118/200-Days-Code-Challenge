# Github: Shantanugupta1118
# DAY 52 of DAY 100
# Array Manipulation    -  Hackerrank

class Solution:
    def fnc(self, size, n):
        res = [0 for _ in range(size)]
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().split())))
        for x in arr:
            for i in range(x[0]-1, x[1]):
                res[i] += x[2]
        return res




size, n = map(int, input().split())
print(max(Solution().fnc(size, n)))