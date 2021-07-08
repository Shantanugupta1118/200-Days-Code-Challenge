


class Solution:
    def getMax(self, arr):
        arr.sort()
        if arr[0]!=1: arr[0] = 1
        for ele in range(1, len(arr)):
            if arr[ele]-arr[ele-1] > 1:
                arr[ele] = arr[ele-1] + 1
        return arr[len(arr)-1]

arr = [3,5,4,6,6]
print(Solution().getMax(arr))