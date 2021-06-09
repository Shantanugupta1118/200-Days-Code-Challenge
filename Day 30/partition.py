# Github: Shantanugupta1118
# DAY 29 of DAY 100
# Partition - InterviewBit
# https://www.interviewbit.com/problems/partitions/


class Solution:
    def solve(self, n, A):
        total = sum(A)
        if total%3!=0:
            return 0
            
        partition = total//3
        a = []
        sum1 = 0
        for i in range(n-2):
            sum1 += A[i]
            if sum1 == partition:
                a.append(i+1)
        count = 0
        for i in range(len(a)):
            ssum = 0
            for j in range(a[i], n-1):
                ssum += A[j]
                if ssum==partition:
                    count += 1
        return count

A = [1, 2, 3, 0, 3]
print(Solution().solve(len(A), A))