# Github: Shantanugupta1118
# DAY 45 of DAY 100
# 962. Maximum Width Ramp -  LeetCode
# https://leetcode.com/problems/maximum-width-ramp/


import sys


#  Brute Force -- O(N^2)
'''
class solution:
    def max_width_ramp(self, nums):
        max_width = -sys.maxsize 
        
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                if nums[start] <= nums[end]:
                    max_width = max(max_width, end-start)
        return max_width
'''

class solution:
    def max_width_ramp(self, nums):
        store = {}
        for i in range(len(nums)):
            x = nums[i]
            if x in store:
                store[x].append(i)
            else:
                store[x] = [i]
        
        mini, maxi = [float('inf')], [float('-inf')]
        for x in sorted(store.keys()):
            mini.append(min(mini[-1], min(store[x])))
        for x in sorted(store.keys(), reverse=True):
            maxi.append(max(mini[-1], max(store[x])))
        
        maxi = maxi[::-1][:-1]
        mini = mini[1:]

        p = 0
        ans = float('-inf')
        while p<len(mini):
            ans = max(ans, maxi[p]-mini[p])
            p+=1
        return ans



nums = list(map(int, input().split()))
print(solution().max_width_ramp(nums))