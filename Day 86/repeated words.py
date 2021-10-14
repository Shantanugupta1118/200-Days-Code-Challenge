



'''
string = input()
n = string.split(" ")
occ = {}
print(n)
for ii in n:
    if ii not in occ: 
        occ[ii] = 1
    else:
        occ[ii] += 1

res = []
for k, v in occ.items():
    if v>1:
        res.append(k)
if len(res)!=0:
    print(*res)
else:
    print("NA")

'''

string = input()
n = string.split(" ")
unique_words = set(n)
res = []
for i in unique_words:
    if n.count(i)>1:
        res.append(i)
res = sorted(res)
if len(res)!=0: 
    print(*res)
else:
    print("NA")

