# Github: Shantanugupta1118
# DAY 104 of DAY 100
# 1291. Sequential Digits


class Solution:
    def seqDig(self, low, high):
        nums = (12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,
             1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,
             56789,123456,234567,345678,456789,1234567,2345678,3456789,
             12345678,23456789,123456789)
        return filter(lambda n: low <= n <= high, nums)
       
    
print(*Solution().seqDig(100, 30000))