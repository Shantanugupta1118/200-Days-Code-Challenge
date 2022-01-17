# Github: Shantanugupta1118
# Day 100 of day 100
# 290. Word Pattern




class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_dc = {}
        if not len(pattern): return False
        if not len(s): return False
        if len(s.split()) != len(pattern): return False
        s = s.split(" ")

        for i in range(len(s)):
            if pattern[i] not in pat_dc and s[i] not in pat_dc.values():
                pat_dc[pattern[i]] = s[i]
                print(pat_dc[pattern[i]], pattern[i], s[i])
            else:
                if pattern[i] not in pat_dc and s[i] in pat_dc.values():
                    return False
                elif pattern[i] in pat_dc and s[i] not in pat_dc.values():
                    return False
                elif pat_dc[pattern[i]] != s[i]: return False
        return True

print(Solution().wordPattern("aaa", "aa aa aa aa"))
