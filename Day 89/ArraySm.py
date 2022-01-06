
arr = list(map(int, input().split()))
res = []
target = arr[0]
del arr[0]
arr.sort()
for i in range(len(arr)-1):
    for j in range(i, len(arr)):
        if arr[i] + arr[j] == target:
            res.extend([arr[i], arr[j]])
if len(res)!=0:
    for i in res:
        print(i, end=", ")
else:
    print(-1)