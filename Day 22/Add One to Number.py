# Github: Shantanugupta1118
# DAY 22 of DAY 100
# Add One to Number
# interviewbit.com/problems/add-one-to-number/


class Solution:
    def plusOne(self, A):
        '''First Approach - Dynamic'''
        '''
        A.reverse()
        carry = 1
        for i in range(len(A)):
            A[i] += int(carry)
            carry = 0
            if len(str(A[i]))>1:
                carry = str(A[i])[0]
                A[i] = int(str(A[i])[1])
            else:
                break
        if carry:
            A.append(int(carry))
        return A[::-1]
        '''
        
        '''Second Approach - Brute Force'''
        A = list(map(str, A))
        n = int("".join(A))
        n += 1
        N = list(map(int, str(n)))
        return N



num = list(map(int, input().split()))
print(Solution().plusOne(num))