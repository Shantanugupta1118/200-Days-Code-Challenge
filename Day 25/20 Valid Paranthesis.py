# Github: Shantanugupta1118
# DAY 25 of DAY 100
# 20 Valid Parantheses - LeetCode/Juspay
# https://leetcode.com/problems/valid-parentheses/


def validate_parantheses(s):
    stack =[]
    open_brac = ['[','{','(']
    for i in s:
        if i in open_brac:
            stack.append(i)
        elif len(stack)!=0 and ((i == '}' and stack[-1]=='{') or (i == ']' and stack[-1] == '[') or (i == ')' and stack[-1] == '(')):
            stack.pop()
        else:
            return False
    return True



string = input()
print(validate_parantheses(string))