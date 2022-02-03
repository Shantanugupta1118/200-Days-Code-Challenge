# Github: Shantanugupta1118
# DAY 114 of DAY 200
# 454. 4Sum II



class Solution:
    def solve(self, n1, n2, n3, n4):
        # Brute Force - O(n*4)
        # count = 0
        # for i in range(len(n1)):
        #     for j in range(len(n2)):
        #         for k in range(len(n3)):
        #             for l in range(len(n4)):
        #                 if n1[i]+n2[j]+n3[k]+n4[l] == 0:
        #                     count += 1
        # return count
    
    
        num_sum = {}
        for i in n1:
            for j in n2:
                s = i+j
                if s not in num_sum:
                    num_sum[s] = 0
                num_sum[s] += 1
        ans = 0
        for i in n3:
            for j in n4:
                s = i+j
                if -s in num_sum:
                    ans += num_sum[-s]
        return ans
    
print(Solution().solve([1,2], [-2,-1], [-1,2], [0,2]))
print(Solution().solve([0], [0], [0], [0]))

