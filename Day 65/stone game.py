# Github: Shantanugupta1118
# DAY 65 of DAY 100
# 877. Stone Game  -  Leetcode/August
# https://leetcode.com/problems/stone-game/


class Solution:
    def solve(self, piles):
        lee, alex = [], []
        piles.sort(reverse=True)
        while len(piles) > 0:
            alex.append(piles.pop(0))
            lee.append(piles.pop(0))
        print(alex, lee)
        if sum(alex) > sum(lee):
            return True
        return False

for _ in range(int(input())):
    arr = [5,3,4,5]
    print(Solution().solve(arr))


    