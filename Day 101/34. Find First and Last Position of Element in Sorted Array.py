# Github: Shantanugupta1118
# Day 101 of Day 200
# 34. Find First and Last Position of Element in Sorted Array


class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0: return [-1, -1]
       # Single Pass ---------- O(n)
        l, r = 0, len(nums)-1
        while l<=r:
            if nums[l] == nums[r] ==  target:
                return [l,r]
            if nums[r] != target:
                r -= 1
            if nums[l]!=target:
                l += 1
           
    '''
        # Multiple Pass --------  O(2n)

        start, end = -1, -1
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
        '''

print(Solution().searchRange([3,5,3,2,1,4,5,6,7,8,4,3,2], 4))
