# Github: Shantanugupta1118
# DAY 27 of DAY 100
# Longest Commont Prefix - InterviewBit/Google
# https://www.interviewbit.com/problems/longest-common-prefix/


class Solution:
    def commonstring(self, s):
        if not s:
            return ""
        for i in range(len(s[0])):
            for x in s[1:]:
                if i>=len(x) or x[i] != s[0][i]:
                    return s[0][:i]
        return s[0]


arr = ["abab", "ab", "abcd"]
print(Solution().commonstring(arr))