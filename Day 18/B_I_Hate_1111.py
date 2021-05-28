# Github: Shantanugupta1118
# DAY 12 of DAY 100
# Hate 1111 - Codeforces
#  https://codeforces.com/contest/1526/problem/B


for i in range(int(input())):
    n = int(input())
    rem = (n-(n%11)*111)
    if rem>=0 and rem%11==0: 
        print("YES")
    else:
        print("NO")