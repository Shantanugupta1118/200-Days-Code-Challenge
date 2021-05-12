# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 5 of DAY 100
# Leetcode 128 - Longest Consecutive Sequence
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

