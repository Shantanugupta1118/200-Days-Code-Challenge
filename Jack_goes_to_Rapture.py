# Github: Shantanugupta1118
# DAY 78 of DAY 100

from collections import defaultdict
import heapq as H

class graph:
    def __init__(self):
        self.g = defaultdict(list)
    def add(self, a, b, c):
        self.g[a] += [(a, b, c)]
        self.g[b] += [(b, a, c)]
    def min_cost(self, s, e):
        h = [(0, s)]
        closed = set()
        while h:
            cost, n = H.heappop(h)
            if n == e:
                return cost
            if n not in closed:
                closed.add(n)
                for _, nb, c in self.g[n]:
                    H.heappush(h, (max(c, cost), nb))
        return "NO PATH EXISTS"

g_nodes, g_edges = map(int, input().split())

g_from = [0] * g_edges
g_to = [0] * g_edges
g_weight = [0] * g_edges

g = graph()
for g_itr in range(g_edges):
    a, b, c = map(int, input().split())
    g.add(a, b, c)

print(g.min_cost(1, g_nodes))
