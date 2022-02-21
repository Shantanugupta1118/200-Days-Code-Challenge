# Github: Shantanugupta1118
# Day 128 of day 200
# 1288. Remove Covered Intervals


class solution:
    def removeCoveredIntervals(self, nums):
        count = 0
        prev_inter = None
        for i in sorted(nums, key=lambda x:(x[0], -x[1])):
            if prev_inter and prev_inter[0] <= i[0] and prev_inter[1] >= i[1]:
                continue
            prev_inter = i
            count += 1
        return count

print(solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))

