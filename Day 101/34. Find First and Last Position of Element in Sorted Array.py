# Github: Shantanugupta1118
# Day 101 of Day 200
# 34. Find First and Last Position of Element in Sorted Array


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        start, end = -1, -1
        
        '''
        l, r = 0, 0
        while l<=r:
            if nums[l] == target:
                start = l
            if nums[r] == target:
                end = r
            if not start:
                l += 1
            if not end:
                r += 1
         '''   
    
#       left--------------------
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
                        
#       right ------------------
        for i in reversed(range(len(nums))):
            if nums[i] == target:
                end = i
                break
            
        return [start, end]
        
