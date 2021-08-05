# Github: Shantanugupta1118
# DAY 65 of DAY 100
# Sort the Array - GFG


class Solution:
    def solve(self, arr, n):
        def quick_sort(arr, low, high):
            if low<high:
                pi = pivot(arr, low, high)
                quick_sort(arr, low, pi-1)
                quick_sort(arr, pi+1, high)

        def pivot(arr, low, high):
            piv = arr[high]
            idx = low-1
            for i in range(low, high):
                if arr[i] < piv:
                    idx += 1
                    arr[idx], arr[i] = arr[i], arr[idx]
            arr[idx+1], arr[high] = arr[high], arr[idx+1]
            return idx+1
        quick_sort(arr, 0, n-1)
        return arr


arr = [4, 6, 23, 65, 43, 76, 45, 32, 24, 1]
print(Solution().solve(arr, len(arr)))