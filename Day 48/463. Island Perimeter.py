
# Github: Shantanugupta1118
# DAY 48 of DAY 100
# 463. Island Perimeter - Leetcode/DFS
# https://leetcode.com/problems/island-perimeter/


class Solution:
    def __init__(self):
        self.count = None
        
    def islandPerimeter(self, grid):
        self.count = 0
        def dfs(i, j):
            if (i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]==0):
                self.count += 1
                return
            if grid[i][j] == -1:
                return

            grid[i][j] = -1

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dfs(i, j)
                    break
        return self.count

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().islandPerimeter(grid))

grid = [[1]]
print(Solution().islandPerimeter(grid))

grid = [[1,0]]
print(Solution().islandPerimeter(grid))
