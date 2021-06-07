# Github: Shantanugupta1118
# DAY 27 of DAY 100
# Re-arrange strgin k distance - Leetcode/Google
# https://leetcode.com/problems/rearrange-string-k-distance-apart/

from collections import *
from heapq import *
class solution:
    def arrange(self, s, k):
        counter = Counter(s)
        pq = [(-counter[c], c) for c in counter]
        heapify(pq)
        ans = ""
        while pq:
            temp_list = []
            if len(pq) < k and -pq[0][0] > 1:
                return ""
            for _ in range(min(k, len(pq))):
                curr_item = heappop(pq)
                count = -curr_item[0]
                c = curr_item[1]
                ans += c
                count -= 1
                if count:
                    temp_list.append((count, c))
            for count, c in temp_list:
                heappush(pq, (-count, c))
        return ans


sstring = "aaabbc"
k = 3
print(solution().arrange(sstring, k))