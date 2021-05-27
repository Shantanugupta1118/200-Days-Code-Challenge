# Github: Shantanugupta1118
# DAY 12 of DAY 100
# 32. Longest Valid Parentheses
#  https://leetcode.com/problems/longest-valid-parentheses/


# Solution:

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0: return 0
        stack = []
        count_validate = 0
        for i in s:
            if i == ')' and len(stack)!=0:
                if '(' == stack[0]:
                    count_validate += 2
                    stack.pop()
            elif i=='(':
                stack.append(i)
        return count_validate

LC = Solution()
string = input()
print(LC.longestValidParentheses(string))