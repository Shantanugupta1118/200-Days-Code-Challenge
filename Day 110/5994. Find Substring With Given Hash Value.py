# Github: Shantanugupta1118
# DAY 110 of DAY 200
# 5994. Find Substring With Given Hash Value


class Solution:
    def res(self, s, pow, mod, k):
        ans = 0
        for i in range(abs(len(s)-k)):
            ans += ord(s[i])*(pow**i)
        return ans
    
    def subStringHash(self, s, power, mod, k, hashVal):
        for i in range(len(s)):
            for j in range(i, len(s)):
                if hashVal == self.res(s[i:j+1], power, mod, k):
                    return s[i+1:j+2]
                
print(Solution().subStringHash("leetcode", 7, 20, 2, 0))