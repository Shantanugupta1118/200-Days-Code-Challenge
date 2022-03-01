# Github: Shantanugupta1118
# Day 134 of day 200
# 1281. Subtract the Product and Sum of Digits of an Integer


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, summ = 1, 0
        while n>0:
            remainder = n%10
            n //= 10
            product *= remainder
            summ += remainder
        return product - summ


print(Solution().subtractProductAndSum(234))
