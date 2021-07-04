

class Juspay_solution:
    def solution(self):
        participants = {}
        visited = {}
        s = set()
        def dfs_approach():
            pass
        n = int(input())
        for i in range(n):
            temp = int(input())
            participants[temp] = []
            visited[temp] = [False, 10^9]


print(Juspay_solution().solution())


'''
4
2
5
7
9
4
2 9 2
7 2 3
7 9 7
9 5 1
7
9

-> 5
'''