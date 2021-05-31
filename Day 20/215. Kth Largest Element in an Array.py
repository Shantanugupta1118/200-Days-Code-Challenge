# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 20 of DAY 100
# 215. Kth Largest Element in an Array - Leetcode
# https://leetcode.com/problems/kth-largest-element-in-an-array/


from heapq import *

''' First Approach without inbuilt fnc '''
'''
def k_largest(arr, k):
    heap = []
    for i in arr:
        heappush(heap, -i)
    for i in range(k):
        a = heappop(heap)
    return a*-1
'''


''' Second Approach using built in fnc'''
def k_largest(arr, k):
    heapify(arr)
    return nlargest(k, arr)[-1]


arr = list(map(int, input().split()))
k = int(input())
print(k_largest(arr, k))