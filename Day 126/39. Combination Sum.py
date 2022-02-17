# Github: Shantanugupta1118
# DAY 126 of DAY 200
# 39. Combination Sum


class Solution:
    def solve(self, arr, target):
        self.ans= []
        def helper(arr, num, sm):
            if sm == target: self.ans.append(num)
            if sm >= target: return
            for i in range(len(arr)):
                helper(arr[i:], num+[arr[i]], sm+arr[i])
        helper(arr, [], 0)
        return self.ans
    
    
print(Solution().solve([2,3,6,7],7))

