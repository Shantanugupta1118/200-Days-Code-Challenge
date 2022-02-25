# Github: Shantanugupta1118
# Day 131 of day 200
# 165. Compare Version Numbers


class Solution:
    def compareVersion(self, v1, v2):
        s1 = list(v1.split('.'))
        s2 = list(v2.split('.'))
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2: 
            s2 += [0]*(n1 - n2)
        elif n1 < n2:
            s1 += [0]*(n2 - n1)

        for i in range(len(s1)):
            if int(s1[i]) < int(s2[i]): return -1
            elif int(s1[i]) > int(s2[i]): return 1
        return 0


print(Solution().compareVersion("1.01", "1.001"))
print(Solution().compareVersion("1.0", "1.0.0"))
print(Solution().compareVersion("0.1", "1.1"))