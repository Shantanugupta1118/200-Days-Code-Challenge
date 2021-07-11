# Github: Shantanugupta1118
# DAY 54 of DAY 100
# Next Similar Number - InterviewBit
# https://www.interviewbit.com/problems/next-similar-number/


import copy
from operator import itemgetter
class Solution:
    def nums(self, arr):
        arr = list(str(arr))
        n = len(arr)
        if n == 1:
            return arr
        
        for i in range(n-1, 0, -1):
            if arr[i] > arr[i-1]:
                break
        if i!=0:
            for j in range(n-1, i+1, -1):
                if arr[i-1] < arr[j]:
                    arr[i-1], arr[j] = arr[j], arr[i-1]
                    break
            arr[i:] = sorted(arr[i:])
        else:
            return -1
        return arr
    
            

print(Solution().nums("4321"))
print(Solution().nums("740948"))