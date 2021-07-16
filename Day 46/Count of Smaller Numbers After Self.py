# Github: Shantanugupta1118
# DAY 46 of DAY 100
# Count of Smaller Numbers After Self - Leetcode/june21
# https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3792/




from bisect import bisect_left

class solution:
    def count_small(self, nums):
        res = [0]*len(nums)
        sorted_list = []
        for i, num in enumerate(reversed(nums)):
            l = bisect_left(sorted_list, num)
            sorted_list.insert(l, num)
            res[i] = l
        
        return reversed(res)


num = [[5, 2, 6, 1], [6, 4, 1, 8, 2, 3, 7 ,9]]
for nums in num:
    print(solution().count_small(nums))
