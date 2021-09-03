# Github: Shantanugupta1118
# DAY 75 of DAY 100
# Diagonal Difference - Hackerrrank

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    right_diag = 0
    left_diag = 0
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                right_diag += arr[i][j]
            if (i == n - j - 1):
                left_diag += arr[i][j]
    return abs(left_diag - right_diag)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
