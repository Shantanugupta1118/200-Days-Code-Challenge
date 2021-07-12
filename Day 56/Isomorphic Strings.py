# Github: Shantanugupta1118
# DAY 56 of DAY 100
# 205. Isomorphic Strings - Leetcode/July
# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3811/


# ----- Passed 31/39 Test Cases --------------
#  Failed for TC
#    IP:
#           s = "BADC", t = "BABA"
#   OP:
#           Expected:   True, returned False
"""
class Solution:
    def Isomorphic(self, s, t):
        dic = {}
        interrupted = False
        for i in range(len(s)):
            if s[i] not in dic and t[i] not in dic:
                dic[s[i]] = t[i]
            elif s[i] in dic:
                if dic[s[i]] != t[i]:
                    interrupted = True
                    break
                elif dic[s[i]] == t[i]:
                    continue
        if interrupted:
            return False
        return True
"""


class Solution:
    def Isomorphic(self, s, t):
        return [s.find(i) for i in s] == [t.find(i) for i in t]


s = "egg"
t = "add"
print(Solution().Isomorphic(s, t))
s = "paper"
t = "title"
print(Solution().Isomorphic(s, t))
s = "foo"
t = "bar"
print(Solution().Isomorphic(s, t))