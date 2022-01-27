# Github: Shantanugupta1118
# DAY 108 of DAY 100
# 190. Reverse Bits

class Solution:
    def reverseBit(self, n):
        return int("{:032b}".format(n)[::-1], 2)
    

print(Solution().reverseBit(10100101000001111010011100))
