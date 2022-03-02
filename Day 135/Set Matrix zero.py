# Github: Shantanugupta1118
# Day 135 of day 200
# Set Matrix Zero


class Solution:
    def setMatZero(self, mat):
        zero_idx = []
        col, row = len(mat), len(mat[0])
        for i in range(col):
            for j in range(row):
                if mat[i][j] == 0:
                    zero_idx.append([i,j])
        
        # Row set Zeros----
        for zeros in zero_idx:
            for i in range(row):
                mat[zeros[0]][i] = 0

        # Column set zeros -----
        for zeros in zero_idx:
            for i in range(col):
                mat[i][zeros[1]] = 0
        return mat



print(*Solution().setMatZero([[1,1,1],[1,0,1],[1,1,1]]))
print(*Solution().setMatZero([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))