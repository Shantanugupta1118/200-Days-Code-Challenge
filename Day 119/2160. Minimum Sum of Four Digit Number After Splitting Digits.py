# Github: Shantanugupta1118
# DAY 119 of DAY 200
# 2160. Minimum Sum of Four Digit Number After Splitting Digits



class Solution:
    def solve(self, n):
        '''
            #  First Approach ---
        n = list(map(int, str(n)))
        new1 = [min(n)*10+max(n)]
        n.remove(max(n))
        n.remove(min(n))
        new2 = [min(n)*10+max(n)]
        return new1[-1]+new2[-1]
        '''
        
        #  Second Approach ----
        n = list(map(int, str(n)))
        n.sort()
        return (n[0]+n[1])*10+n[2]+n[3]
    
print(Solution().solve(2932))
print(Solution().solve(4009))

