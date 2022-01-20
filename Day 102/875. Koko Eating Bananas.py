#Github: Shantanugupta1118
# Day 102 of Day 200
#875. Koko Eating Bananas


class Solution:
    def koko(self, piles, h):
        l, r = 1, max(piles)
        while l<r:
            mid = (l+r)//2
            if sum([(x+mid-1)//mid for x in piles]) > h:
                l = mid+1
            else:
                r = mid
        return l



print(Solution().koko([3,6,7,10], 8))
