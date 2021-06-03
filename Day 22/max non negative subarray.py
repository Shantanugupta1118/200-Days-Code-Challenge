# Github: Shantanugupta1118
# DAY 22 of DAY 100
# Max Non Negative SubArray
# https://www.interviewbit.com/problems/max-non-negative-subarray/


class Solution:
    def maxset(self, A):
        mx = []
        temp = []
        for i in A:
            if i>=0:
                temp.append(i)
            else:
                mx.append(temp)
                temp = []
        if temp is not None:
            mx.append(temp)
        max_sum = 0
        ans = 0
        for i in mx:
            if sum(i) >= max_sum:
                max_sum = sum(i)
                ans = i
            elif len(i)==len(ans):
                if len(ans) > len(i):
                    continue
                else:
                    ans = i
        if len(ans)!=0:
            return ans, mx
        return -1

A = list(map(int, input().split()))
print(Solution().maxset(A))