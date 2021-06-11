# Github: Shantanugupta1118
# DAY 28 of DAY 100
# Array 3 Pointer - InterviewBit/Google/Microsoft/Yahoo
# https://www.interviewbit.com/problems/array-3-pointers/


class Solution:
    def minimize(self, A, B, C):
        i, j, k = len(A), len(B), len(C)
        mx = max(i, j, k)
        if len(A)!=mx:
            while len(A)!=mx:
                A.append(0)
        if len(B) != mx:
            while len(B)!=mx:
                B.append(0)
        if len(C)!=mx:
            while len(C)!=mx:
                C.append(0)
        i=j=k=mx
        while mx!=0:
            
                



A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 20]
print()
