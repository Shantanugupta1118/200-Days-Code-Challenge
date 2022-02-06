# Github: Shantanugupta1118
# DAY 117 of DAY 200
# 80. Remove Duplicates from Sorted Array II



from collections import Counter as Cnt

class Solution:
    '''
        # First Approach --------
        
    def solve(self, arr):
        dic_arr = {}
        for i in arr:
            if i not in dic_arr:
                dic_arr[i] = 1
            else:
                dic_arr[i] += 1
        arr.clear()
        for k in dic_arr:
            arr.append(k)
            if dic_arr[k] >= 2:
                arr.append(k)
        arr.sort()
        return len(arr)
    '''
    
    def solve(self, arr):
        n = len(arr)
        counter = Cnt(arr)
        print(counter)
        for i in reversed(range(n)):
            if counter[arr[i]] > 2:
                counter[arr[i]] -= 1
                arr.pop(i)
        return arr
    
print(Solution().solve([1,1,1,2,2,3]))

