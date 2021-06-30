# Github: Shantanugupta1118
# DAY 42 of DAY 100
# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/


import math
class Solution:
    def minWindow(self, s, t):
        count = {}
        for char in t:
            count[char] = count.get(char, 0) + 1
        match = 0
        min_l = math.inf
        res = ""
        window_start = 0
        for window_end in range(len(s)):
            r_char = s[window_end]
            if r_char in count:
                count[r_char] -= 1
                if count[r_char] == 0:
                    match += 1
            while match == len(count):
                if window_end - window_start + 1 < min_l:
                    min_l = window_end - window_start + 1
                    res = s[window_start : window_end + 1]
                r_char = s[window_start]
                if r_char in count:
                    count[r_char] += 1
                    if count[r_char] > 0:
                        match -= 1
                window_start += 1
        return res    


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))