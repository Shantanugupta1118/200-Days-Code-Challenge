# Github: Shantanugupta1118
# DAY 65 of DAY 100

class Solution:
    def interstion_sort(self, arr):
        for i in range(1,len(arr)):
            key = arr[i]
            j = i
            while arr[j-1] > key and j>=1:
                arr[i] = arr[j-1]
                j -= 1
            arr[j] = key

for _ in range(int(input())):
    arr = [5,2,4,8,6,2,1,4,7,8,10,84,6,46,54,6,4,604,6,4,6,40]
    Solution().interstion_sort(arr)
    print(arr)