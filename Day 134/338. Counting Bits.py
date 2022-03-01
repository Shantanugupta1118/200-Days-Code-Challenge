# Github: Shantanugupta1118
# Day 134 of day 200
# 338. Counting Bits



class Solution:
    def countbits(self, n):
        bits = [0]
        for i in range(1,n+1):
            bits.append(1+bits[i&i-1])
        return bits

print(Solution().countbits(5))
print(Solution().countbits(10))
print(Solution().countbits(2))