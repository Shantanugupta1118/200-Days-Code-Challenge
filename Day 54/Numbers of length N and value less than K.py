# Github: Shantanugupta1118
# DAY 54 of DAY 100
# Numbers of length N and value less than K  - InterviewBit
# https://www.interviewbit.com/problems/numbers-of-length-n-and-value-less-than-k/


# -------- O(B*N^2) ------------
"""
import copy
class Solution:
    def solve(self, A, B, C):
        res = []
        if B==1:
            count = 0
            for i in A:
                if i<C:
                    count += 1      
            return count
        i = 0
        temp = A.copy()
        while i!=B:
            i += 1
            for j in range(len(temp)):
                for k in range(len(temp)):
                    if int(str(temp[j])+str(temp[k])) < C:
                        res.append(int(str(temp[j])+str(temp[k])))
                    else:
                        res = list(set(res))
                        break
            temp = res

        print(res)
        count = 0
        for i in res:
            if len(str(i))==B:
                count+=1
        return count

"""     


#  ----- Dynamic Approach  O(N) --------------
MAX = 10
class Solution:
    def solve(self, A, B, C):
        def vector_helper(N):
            digit = []
            while (N != 0):
                digit.append(N % 10)
                N = N // 10
            if (len(digit) == 0):
                digit.append(0)
            digit = digit[::-1]
            return digit

        d, d2 = 0,0
        digit = vector_helper(C)
        d = len(A)
        if (B > len(digit) or d == 0):
            return 0
        elif (B < len(digit)):
            if (A[0] == 0 and B != 1):
                return (d - 1) * pow(d, B - 1)
            else:
                return pow(d, B)
        else :
            dp=[0 for i in range(B + 1)]
            lower=[0 for i in range(MAX + 1)]
            for i in range(d):
                lower[A[i] + 1] = 1
            for i in range(1, MAX+1):
                lower[i] = lower[i - 1] + lower[i]
    
            flag = True
            dp[0] = 0
            for i in range(1, B+1):
                d2 = lower[digit[i - 1]]
                dp[i] = dp[i - 1] * d
                if (i == 1 and A[0] == 0 and B != 1):
                    d2 = d2 - 1
                if (flag):
                    dp[i] += d2
                flag = (flag & (lower[digit[i - 1] + 1] == lower[digit[i - 1]] + 1))
            
            return dp[B]




A = [ 0, 2, 3, 4, 5, 7, 8, 9 ]
B = 5
C = 86587
print(Solution().solve(A, B, C))
A = [0,1,5]
B = 1
C = 2
print(Solution().solve(A, B, C))