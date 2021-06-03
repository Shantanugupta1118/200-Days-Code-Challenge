# Github: Shantanugupta1118
# DAY 23 of DAY 100
# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import *


# First approach using heap nsmallest function
def kclosest(nums, k):
    return nsmallest(k, nums, key=lambda x:x[0]**2+x[1]**2 )

# Second Approach using Heappush and Heappushpop
"""
def kclosest(nums, k):
    max_heap = []
    for i in nums:
        if len(max_heap)<k:
            heappush(max_heap, [-(i[0]**2+i[1]**2), i])
        else:
            heappushpop(max_heap, [-(i[0]**2 + i[1]**2), i])
    # print(max_heap)
    return [pair for val, pair in max_heap]
"""

nums = [[1,3],[-2,2]]
k = 1
print(kclosest(nums, k))

nums = [[3,3],[5,-1],[-2,4]]
k = 2
print(kclosest(nums, k))