# SOlution First

from collections import defaultdict
class Juspay_solution:
    def solution(self):
        visited = defaultdict(list) 
        def dfs_approach(s, e):
            if s==e: return True
            visited[s] = 1
            for x in adj[s]:
                if not visited[x]:
                    if dfs_approach(x, e):
                        return True

            
        n = int(input())
        participants = []
        for i in range(n):
            participants.append(int(input()))
        no_of_adjacent = int(input())
        adj = defaultdict(list) 
        for i in range(no_of_adjacent):
            x, y = map(int, input().split())
            adj[x].append(y)
        n1 = int(input())
        n2 = int(input())
        if dfs_approach(n1, n2):
            return 1
        else:
            return 0
        


print(Juspay_solution().solution())




# 4
# 2
# 5
# 7
# 9
# 4
# 2 9
# 7 2
# 7 9
# 9 5
# 7
# 9