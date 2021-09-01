# Github: Shantanugupta1118
# DAY 73 of DAY 100
# 167. Two Sum II - Input array is sorted - leetcode

class Solution:
    def solve(self, numbers, target):
        left, right = 0,0
        for i in range(len(numbers)):
            if numbers[i] >= target:
                right = i
                break
        print(left, right)
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return left+1, right+1
            if total < target:
                left +=1
            else:
                right -=1
            


print(Solution().solve(numbers = [2,7,11,15], target = 9))
