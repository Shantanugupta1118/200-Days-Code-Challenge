# Github: Shantanugupta1118
# DAY 18 of DAY 100
#  Array Manipulation - Hackerrank
#  https://www.hackerrank.com/challenges/crush/problem



n, query = map(int, input().split())
arr = [0]*n 
while query!=0:
    start, end, value = map(int, input().split())
    for i in range(start-1, end):
        arr[i] += value
    query -= 1
print(*arr)