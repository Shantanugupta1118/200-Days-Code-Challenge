# Github: Shantanugupta1118
# DAY 13 of DAY 100
# Non-Divisible Subset - Hackerrank
# https://www.hackerrank.com/contests/hackathon-tr-21may/challenges/non-divisible-subset


# solution

def main():
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    count = [0]*k
    for itr in ls:
        count[itr%k] += 1
    res = 0
    for i in range(1, (k+1)//2):
        res += max(count[i], count[k-i])
    if k%2==0 and count[k//2]: res +=1
    if count[0]: res +=1
    print(res)

main()