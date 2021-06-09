# Github: Shantanugupta1118
# DAY 29 of DAY 100
# 3Sum-Closest - Leetcode
# https://leetcode.com/problems/3sum-closest/


import sys

class solution:
    def max_sum(self, A, target):
        A.sort()
    
        res, max_diff = 0, sys.maxsize
        for i in range(len(A)-2):
            j, k = i+1, len(A)-1
            m, min_diff = 0, 0
            while j<k:
                m = A[i] + A[j] + A[k]
                min_diff = abs(target - m)
                if min_diff < max_diff:
                    max_diff = min_diff
                    res = m
                if m > target:
                    k -= 1
                else:
                    j += 1
        return res
# A = [-1, 2, 1, -4]
# A = [0, 0, 0, 0]
A = [1,1,-1,-1,3]
tar = -1
print(solution().max_sum(A, tar))