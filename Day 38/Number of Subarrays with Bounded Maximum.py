# Github: Shantanugupta1118
# DAY 38 of DAY 100
# Number of Subarrays with Bounded Maximum - Leetcode/June 21
# https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/

import copy

class solution:
    def solve(self, nums, left, right):
        si, ei = 0, 0
        prev, ans = 0, 0
        while ei<len(nums):
            if nums[ei] <=  right and nums[ei] >= left:
                prev = ei-si+1
                ans += prev
            elif nums[ei] < left:
                ans += prev
            else:
                si = ei+1
                prev = 0
            ei += 1
        return ans



# num = list(map(int, input().split()))
# left = int(input())
# right = int(input())
num = [2,9,2,5,6]
left, right = 2, 8
print(solution().solve(num,left, right))