# Github: Shantanugupta1118
# DAY 69 of DAY 100
# Disjoint Union - GFG
# https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/1#


class Solution:
    def find(self, parent, x):
        if x == parent[x-1]:
            return x
        parent[x-1] = self.find(parent, parent[x-1])
        return parent[x-1]

    def unionSet(self, parent, x, y):
        a = self.find(parent, parent[x-1])
        b = self.find(parent, parent[y-1])
        if a!=b:
            parent[a-1] = b


for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [x for x in range(1, n+1)]
    str = input().strip().split()
    i = 0
    f = Solution()
    while i<len(str):
        if str[i] == 'FIND':
            print(f.find(arr, int(str[i+1])), end=" ")
            i += 2 
        elif str[i] == 'UNION':
            f.unionSet(arr, int(str[i+1]), int(str[i+2]))
            i += 3
    print()