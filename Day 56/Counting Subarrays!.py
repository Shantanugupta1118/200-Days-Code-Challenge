# Github: Shantanugupta1118
# DAY 56 of DAY 100
# Counting Subarrays! - InterviewBit
# https://www.interviewbit.com/old/problems/counting-subarrays/


class Solution:
    def solve(self, A,B):
        n = len(A)
        if not B:
            return (n*n+1)//2
        res = []
        
        for i in range(n+1):
            for j in range(i):
                res.append(A[j: i])
        count = 0
        for ii in res:
            if sum(ii) < B:
                count += 1
        return count
