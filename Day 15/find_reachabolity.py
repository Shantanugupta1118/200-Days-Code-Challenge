# Github: Shantanugupta1118
# DAY 15 of DAY 100
# Find Reachability - HackerEarth



try:
    L=[]
    while True:
        name=input()
        L.append(name)
except:
    pass

follower = []
following = []
rel = []
for ele in L:
    if len(ele) > 1:
        rel.append(ele)
        follower.append(ele[0])
        following.append(ele[2])
    else:
        follower.append(ele)
op = 0
for ind in range(1,len(follower)):
    if ind ==0:
        if follower[ind] in following or follower[ind+1] in following:
            op =1
    elif ind == len(follower):
        if follower[ind] in following or follower[ind-1] in following:
            op = 1
    elif follower[ind] in following or follower[ind+1] in following or follower[ind-1] in following:
        op=1
    
print(op)