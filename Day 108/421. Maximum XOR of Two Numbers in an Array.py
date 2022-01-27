# Github: Shantanugupta1118
# DAY 108 of DAY 100
#421. Maximum XOR of Two Numbers in an Array


class Solution:
    '''
        Partial Accepted: TLE - 31/41
        Brute Force
    '''
    '''
    def maxXor(self, nums):
        mx = -999
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if mx < nums[i]^nums[j]:
                    mx = nums[i]^nums[j]
        return mx
    '''
    
    
    '''
        Full Accepted:
            Bit Manipulation Approach ---
    '''
    def maxXor(self, nums):
        res = 0
        for i in reversed(range(0,32)): 
            pref = set([num>>i for num in nums])
            print(pref, i, end=' ')
            res <<= 1
            x = res+1
            for pre in pref:
                if x^pre in pref:
                    res = x
                    break
            print(res)
        return res
        
        
    
print(Solution().maxXor([3,10,5,25,2,8]))
print(Solution().maxXor([14,70,53,83,49,91,36,80,92,51,66,70]))