# Github: Shantanugupta1118
# DAY 55 of DAY 100
# 4. Median of Two Sorted Arrays  - Leetcode
# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        new_list = sorted(nums1+nums2)
        n = len(new_list)
        if n%2!=0:
            return float(new_list[n//2])
        
        else:
            mid1 = new_list[(n-1)//2]
            mid2 = new_list[(n+1)//2]
            return 0.5*(mid1+mid2)



nums1 = [1,3,6,5,4]
nums2 = [2,5,8,9,12]
print(Solution().findMedianSortedArrays(nums1, nums2))