# Github: Shantanugupta1118
# DAY 54 of DAY 100
# 295. Find Median from Data Stream  - Leetcode/July
# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3810/



from heapq import *
class Solution:
    def __init__(self):
        self.data = 1, [], []
        print(self.data)


    def addNum(self, num):
        print(self.data)
        sign, heap1, heap2 = self.data
        heappush(heap2, -heappushpop(heap1, num*sign))
        self.data = -sign, heap2, heap1
        print(self.data)

    def findMedian(self):
        sign, heap1, _ = temp = self.data
        return (heap1[0]*sign - temp[-sign][0])/2.0

obj = Solution()
obj.addNums(5)
