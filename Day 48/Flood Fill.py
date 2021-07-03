# Github: Shantanugupta1118
# DAY 48 of DAY 100
# 733. Flood Fill -  LeetCode/DFS
# https://leetcode.com/problems/flood-fill/



class Solution:
    def flood_fill(self, image, sr, sc, new_color):
        row, col = len(image), len(image[0])
        color = image[sr][sc]

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = new_color
                if r>=1: dfs(r-1, c)
                if r+1<row: dfs(r+1, c)
                if c>=1: dfs(r, c-1)
                if c+1<col: dfs(r, c+1)

        if color == new_color:
            return image
        dfs(sr, sc)
        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc = 1, 1
newColor = 2
print(Solution().flood_fill(image, sr, sc, newColor))