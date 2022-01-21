# Github: Shantanugupta1118
# DAY 103 of DAY 100
# 134. Gas Station


class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        
        extra, ans = 0, 0
        for i in range(len(gas)):
            extra += gas[i] - cost[i]
            if extra < 0:
                ans = i+1
                extra = 0
        return ans



print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5, 1, 2]))