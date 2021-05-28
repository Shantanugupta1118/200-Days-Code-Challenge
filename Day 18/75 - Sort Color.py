# Github: Shantanugupta1118
# DAY 18 of DAY 100
# 75 - Sort Colors - Leetcode
# https://leetcode.com/problems/sort-colors/

def sort_colors(nums, target = 1):
    i, j, n = 0, 0, len(nums) - 1
    while j<=n:
        if nums[j] < target:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i+1, j+1
        elif nums[j] > target:
            nums[j], nums[n] = nums[n], nums[j]
            n-=1
        else:
            j += 1



nums = list(map(int, input().split()))
sort_colors(nums)
print(nums)