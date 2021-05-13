# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 7 of DAY 100
# Leetcode 906 - Super Palindromes

# SOlution

from math import sqrt
def isPalind(n):
    return str(n) == str(n)[::-1]


def main():
    # l = input()
    # r = input()
    l, r = 40000000000000000, 50000000000000000
    # l, r = int(l), int(r)
    # if l==1: return 1
    count = 0
    i = int(sqrt(l))
    while i*i<=r:
        if isPalind(i) and isPalind(i*i):
            count += 1
        i += 1
    print(count)

main()