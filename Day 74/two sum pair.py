# Github: Shantanugupta1118
# DAY 74 of DAY 100

class Solution:
    def solve(self, arr):
        i = 0
        triplet = []
        while i<len(arr)-2:
            for j in range(1,len(arr)-1):
                if abs(arr[i]-arr[j]) in arr:
                    triplet.append([arr[i], arr[j], abs(arr[i]-arr[j])])
                    i += 1
        return len(triplet)

print(Solution().solve([1,5,3,2]))