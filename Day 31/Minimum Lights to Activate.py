# Github: Shantanugupta1118
# DAY 31 of DAY 100
# Topic: Array - Problem
# Minimum Lights to Activate - InterviewBit/Directi
# https://www.interviewbit.com/courses/programming/topics/arrays/


class solution:
    def solve(self, A, B):
        i, n, bulb = 0, len(A), 0
        while i < n:
            flag = False
            j = min(i+B-1, n-1)
            while j>=i-B+1 and j<n and j>0:
                flag = True
                bulb += 1
                i = j + B
                break
            j -= 1
            if not flag:
                return -1
        return bulb

A = [0, 0, 1, 1, 1, 0, 0, 1]
B = 3
print(solution().solve(A, B))