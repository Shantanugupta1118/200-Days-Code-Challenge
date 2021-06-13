
class Solution:
    def largestNumber(self, A):
        res = []
        for i in range(len(A)):
            temp = list(map(int, str(A[i])))
            res.append(temp)
        ans = ''
        while res:
            mx = max(res)
            res.remove(mx)
            mx = map(str, mx)
            ans += "".join(mx)
        return ans

A = [3, 30, 34, 5, 9]
print(Solution().largestNumber(A))