# Github: Shantanugupta1118
# DAY 13 of DAY 100
# Highest Value Palindrome - Hackerrank
# https://www.hackerrank.com/challenges/richie-rich/problem

def create_palin(s, k):
    i,j = 0, len(s)-1
    while i<j and k!=0:
        # print("begin",s, i, j, k)
        if s[i]!=s[j]:
            mx = max(s[i], s[j])
            if s[i]>s[j]:
                s[j] = mx
            else:
                s[i] = mx
            k -= 1
        i += 1
        j -= 1
        # print("end",s, i, j, k)
    if k!=0:
        i, j = 0, len(s)-1
        while k!=0 and k>0:
            if s[i]==s[j] or s[i]>9 and s[j]>9:
                s[i] = '9'
                s[j] = '9'
                k -= 1
            i += 1
            j -= 1
    s = "".join(s)

    if s==s[::-1]: return s
    return -1



n, k = map(int, input().split())
inp = input()
print(create_palin(list(inp), k))