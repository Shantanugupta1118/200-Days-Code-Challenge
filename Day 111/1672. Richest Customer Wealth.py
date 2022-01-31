# Github: Shantanugupta1118
# DAY 111 of DAY 200
# 1672. Richest Customer Wealth



class Solution:
    def richest_cust(self, acc):
        mx = -999
        for i in acc:
            mx = max(mx, sum(i))
        return mx

print(Solution().richest_cust([[1,2,3],[3,2,1]]))
