# username: shantanugupta1118
# Day 36 of 100 Days
# Jim and Order - Hackerrank

arr = []
for _ in range(int(input())):
	a,b = map(int, input().split())
	arr.append(a+b)

idx = {}
for i in range(len(arr)):
	idx[i+1] = arr[i]

nn = sorted(idx.items(), key=lambda x:x[1])
for i,j in nn:
	print(i, end=' ')

