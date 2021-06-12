# username: shantanugupta1118
# Day 32 of 100 Days
# Minimum Number of Refueling Stops - Leetcode/June-21
# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3776/



class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations += [(target, 0)]
        pq, pqsum = [[1, startFuel]], startFuel
        for x, y in stations:
            if pqsum < x:
                return -1
            temp, temp_sum = [], 0
            while temp_sum < x:
                target_x, target_y = pq.pop()
                temp.append([1, target_y])
                temp_sum += target_y
            while temp:
                target_x, target_y = temp.pop()
                pq.append((target_x, target_y))
            pq.append((0, y))
            pq.sort()
            pqsum += y
        return sum((x for x, _ in list(pq))) -1

n = int(input())
stations = []
for i in range(n):
	stations.append(list(map(int, input().split())))
target = int(input())
startFuel = int(input())
print(Solution().minRefuelStops(target, startFuel, stations))