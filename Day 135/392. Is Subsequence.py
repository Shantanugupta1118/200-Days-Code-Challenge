# Github: Shantanugupta1118
# Day 135 of day 200
# 392. Is Subsequence


class Solution:
    def isSubsequence(self, s, t):
            flag = False
            i = 0
            for j in range(len(t)):
                if i<len(s) and s[i] == t[j]:
                    i += 1
            if i==len(s): return True
            return False


print(Solution().isSubsequence("abc", "axcbsfsdjc"))
print(Solution().isSubsequence("yqhac", "cadjdciqx"))