from collections import Counter

class Solution:
	def prime(self, res):	
		prime_set = []
		prime = [True for i in range(res)]
		p = 2
		while (p * p <= res):
			if (prime[p] == True):
			    for i in range(p * 2, res, p):
			        prime[i] = False
			p += 1
		prime[0]= False
		prime[1]= False
		for p in range(res):
			if prime[p]:
			    prime_set.append(p)

		ans = []
		temp = []
		for i in prime_set:
			for j in prime_set:
				if i+j == res and i not in temp and j not in temp:
					if i<=j:
						return i,j
					else:
						return j,i


res = 1048574
print(Solution().prime(res))