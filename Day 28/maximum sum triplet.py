# Github: Shantanugupta1118
# DAY 28 of DAY 100
# Maximum Sum Triplet - InterviewBit
# https://www.interviewbit.com/problems/maximum-sum-triplet/




class solution:
    def solve(self, arr):
        mx1, mx2 = 0, 0
        ans = 0
        for i in range(1, len(arr)-1):
            for j in range(0, i):
                if arr[j] < arr[i]:
                    mx1 = max(mx1, arr[j])
            for j in range(i+1, len(arr)):
                if arr[j] > arr[i]:
                    mx2 = max(mx2, arr[j])
                    if mx1>0 and mx2>0:
                        ans = max(ans, mx1+mx2+arr[i])
        return ans


arr = [2, 5, 3, 1, 4, 9]
print(solution().solve(arr))
