# username: shantanugupta1118
# Day 34 of 100 Days
# Palindrom-pairs - Leetcode/June-21
# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3777/



class Solution:
	def palindrome_pairs(self, s):
		def ispalin(x):
			return x==s[::-1]

		res = []
		initial_idx = 0
		for i in s:
			for j in range(len(s)):
				if ispalin(s[j]+i):
					res.append([j+i])
		return res

st = ["abcd","dcba","lls","s","sssll"]
print(Solution().palindrome_pairs(st))