# Github: Shantanugupta1118
# DAY 79 of DAY 100


import collections 

# limit = 10**6+1
# def DownToZero():
#     active = [-1]*limit
#     active[0], active[1], active[2], active[3] = 0, 1, 2, 3 

#     for i in range(limit):
#         if active[i] == -1 or active[i] == active[i-1]+1:
#             active[i] = active[i-1] + 1
#         j = 1
#         while j<=i and j*i < limit:
#             if active[j*i] == -1 or active[j*i] > active[i]+1:
#                 active[j*i] = active[i]+1
#             j += 1
#     return active

import sys, math

def downToZero():
    # global min_moves
    # if n <= 3: return n 
    # if min_moves[n] > 0: return min_moves[n]
    # m = sys.maxsize
    # for i in range(2, int(math.sqrt(n))+1):
    #     if n%i == 0:
    #         factor = n//i
    #         m = min(m, downToZero(factor)+1)
    # m = min(m, downToZero(n-1)+1)
    # # min_moves[n] = m
    # return m 
    
    N=1000001
    moves=[-1]*(N+1)
    moves[0]=0
    moves[1]=1
    moves[2]=2
    moves[3]=3
    
    for i in range(1,N+1):
        if (moves[i]==-1 or moves[i]>moves[i-1]+1):
            moves[i]=moves[i-1]+1
        j=2
        while j<=i and j*i<=N:
            if (moves[i*j]==-1 or (moves[i]+1)<moves[i*j]):
                moves[i*j]=moves[i]+1
            j+=1
    return moves                


generated_numbers = downToZero()
for _ in range(int(input())):
    n = int(input())
    min_moves = [-1]*1000001
    print(generated_numbers[n])