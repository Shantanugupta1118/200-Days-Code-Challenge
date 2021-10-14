# Github: Shantanugupta1118
# DAY 85 of DAY 100

class Solution:
    def solve(self, arr, threshold):
        res1, res2 = {}, {}
        ans = []
        for i in arr:
            # print(i)
            receive, send, amt = map(int, i.split(' '))
            if receive not in res1:
                res1[receive] = 1
            elif receive in res1:
                res1[receive] += 1
            if send not in res2:
                res2[send] = 1
            elif send in res2:
                res2[send] += 1
        res1.update(res2)
        # print(res1)
        for key, val in res1.items():
            if val >= threshold:
                ans.append(key)
        ans.sort()
        return ans

n = []
for _ in range(int(input())):
    n.append(input())
thresold = int(input())
print(*Solution().solve(n, thresold))