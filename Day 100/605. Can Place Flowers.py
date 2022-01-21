# Github: Shantanugupta1118
# DAY 100 of DAY 100
# 605. Can Place Flowers - Leetcode

class Solution:
    def plantFlower(self, flowers, n):
        '''
        # -------------- some cases was failed --------------------
        if len(flowers) < 2 and 1 in flowers: return False
        count = 0
        i = 0
        while i < len(flowers):
            if flowers[i] == 0:
                for j in range(i, len(flowers)):
                    if flowers[j] == 0:
                        count += 1
                    else:
                        break
                i = j
                print(n, count)

                if count%2==0:
                    count = count//2 - 1
                else:
                    if count >= 2 and j == len(flowers)-1:
                        n = n-count//2
                    elif count > 2 and j!=len(flowers)-1:
                        n = n - count//2
            
            else:
                if n<=0: break
                i += 1
                count = 0
        if n==0 or n < 0: return True
        else: return False
        '''
        
        plant_flower = [0] + flowers + [0]
        count = 0
        for idx in range(len(flowers)):
            if plant_flower[idx:idx+3] == [0, 0, 0]:
                plant_flower[idx+1]=1
                count+=1
        return count >= n  
                
        
        
 
    
print(Solution().plantFlower([1,0,0,0,1], 1))
print(Solution().plantFlower([1,0,0,0,0,1], 2))
print(Solution().plantFlower([1,0,1,0,1,0,1],1))