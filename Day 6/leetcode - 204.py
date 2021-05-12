# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 6 of DAY 100
# Leetcode - 204 - Count Primes
# https://leetcode.com/problems/count-primes/

# solution


def main():
    count = 0
    lower = 1
    upper = int(input())
    prime = [True for i in range(upper+1)]
    p = 2
    while p*p <= upper:
        if prime[p] == True:
            for i in range(p*p, upper+1, p):
                prime[i] = False
        p += 1
    for p in range(2, upper+1):
        if prime[p]: count += 1
    print(count)

main()