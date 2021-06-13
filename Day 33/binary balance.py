

from itertools import chain, combinations

for _ in range(int(input())):
    n = int(input())
    binary_str = list(map(int, input()))
    l, r = map(int, input().split())
    # binary_str = list(s)
    # li = list(chain.from_iterable(combinations(binary_str, r)))
    li = combinations(binary_str, r)
    for i in list(li):
        print(i)
    for i in range(len(binary_str)+1):
        li1 = []
        for x in li:
            if x:
                li1.append(x)
        li2 = []
        for j in li1:
            x = list(j)
            bi = "".join(x)
            dec = int(str(bi), 2)
            if dec>=l and dec<=r:
                li2.append(dec)
    print(len(set(li2)))
    print(len(set(li1)))