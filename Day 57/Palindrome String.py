# Github: Shantanugupta1118
# DAY 57 of DAY 100
# Palindrome String   -  InterviewBit
# https://www.interviewbit.com/old/problems/palindrome-string/


class Solution:
    def isPalindrome(self, A):
        lst=[]
        for i in A.lower():
            if ord(i)>=97 and ord(i)<=102 or (ord(i)>=48 and ord(i)<=57):
                lst.append(i)
        n=len(lst)
        if lst[::]==lst[::-1]:
            return 1
        else:
            return 0


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))