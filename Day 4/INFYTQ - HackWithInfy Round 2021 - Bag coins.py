# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 4 of DAY 100
#  Infytq - HackwithInfy round solution 2021 - Bags coins.

#solution
def solve(bag_coins, n):
    count=[]
    k=0
    for j in bag_coins:
        minn=min(bag_coins[k:len(bag_coins)])
        total=0
        for ele in bag_coins[k:len(bag_coins)]:       
            if(ele>=minn):
                total+=minn
        count.append(total)
        k+=1
    return max(count)


n=int(input())
bag_coins=[]
for  i in range(n):
    x = int(input())
    bag_coins.append(x)
print(solve(bag_coins, n))

