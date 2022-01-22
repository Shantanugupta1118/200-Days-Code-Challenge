# Github: Shantanugupta1118
# DAY 104 of DAY 100
# 1510. Stone Game IV


import math

class Solution:
    def __init__(self):
        self.cache = {}
    
    def winnerSquareGame(self, n: int) -> bool:
        if not n: return False
        if n in self.cache:
            return self.cache[n]
        i = int(math.sqrt(n))
        while i >= 1:
            if not self.winnerSquareGame(n - i*i):
                self.cache[n] = True
                return self.cache[n]
            i -= 1
        self.cache[n] = False
        return self.cache[n]
    
print(Solution().winnerSquareGame(3))