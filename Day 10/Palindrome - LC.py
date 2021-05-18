# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 10 of DAY 100
# LC - Palindrome  
# https://leetcode.com/problems/palindrome-number/submissions/


# Short approach
"""
def is_palind(n):
    return str(n) == str(n)[::-1]


n = int(input())
print(is_palind(n))"""


def is_palind(n):
    s = ''
    for i in reversed(str(n)):
        s += i
    return str(n)==s


n = int(input())
print(is_palind(n))