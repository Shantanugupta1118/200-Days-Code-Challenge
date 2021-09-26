

def e_commerce(n, arr):
    pos_count = 0
    for i in range(n):
        if arr[i] > 0: pos_count += 1
    return pos_count

n = int(input())
arr = [int(x) for x in input().split()]
print(e_commerce(n, arr))