# Github: Shantanugupta1118
# DAY 112 of DAY 200
# 121. Best Time to Buy and Sell Stock



class Solution:
    def maxSell(self, prices):
        if len(prices)<=1: return 0
        profit, buy_price = 0, max(prices)
        for i in prices:
            buy_price = min(buy_price, i)
            profit = max(i - buy_price, profit)
        return profit             
                 
         
         
         
         
print(Solution().maxSell([7,1,5,3,6,4]))
print(Solution().maxSell([7,6,4,3,1]))
print(Solution().maxSell([2,4,1]))