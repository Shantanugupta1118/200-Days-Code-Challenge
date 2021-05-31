# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 20 of DAY 100
# 1046. Last Stone Weight - Leetcode
# https://leetcode.com/problems/last-stone-weight/

def LastStone(arr):
    while len(arr)>1:
        arr.sort()
        if arr[-1]==arr[-2]:
            arr = arr[:-2]
        else:
            arr[-1] -= arr[-2]
            del arr[-2]
    return arr if len(arr)==1 else 0


arr = list(map(int, input().split()))
print(*LastStone(arr))
