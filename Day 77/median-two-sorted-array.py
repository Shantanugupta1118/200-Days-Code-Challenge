# Github: Shantanugupta1118
# DAY 77 of DAY 100


'''
# TC - O(nlogn)
class Solution:
    def solve(self, ls1, ls2):
        ls1 = ls1+ls2
        ls1.sort()      #TC - Worst Case - O(nlogn)
        n = len(ls1)    #TC - O(n)
        med = n//2
        if med%2!=0:
            return ls1[med]
        return (ls1[med] + ls1[med-1])//2
        '''


class Solution:
    def solve(self, ls1, ls2):
        len1, len2 = len(ls1), len(ls2)
        mid = (len1+len2)/2
        if mid == 0.5: return float(ls1[0]) if len1 > len2 else float(ls2[0])
        x = y = 0
        curr = prev = 0
        itr = mid+1 if mid % 1 == 0 else mid+0.5
        for __ in range(int(itr)):
            prev = curr
            if x == len1:
                curr = ls2[y]
                y += 1
            elif y == len2:
                curr = ls1[x]
                x += 1
            elif ls1[x] > ls2[y]:
                curr = ls2[y]
                y += 1
            else:
                curr = ls1[x]
                x += 1
        if mid%1!=0.0:
            return int(curr)
        else:
            return (curr+prev)/2


arr1 = [1,12,15,26,38]
arr2 = [2,13,24]
print(int(Solution().solve(arr1, arr2)))