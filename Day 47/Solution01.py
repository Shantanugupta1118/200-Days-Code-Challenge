class Juspay_Solution:
    def bfs_approach(self, graph, c, t):
        s, n, length_of_graph, count = 1, len(graph)-1, len(graph), 0
        distance, pred, color, x = [], [], [], []
        for _ in range(length_of_graph):
            distance.append(9999)
            pred.append(None)
            color.append('w')
        x.append(s)
        distance[s] = 0
        color[s] = 'g'
        while len(x) != 0:
            temp = x.pop(0)
            if temp == n: break
            count += 1
            color[temp] = 'b'
            for i in graph[temp]:
                if color[i] == 'w':
                    x.append(i)
                    color[i] = 'g'
                    distance[i] = distance[temp] + c 
                    pred[i] = temp
        return distance[n]

    def color_traverse(self, xx, t, c):
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
        return xx



n, m, t, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

xx = Juspay_Solution().bfs_approach(graph, c, t)
print(Juspay_Solution().color_traverse(xx, t, c))