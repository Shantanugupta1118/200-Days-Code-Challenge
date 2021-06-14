# username: shantanugupta1118
# Day 34 of 100 Days
# Meeting Room II - Leetcode/LintCode
# https://www.lintcode.com/problem/921/


from heapq import heappush, heappushpop
class Solution:
	def meeting(self, intervals):
		if len(intervals) == 0:
			return 0 

		intervals.sort(key=lambda x:x[0])
		min_heap = [intervals[0][1]]
		for i in range(1, len(intervals)):
			if intervals[i][0] < min_heap[0]:
				heappush(min_heap, intervals[i][1])
			else:
				heappushpop(min_heap, intervals[i][1])
		return len(min_heap)




intervals = [(2,7)]
print(Solution().meeting(intervals))