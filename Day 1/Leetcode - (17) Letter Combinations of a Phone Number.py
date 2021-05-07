# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 1 of DAY 100
# Leetcode - 17. Letter Combination of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Test Case:
    # 1
        # digits = '23'
        # combinations = "ad","ae","af","bd","be","bf","cd","ce","cf"

# Solution -----

# Approach 1: using Array list
# Run time complexity: O(n) - linear time
from collections import deque

key = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

def combination(number):
    number = list(map(int, number))
    len_n = len(number)
    l = []
    q = deque()
    q.append("")
    while len(q)!=0:
        s = q.pop()
        if len(s)==len_n: l.append(s)
        else:
            for n in key[number[len(s)]]: q.append(s+n)
    return l[::-1]

digits = input()
print(combination(digits))






# key_alphabets = {'2':'abc',
#                 '3':'def',
#                 '4':'ghi',
#                 '5':'jkl',
#                 '6':'mno',
#                 '7':'pqrs',
#                 '8':'tuv',
#                 '9':'wxyz'}

