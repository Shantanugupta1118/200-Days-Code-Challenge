# Github: Shantanugupta1118
# DAY 115 of DAY 200
# 525. Contiguous Array



class Solution:
    def solve(self, nums):
        dic = {0:-1}
        prefSum, res = 0, 0
        for i, num in enumerate(nums):
            prefSum += 1 if num == 1 else -1
            if prefSum in dic:
                res = max(res, i-dic[prefSum])
            else:
                dic[prefSum] = i
        return (res)
    
    
print(Solution().solve([0,1,0]))

