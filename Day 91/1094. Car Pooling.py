# Github: Shantanugupta1118
# DAY 91 of DAY 100
# 1094. Car Pooling - Leetcode
# https://leetcode.com/problems/car-pooling/


class Solution:
    def carPooling(self, trips,capacity):
        car = [0]*1001
        for trip in trips:
            car[trip[1]] += trip[0]
            car[trip[2]] -= trip[0]
        for stop in car:
            capacity -= stop
            if capacity < 0: return False
        return True

    def solve(self, trips, capacity):
        return self.carPooling(trips, capacity)

for _ in range(1):
    print(Solution().solve([[2,1,5],[3,3,7]], 5))