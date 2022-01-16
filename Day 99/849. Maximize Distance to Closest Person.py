# Github: Shantanugupta1118
# DAY 99 of DAY 100
# 849. Maximize Distance to Closest Person

from operator import le


class Solution:
    def maxDistance(self, x):
        length_of_seats = len(x)
        length_of_setseat = set()
        k = 0
        if x[0]==0:
            i = 1
            while i<1 and x[i]==0:
                i += 1
            length_of_setseat.add(i+i)
            k = i
        i = 1
        if x[length_of_seats-i] == 0:
            i = 1
            while i<=length_of_seats and x[length_of_seats-i] == 0:
                i += 1
            length_of_setseat.add(i + i - 1)
        p = k
        for j in range(k+1, length_of_seats):
            if x[j] == 1:
                length_of_setseat.add(j-p)
                p = j
        return max(length_of_setseat)//2


print(Solution().maxDistance([1,0,0,0,1,0,1]))