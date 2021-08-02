# Github: Shantanugupta1118
# DAY 60 of DAY 100
# 1.-  Leetcode/August
#https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3836/


class Solution:
    def two_sum(self, arr, target):
        for i in range(len(arr)):
            if target - arr[i] in arr[i:]:
                for j in range(i+1,len(arr)):
                    if target - arr[i] == arr[j]:
                        return [i, j]
        return -1

arr = [3,3]
t = 6
print(Solution().two_sum(arr, t))
