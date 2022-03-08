#  Day 141 of 200 Days
# 740. Delete and Earn


class Solution:
    def deleteNearn(self, nums):
        points = [0]*10001
        for i in range(len(nums)):
            points[nums[i]] += nums[i]
        
        for i in range(2, 10001):
            points[i] = max(points[i-2]+points[i], points[i-1])
        
        return points[10000]

print(Solution().deleteNearn([3,4,2]))
print(Solution().deleteNearn([2,2,2,3,3,3,4]))
        

