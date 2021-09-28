# Github: Shantanugupta1118
# DAY 84 of DAY 100

class Solution:
    def solve(self, arr):
        '''
        # -------- Complexity - O(2*n) ---------
        odd, even = [], []
        for i in arr:
            if i%2==0: even.append(i)
            else: odd.append(i)
        res = []
        for i in range(len(arr)):
            if i%2==0: 
                res.append(even.pop(0))
            else:
                res.append(odd.pop(0))
        return res
        '''


        # -------- Best complexity - O(n) ---------
        odd, even = 1, 0
        ls = [0]*len(arr)
        for i in arr:
            if i%2==0:
                ls[even] = i
                even += 2
            else:
                ls[odd] = i
                odd += 2
        return ls

# for _ in range(int(input())):
arr = list(map(int, input().split()))
print(Solution().solve(arr))
