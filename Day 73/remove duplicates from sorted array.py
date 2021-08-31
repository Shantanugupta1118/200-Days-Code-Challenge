# Github: Shantanugupta1118
# DAY 73 of DAY 100
# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/



class solution:
    def removeDuplicates(self, nums):
        if len(nums) is None:
            return 0
        if len(nums)==0 or len(nums)==1:
            return len(nums)

        length_new = len(nums)
        count = len(nums)-1
        while count>0:
            if nums[count] == nums[count-1]:
                del nums[count]
                length_new -= 1
            count -= 1
        return length_new

print(solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))