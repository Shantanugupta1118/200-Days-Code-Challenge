# Github: Shantanugupta1118
# DAY 56 of DAY 100
# A. AquaMoon and Strange Sort -- Codeforces
# https://codeforces.com/contest/1545/problem/A


for  _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = False
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")