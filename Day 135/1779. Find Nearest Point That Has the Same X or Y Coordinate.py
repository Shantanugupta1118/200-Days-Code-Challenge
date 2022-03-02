# Github: Shantanugupta1118
# Day 135 of day 200
# 1779. Find Nearest Point That Has the Same X or Y Coordinate

import sys

class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:
        mx = sys.maxsize
        min_indx = -1
        for i in range(len(points)):
            if points[i][0] == x or y == points[i][1]:
                dist = abs(x-points[i][0]) + abs(y - points[i][1])
                if dist < mx:
                    mx = dist
                    min_indx = i
        return min_indx


print(Solution().nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))
