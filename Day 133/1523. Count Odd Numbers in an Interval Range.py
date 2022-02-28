# Github: Shantanugupta1118
# Day 133 of day 200
# 1523. Count Odd Numbers in an Interval Range


import math
class Solution:
    def countOdd(self, low, high):
        s = math.floor((high-low)/2)
        if low%2==0 and high%2==0: 
            pass
        else:
            s += 1
        return s


print(Solution().countOdd(21, 22))
print(Solution().countOdd(3, 7))