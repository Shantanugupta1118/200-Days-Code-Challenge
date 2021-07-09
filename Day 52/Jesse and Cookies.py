# Github: Shantanugupta1118
# DAY 52 of DAY 100
# Jesse and Cookies    -  Hackerrank

from heapq import heappush, heappop, heapify
class Solution:
    def JesseAndCookies(self, n, k, cookies):
        heapify(cookies)
        res = 0
        while any(c < k for c in cookies) and len(cookies)>1:
            a = heappop(cookies)
            b = heappop(cookies)
            heappush(cookies, a + b*2)
            res += 1
        if all(x >= k for x in cookies):
            return res
        else:
            return -1            


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(Solution().JesseAndCookies(n, k, arr))