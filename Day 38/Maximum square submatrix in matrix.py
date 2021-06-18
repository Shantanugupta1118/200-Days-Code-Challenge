# Github: Shantanugupta1118
# DAY 38 of DAY 100
# Maximum square submatrix in matrix - GfG




def findLargestSquare(M, m, n, maxsize):
    if m == 0 or n == 0:
        if maxsize != 0:
            return M[m][n], max(maxsize, M[m][n])
        for i in range(m + 1):
            if M[i][n] == 1:
                return 1, 1
        for j in range(n + 1):
            if M[m][j] == 1:
                return 1, 1
        return 0, 0
    left, maxsize = findLargestSquare(M, m, n - 1, maxsize)
    top, maxsize = findLargestSquare(M, m - 1, n, maxsize)
    diagonal, maxsize = findLargestSquare(M, m - 1, n - 1, maxsize)
    size = 1 + min(min(top, left), diagonal) if M[m][n] else 0
    
    return size, max(maxsize, size)


M = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]

maxsize = findLargestSquare(M, len(M) - 1, len(M[0]) - 1, 0)
print(maxsize[1])