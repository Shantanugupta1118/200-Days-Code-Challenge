# Github ID: Shantanugupta1118
# Day 127 of Day 200
# Minimize deviation in array  -  Leetcode


from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if num%2: nums[i]=2*num
        nums=SortedList(nums)
        Max=nums[-1]
        ans=sys.maxsize
        while Max%2==0:
            diff=Max-nums[0]
            nums.pop()
            nums.add(Max//2)
            Max=nums[-1]
            ans=min(ans,Max-nums[0])
        return min(ans,Max-nums[0])
