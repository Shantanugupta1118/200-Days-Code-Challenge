# Github: Shantanugupta1118
# DAY 11 of DAY 100
# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/


def is_palind(s):
    s = ''.join(e.lower() for e in string if e.isalnum())
    print(s)
    return s==s[::-1]
string = input()
print(is_palind(string))