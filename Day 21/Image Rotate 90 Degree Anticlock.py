# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 21 of DAY 100
# GFG - Image Rotate 90 degree anticlockwise
# https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

n = int(input())
mat, temp = [], []
count = 1
for row in range(n):
    for data in range(1,n+1):
        temp.append(count)
        count += 1
    mat.append(temp)
    temp = []

for row in reversed(range(n)):
    for col in range(n):
        print(mat[col][row], end=' ')
    print()
