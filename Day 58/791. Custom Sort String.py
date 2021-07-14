# Github: Shantanugupta1118
# DAY 58 of DAY 100
# 791. Custom Sort String   -  LeetCode
# https://leetcode.com/problems/custom-sort-string/

from collections import  Counter
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        cnt = Counter(str)
        ans = ""
        for c in order:
            if cnt[c] > 0:
                ans += cnt[c] * c
                del cnt[c]
        for c, v in cnt.items():
            ans += v * c
        return ans

print(Solution().customSortString("cbagf", "abcd"))