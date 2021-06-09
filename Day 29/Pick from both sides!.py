# Github: Shantanugupta1118
# DAY 29 of DAY 100
# Pick from both sides! - InterviewBit
# https://www.interviewbit.com/problems/pick-from-both-sides/

import sys

class Solution:
    def solve(self, A, B):
        n, p = len(A), 0
        q, count, window =  n-1, 0, B
        for i in range(B):
            count += A[i]
        mx = -sys.maxsize
        i = 0
        while window!=0 and i<B:
            count -= A[window-1]
            count += A[q]
            window -= 1
            q -= 1
            mx = max(count, mx)
            i+=1
        return mx