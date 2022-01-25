# Github: Shantanugupta1118
# Day 106 of Day 200
#941. Valid Mountain Array



class Solution:
    def validMountainArray(self, arr):
        increased = decreased = False
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if decreased:
                    return False
                increased = True
            elif arr[i] < arr[i-1]:
                if not increased:
                    return False
                decreased = True
            else:
                return False
            
        return decreased


print(Solution().validMountainArray([0,3,4,5,6,3,2,1]))
