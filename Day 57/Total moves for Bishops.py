# Github: Shantanugupta1118
# DAY 57 of DAY 100
# Total Moves For Bishop!   -  InterviewBit
# https://www.interviewbit.com/problems/total-moves-for-bishop/


class Solution:
    def solve(self, A, B):
        return (min(A, B)-1) + (8-max(A,9-B)) + (8-max(A, B)) + (min(A, 9-B)-1)


print(Solution().solve(4,3))
print(Solution().solve(4,7))
print(Solution().solve(1,4))