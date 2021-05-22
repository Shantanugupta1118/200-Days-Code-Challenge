# Github: Shantanugupta1118
# DAY 14 of DAY 100
# Non-Divisible Subset - Hackerrank
# https://www.hackerrank.com/contests/hackathon-tr-21may/challenges/absolute-permutation

# solution

def main():
    n, k = map(int, input().split())
    if k == 0:
        print(*(range(1, n+1)))
    elif (n/k)%2!=0.0:
        print(-1)
    else:
        arr = []
        for i in range(1, n, 2*k):
            d = list(range(i, i+k*2))
            arr += d[k:]+d[:k]
        print(*arr)

for _ in range(int(input())):
    main()