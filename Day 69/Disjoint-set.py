# Github: Shantanugupta1118
# DAY 69 of DAY 100

class Solution:
    def solve(self, n, k, queries):
        arr = {}
        res = []
        for i in range(1,n+1):
            arr[i] = i
        for query in queries:
            if query[0] == 'find':
                res.append(arr[query[1]])
            else:
                arr[query[1]] = arr[query[2]]
        return res

for _ in range(int(input())):
    # N, K = map(int, input().split())
    N, K = 5, 4
    query = [['find',4],['find',1],['unionSet',3,1],['find',3]]
    print(Solution().solve(N, K, query))