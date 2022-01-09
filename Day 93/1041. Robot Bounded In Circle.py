# Github: Shantanugupta1118
# DAY 93 of DAY 100

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        sums = [0] * 4       
        idx = 0
        for move in instructions:
            if move == 'G':
                sums[idx % 4] += 1
            else:
                idx += 1 if move == 'L' else -1

        return (sums[0] == sums[2] and sums[1] == sums[3]) or idx % 4 != 0
    def solve(self, ls):
        return self.isRobotBounded(ls)
        

print(Solution().solve("GGLLGG"))
print(Solution().solve("GG"))
print(Solution().solve("GL"))
print(Solution().solve("GGLG"))
print(Solution().solve("GGL"))