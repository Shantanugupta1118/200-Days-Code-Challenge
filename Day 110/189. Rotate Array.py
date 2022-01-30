# Github: Shantanugupta1118
# DAY 119 of DAY 200
# 189. Rotate Array
 

class Solution:
    '''
        First approach
    ''' 
    '''
    def rotateArray(self, arr, k):
        for i in range(k):
            arr = [arr[-1]] + arr[:-1]
        return arr
     '''

    def rotateArray(self, arr, k):
        l = len(arr)
        if l == k: return
        k = k%l
        arr.reverse()
        for i in range(k//2):
            arr[i], arr[k-1-i] = arr[k-1-i], arr[i]
        for i in range(k, (l+k)//2):
            arr[i], arr[l-1-i+k] = arr[l-1-i+k], arr[i]
        
        
    
    
arr = [1,2,3,4,5,6,7]; k = 3
Solution().rotateArray(arr, k)
print(arr)
arr = [-1,-100,3,99]; k = 2
Solution().rotateArray(arr, k)
print(arr)