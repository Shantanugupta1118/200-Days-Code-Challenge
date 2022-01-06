# Github: Shantanugupta1118
# DAY 74 of DAY 100

class Solution:
    def reverse_list(self, nums):
        N = len(nums)
        i, j = 0, N-1
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def solve(self, arr):
        n = len(arr)
        i = n-1
        while i > 0 and arr[i] <= arr[i-1]:
            i -= 1
        if i==0:
            self.reverse_list(arr)
            return 
        i -= 1
        j = n-1
        while arr[j] <= arr[i]:
            j -= 1
        self.swap(arr, i, j)
        arr[i+1:] = sorted(arr[i+1:])
        return arr

for arr in [[1,2,3],[1,3,2],[3,2,1]]:
    # print(arr)
    print(Solution().solve(arr))