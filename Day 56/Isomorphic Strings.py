# Isomorphic Strings - Leetcode/July
# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3811/


from collections import  defaultdict
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


s = "egg"
t = "add"
print(Solution().Isomorphic(s, t))
s = "paper"
t = "title"
print(Solution().Isomorphic(s, t))
s = "foo"
t = "bar"
print(Solution().Isomorphic(s, t))