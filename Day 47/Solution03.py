
class Juspay_Solution:
    def traverse(self, graph, visited, curr, path, stack, n):
        if curr==n-1:
            path.append(stack.copy())
            stack.pop()
            return path, stack
        else:
            visited[curr] = 1
            for ele in graph[curr]:
                if visited[ele] == 0:
                    stack.append(ele)
                    path, stack = self.traverse(graph, visited, ele, path, stack, n)
            stack.pop()
            return path, stack

    def duration_traverse(self, duratione, t, c):
        duration = 0
        l = len(path[0])
        for i in range(1,len(path)):
            if len(path[i])>l:
                l=len(path[i])
                break
        if l==len(path[0]): return -1
        else:
            for i in range(1, l):
                duration += c
                if i==l-1:
                    break
                else:
                    temp = duration//t
                    if temp%2==1:
                        duration = (temp+1)*t
            return duration


n, m, t, c = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

path, _ = Juspay_Solution().traverse(graph, visited, 0, [], [0], n)
path.sort(key=lambda x:len(x))
print(Juspay_Solution().duration_traverse(path, t, c))
