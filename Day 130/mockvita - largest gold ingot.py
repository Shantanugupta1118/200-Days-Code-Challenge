# Github: Shantanugupta1118
# DAY 130 of DAY 200
# Largest Gold Ingot   -  TCS Mockvita


class Solution:
    def __init__(self):
        self.mod = 10**9+7
        
    def solve(self, n, l, b, arr, total_sum):
        m = self.mod
        temp, ans = 0, 0
        st = []
        print(total_sum)
        for i in range(n):
            while len(st) != 0 and arr[i] <= arr[st[-1]]:
                top = st[-1]
                st.pop()
                temp = arr[top]*i
                if len(st) != 0:
                    temp = temp - st[-1] - 1
                ans = max(ans%self.mod, temp)
            st.append(i)
            print(st)
        while len(st) == False:
            top = st[-1]
            st.pop()
            temp = arr[top]*n
            if len(st) != 0:
                temp = temp - st[-1] - 1    
            ans = max(ans%self.mod, temp)
        print(ans)
        return ((total_sum%m - ans%m)%m*l%m*b%m)%m

    
    
    
    
# n = int(input())    # total number of arr
# l,b = map(int, input().split())    # length, breadth
# arr = []
# total_sum = 0
# for i in n:
#     txt = int(input())
#     arr.append(txt)
#     total_sum += txt
    
# print(Solution().solve(n, l, b, arr, total_sum))
print(Solution().solve(7, 1, 1, [6,7,3,4,5,1,3], 28))
