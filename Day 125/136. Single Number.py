# Github: Shantanugupta1118
# DAY 125 of DAY 200
# 136. Single Number

from collections import Counter 

class Solution:
    def solve(self, arr):
        num = Counter(arr)
        for k,v in num.items():
            if v==1: return k
    
    
print(Solution().solve([2,2,3]))

