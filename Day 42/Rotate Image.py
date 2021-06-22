# Github: Shantanugupta1118
# DAY 42 of DAY 100
# 48. Rotate Image    -  LeetCode
# https://leetcode.com/problems/rotate-image/



class Solution:
    def rotateimage(self, matrix):
        n = len(matrix)-1
        for i in range(0, len(matrix)):
            for j in range(i, n-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = temp


mat = [[5,1,9,11],
       [2,4,8,10],
       [13,3,6,7],
       [15,14,12,16]]
for i in mat:
    print(*i)
print()
Solution().rotateimage(mat)
for i in mat:
    print(*i)

