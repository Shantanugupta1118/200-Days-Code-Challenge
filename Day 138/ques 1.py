


from collections import defaultdict

def getPalindrome(st):
	hmap = defaultdict(int)
	for i in range(len(st)):
		hmap[st[i]] += 1
	oddCount = 0

	for x in hmap:
		if (hmap[x] % 2 != 0):
			oddCount += 1
			oddChar = x

	firstHalf = ""
	secondHalf = ""
	for x in sorted(hmap.keys()):
		s = (hmap[x] // 2) * x
		firstHalf = firstHalf + s
		secondHalf = s + secondHalf
	if (oddCount == 1):
		return (firstHalf + oddChar + secondHalf)
	else:
		return (firstHalf + secondHalf)


def CountPS(str, n):
    str = getPalindrome(str)
    dp = [[0 for x in range(n)]	for y in range(n)]

    P = [[False for x in range(n)]
        for y in range(n)]
    for i in range(n):
        P[i][i] = True

    for i in range(n - 1):
        if (str[i] == str[i + 1]):
            P[i][i + 1] = True
            dp[i][i + 1] = 1



    for gap in range(2, n):
        for i in range(n - gap):
            j = gap + i
            if (str[i] == str[j] and P[i + 1][j - 1]):
                P[i][j] = True
            if (P[i][j] == True):
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] + 1 - dp[i + 1][j - 1])
            else:
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] - dp[i + 1][j - 1])
    return dp[0][n - 1] + len(str)



n = int(input())
q = int(input())
s = input()
res = 0
for i in range(q):
    start, end = map(int, input().split())
    temp, n = s[start:end+1], len(s[start:end+1])
    res += CountPS(temp, n)
print(res)