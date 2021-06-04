# Github: Shantanugupta1118
# DAY 23 of DAY 100
# Minimum Loss - Hackerrank
import sys
def minimumloss(arr, n):
    mini = sys.maxsize
    for i in range(n-1):
        for j in range(i,n):
            if arr[i] > arr[j] and arr[i]-arr[j] < mini:
                mini = min(mini, arr[i] - arr[j])
    return mini


n = int(input())
arr = list(map(int, input().split()))
print(minimumloss(arr, n))