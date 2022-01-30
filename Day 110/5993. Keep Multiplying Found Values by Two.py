# 5993. Keep Multiplying Found Values by Two


class Solution:
    def findFinal(self, nums, n):
        # res = []
        if n not in nums: return n
        while True:
            temp = n*2
            # print(n, temp)
            if temp in nums:
                n = temp
            else:
                n = temp
                break
        return n
    
print(Solution().findFinal([5,3,6,1,12], 3))