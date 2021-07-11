# Github: Shantanugupta1118
# DAY 54 of DAY 100
# Numbers of length N and value less than K  - InterviewBit
# https://www.interviewbit.com/problems/numbers-of-length-n-and-value-less-than-k/


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

        
# A = [ 0, 2, 3, 4, 5, 7, 8, 9 ]
# B = 5
# C = 86587
A = [0,1,5]
B = 1
C = 2
print(Solution().solve(A, B, C))