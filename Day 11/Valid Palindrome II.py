# Github: Shantanugupta1118
# DAY 11 of DAY 100
# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/


# Solutions

"""def validate_pal(s, counter=1):
    i, j = 0, len(s)-1
    while i<j and s[i]==s[j]:
        i+=1
        j-=1
    if i>=j: return True
    if counter==0: return False
    return validate_pal(s[i+1:j+1], 0) or validate_pal(s[i:j], 0)


string = input()
print(validate_pal(string))
"""


class Solution:
    def validPalindrome(self, s, counter=1) -> bool:
        i, j = 0, len(s)-1
        while i<j and s[i]==s[j]:
            i+=1
            j-=1
        if i>=j: return True
        if counter==0: return False
        return self.validPalindrome(s[i+1:j+1], 0) or self.validPalindrome(s[i:j], 0)

string = input()
Lc = Solution()
print(Lc.validPalindrome(string))