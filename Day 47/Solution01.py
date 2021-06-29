class Juspay_Solution:
    def bfs_approach(self, graph, c, t):
        pass




n, m, t, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
xx = Juspay_Solution().bfs_approach(graph, c, t)

connect = [None]
for _ in range(t):
    connect.append('g')
for i in range(t, xx+1):
    if i == 0: continue
    if (i//t)%2 == 0: connect.append('g')
    else: connect.append('r')
for i in range(0, xx, c):
    if connect[i] == 'r': 
        xx += (connect[i+1:].index('g'))
print(xx)