# Github: Shantanugupta1118
# Day 134 of day 200
# 191. Number of 1 Bits


class Solution:
    # Method 1
    '''
    def Number1bits(self, n):
        return bin(n).replace("0b","").count('1')
    '''

    def Number1bits(self, n):
        return sum([1 if (1<<i)&n else 0 for i in range(32)])

print(Solution().Number1bits(11))
print(Solution().Number1bits(112445))
print(Solution().Number1bits(10))
