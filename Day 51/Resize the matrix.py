# Github: Shantanugupta1118
# DAY 51 of DAY 100
# Reshape the Matrix
# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3803



class Solution:
    def resize_mat(self, mat, r, c):
        if len(mat)*len(mat[0]) != r*c:
            return mat
        new_mat = []
        for i in mat:
            new_mat.extend(i)
        res = []
        temp = []
        for i in range(r):
            for j in range(c):
                temp.append(new_mat[0])
                del new_mat[0]
            res.append(temp)
            temp = []
        return res


mat = [[1,2],[3,4]]
r, c = 1, 4
print(*Solution().resize_mat(mat, r, c))