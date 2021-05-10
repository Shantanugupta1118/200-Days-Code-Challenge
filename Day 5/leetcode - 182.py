# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 5 of DAY 100
# Leetcode 182 - Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/



# Solution:

# Run Time Complexity - O(n) linear time complexity
def main():
    nums = list(map(int, input().split()))
    nums = set(nums)
    mx = 0
    for n in nums:
        if n-1 not in nums:
            curr = n
            itr = 1
            while curr+1 in nums:
                curr += 1
                itr += 1
            mx = max(mx, itr)
    return mx
    print(mx)

main()










# def main():
#     nums = list(map(int, input().split()))
#     n = len(nums)
#     quickSort(nums, 0, n-1)
#     i = 0
#     m = 0
#     while i < n-1:
#         diff = abs(nums[i] - nums[i+1])
#         if diff!=0:
#             for j in range(i, n-1):
#                 if abs(nums[j] - nums[j+1]) == diff:
#                     temp = nums[i:j+2]
#                     m = max(m, len(temp))
#         i += 1
#     print(m)