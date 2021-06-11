# Github: Shantanugupta1118
# DAY 18 of DAY 100
# 42. Trapping Rain Water - Leetcode
# https://leetcode.com/problems/trapping-rain-water/

class solution:
    def watertrap(self, h):
        if len(h) <= 2:
            return 0

        left = []
        left_most = h[0]
        for m in h:
            left_most = max(left_most, m)
            left.append(left_most)
        
        h = h[::-1]
        right = []
        right_most = h[0]
        for m in h:
            right_most = max(right_most, m)
            right.append(right_most)
        print(left, right)
        compiled = []
        for i in range(len(left)):
            compiled.append(min(left[i], right[len(h)-i-1]))
        return sum(compiled) - sum(h)