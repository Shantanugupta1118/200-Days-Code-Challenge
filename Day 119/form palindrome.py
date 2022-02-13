# Github: Shantanugupta1118
# DAY ___ of DAY 200
#


from collections import defaultdict

class Solution:
    def getPalindrome(self, st):
        st = str(st)
        hmap = defaultdict(int)
       	for i in range(len(st)):
       		hmap[st[i]] += 1
       
       	oddCount = 0
       	for x in hmap:
       		if (hmap[x] % 2 != 0):
       			oddCount += 1
       			oddChar = x
       	if (oddCount > 1 or oddCount == 1 and
       			len(st) % 2 == 0):
       		return -1
       	firstHalf = ""
       	secondHalf = ""
       	for x in sorted(hmap.keys()):
       		s = (hmap[x] // 2) * x
       		firstHalf = firstHalf + s
       		secondHalf = s + secondHalf
       	if (oddCount == 1):
       		return (firstHalf + oddChar + secondHalf)
       	else:
       		return (firstHalf + secondHalf)

    
    
print(Solution().getPalindrome(2341))
print(Solution().getPalindrome(388003))
