# Github: Shantanugupta1118
# DAY 97 of DAY 100
# 452. Minimum Number of Arrows to Burst Balloons


import collections

class Solution:
    def deleteAndEarn(self, nums):
        
        c = collections.Counter(nums)
        
        keys = sorted(c.keys())
        prev = 0
        ans = cur = c[keys[0]] * keys[0]
        for i in range(1, len(keys)):
            if keys[i] == keys[i-1] + 1:
                prev, cur = cur, max(cur, prev + keys[i] * c[keys[i]])
            else:    
                prev, cur = cur, cur + keys[i] * c[keys[i]]
            ans = max(ans, cur)
        return ans