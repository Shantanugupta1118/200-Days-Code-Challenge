# Github: Shantanugupta1118
# DAY 28 of DAY 100
# Array 3 Pointer - InterviewBit/Google/Microsoft/Yahoo
# https://www.interviewbit.com/problems/array-3-pointers/


from sys import maxsize
class Solution:
    def minimize(self, A, B, C):
        p, q, r = len(A), len(B), len(C)
        intersect = maxsize
        temp1, temp2, temp3 = 0, 0, 0
        i, j, k = 0, 0, 0
        while i<p and j<q and k<r:
            mn = min(A[i], min(B[j], C[k]))
            mx = max(A[i], max(B[j], C[k]))
            if mx-mn < intersect:
                temp1, temp2, temp3 = i, j, k
                intersect = mx-mn
            if intersect==0:
                break
            if A[i] == mn:
                i += 1
            elif B[j] == mn:
                j += 1
            else:
                k += 1
        return max(abs(A[temp1] - B[temp2]), abs(B[temp2] - C[temp3]), abs(C[temp3] - A[temp1]))
                



A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 20]
print(Solution().minimize(A, B, C))
