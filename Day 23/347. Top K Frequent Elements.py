# Github: Shantanugupta1118
# DAY 23 of DAY 100
# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter

def ktopElement(nums, k):
    occurrence = Counter(nums)
    occurrence = dict(sorted(occurrence.items(), key=lambda x:x[1], reverse=True))
    res = []
    for key, _ in occurrence.items():
        if k!=0:
            res.append(key)
            k -= 1
    return res


nums = list(map(int, input().split()))
k = int(input())
print(ktopElement(nums, k))