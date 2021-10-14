# Github: Shantanugupta1118
# DAY 87 of DAY 100



import time
from functools import lru_cache


#  --------------- NAIVE THEORY BASED ---------------
'''
class Solution:

    def check_factor(self, x, y):
        while x%y==0:
            x = x// y
        return x

    def isUgly(self, x):
        x = self.check_factor(x, 2)
        x = self.check_factor(x, 3)
        x = self.check_factor(x, 5)
        return 1 if x==1 else 0
        
    def solve(self):
        n = int(input())
        numbers = []
        count, i = 1, 1
        print(time.time())
        while n > count:
            i += 1
            numbers.append(i)
            if self.isUgly(i):
                count += 1
        print(time.time())
        return numbers[-1]
            
print(Solution().solve())
'''


# ------------ Dynamic Programming Based -------------

class Solution:
    def solve(self, n):
        num = [0]*n
        div_2, div_3, div_5 = 2, 3, 5

        for i in range(n):
            

n = int(input())
print(Solution().solve(n))



