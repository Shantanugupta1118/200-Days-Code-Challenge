# Github: Shantanugupta1118
# DAY 39 of DAY 100
# Max Non Negative SubArray   -   InterviewBit
# https://www.interviewbit.com/problems/max-non-negative-subarray/

import sys
class Solution:
    def solve(self, arr):
        start, end, temp_start, temp_end = -1, -1, 0, 0
        total = -(sys.maxsize)
        temp_total = 0 
        for i in range(len(arr)):
            if arr[i] < 0:
                temp_start = i+1
                temp_end = i + 1
                temp_total = 0 
            else:
                temp_total += arr[i]
                if temp_total > total:
                    start = temp_start
                    end = i 
                    total = temp_total
                elif (temp_total == total) and (temp_end - temp_start > end - start):
                    start = temp_start
                    end = i
                    total = temp_total
                temp_end += 1
        if start == -1:
            return []
        res = [] 
        for i in range(start, end+1):
            res.append(arr[i])
        return res  


TC = [[10, -1, 2, 3, -4, 100], [1, 2, 5, -7, 2, 3]]
for arr in TC:
    print(Solution().solve(arr))