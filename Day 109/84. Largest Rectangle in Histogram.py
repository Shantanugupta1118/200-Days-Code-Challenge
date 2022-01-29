# Github: Shantanugupta1118
# DAY 109 of DAY 200
# 84. Largest Rectangle in Histogram

'''
    # Partially Accepted --
    
class Solution:
    def LargeHist(self, height):
        mx = max(height)
        n = len(height)
        count = 0
        for i in range(n-1):
            for j in range(i, n):
                if i!=j:
                    mn = min(height[i:j])
                    print(height[i:j+1])
                    count += 1
                    temp = mn*count
                    print(temp, count, height[i], height[j])
                    mx = max(temp, mx)
            temp = 0
            count = 0
            print("first iter: ", mx)
        min_val = min(height)

        #print(mx, min_val, n)
        temp = min_val*n
        mx = max(temp, mx)
        return mx
 '''       
    
 
class Solution:
    def LargeHist(self, height):
        mx = 0
        stack = []
        height = height + [0]
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                temp = height[stack.pop()]
                mx = max(mx, temp*(i-stack[-1]-1) if stack else temp*i)
            stack.append(i)
        return mx

print(Solution().LargeHist([2,1,5,6,2,3]))
print(Solution().LargeHist([5,4,1,2]))
print(Solution().LargeHist([1,2,2]))