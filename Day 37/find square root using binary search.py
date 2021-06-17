# Github: Shantanugupta1118
# DAY 37 of DAY 100
# Find square root of number using Binary Search - Leetcode/Binary Search
# https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/



class solution:
    def sqrt(self, n):
        start, end = 0, n 
        while start <= end:
            mid = (start+end)//2
            square = mid**2
            if square == n:
                return mid
            elif square > n:
                end = mid - 1
            else:
                start = mid +1
        return end 

num = int(input())
print(solution().sqrt(num))