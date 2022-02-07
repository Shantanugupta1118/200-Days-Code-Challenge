# Github: Shantanugupta1118
# DAY 389 of DAY 200
# 389. Find the Difference



class Solution:
    def solve(self, s, t):
        for i in s:
            if i in t:
                t = t.replace(i, "", 1)
        return t
    
    
print(Solution().solve("abcd", "abcde"))
print(Solution().solve("", "y"))
print(Solution().solve("a", "aa"))
