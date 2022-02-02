# Github: Shantanugupta1118
# DAY ___ of DAY 200
#


class Solution:
    def solve(self, n):
        if len(str(n)) == 1 or len(str(n)) == 0:
            return n
        ls = list(map(int, str(n)))
        while len(ls) != 1:
            ls = list(map(int, str(sum(ls))))            
        return ls[-1]
    
    
print(Solution().solve(38))

