# Github: Shantanugupta1118
# DAY 30 of DAY 100
# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1 
        print(d)
        for k, v in d.items():
            print(k, v)
            if v>2:
                c = v
                while c>2:
                    nums.remove(k)
                    c -= 1
        return nums, len(nums)
    
nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates(nums))