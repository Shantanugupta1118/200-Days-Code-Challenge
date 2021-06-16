# username: shantanugupta1118
# Day 36 of 100 Days
# Jim and Order - Hackerrank


class Solution:
    def icecream(self, k, cost):
        for i in range(len(cost)-1):
            for j in range(len(cost)):
                if i!=j and cost[i]+cost[j]==k:
                    return i+1,j+1

for _ in range(int(input())):
    m = int(input())
    n = int(input())
    cost = list(map(int, input().split()))
    res = Solution().icecream(m, cost)
    print("{0} {1}".format(res[0],res[1]))