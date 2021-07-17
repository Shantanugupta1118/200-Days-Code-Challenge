# Github: Shantanugupta1118
# DAY 60 of DAY 100
# 927. Three Equal Parts  -  Leetcode/July
# https://leetcode.com/problems/three-equal-parts/


class Solution:
    def threeEqualParts(self, arr):
        ans = [-1,-1]
        numsOf1s = 0
        for i in arr:
            numsOf1s += i
        if numsOf1s == 0:
            return [0,2]
        if numsOf1s%3 != 0:
            return ans
        
        eachPart = numsOf1s//3
        index0, index1, index2 = -1, -1, -1
        numsOf1s = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                numsOf1s += 1
                if numsOf1s == eachPart+1:
                    index1 = i
                elif numsOf1s == 2*eachPart+1:
                    index2 = i
                elif numsOf1s == 1:
                    index0 = i
        while index2 < len(arr):
            if arr[index2] == arr[index0] and arr[index2] == arr[index1]:
                index0 += 1
                index1 += 1
                index2 += 1
            else:
                return ans 
        return [index0-1, index1]


arr = list(map(int, input().split()))
print(Solution().threeEqualParts(arr))