# Github: Shantanugupta1118
# DAY 14 of DAY 100
# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/


# solution

def solve(h):
    mx = 0
    # mid = len(h)//2
    n = len(h)
    for i in range(n-1 ):
        steps = 0
        for j in range(i, n):
            mx = max(mx, min(h[i], h[j])*steps)
            steps += 1
        #     print("in", mx, steps)
        # print(mx, steps)
    return mx

height = list(map(int, input().split()))
print(solve(height))