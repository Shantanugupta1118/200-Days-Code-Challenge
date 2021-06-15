# username: shantanugupta1118
# Day 35 of 100 Days
# Vowel and Consonant Substrings! - InterviewBit
# https://www.interviewbit.com/problems/vowel-and-consonant-substrings/


# Solution 1 - O(n^2) /  Issue - TLE


"""def solution(word):
	res = [word[i: j] for i in range(len(word))
	          for j in range(i + 1, len(word) + 1)]
	vowel = 'aeiou'
	count = 0
	for i in res:
	    if i[0] in vowel and i[-1] not in vowel:
	        count += 1
	    elif i[-1] in vowel and i[0] not in vowel:
	        count += 1
	return count


word = "coujfhovhsouvaofihg"
print(solution(word))
"""


# Solution 2 - Brute-Force / O(n)

def solve(word):
	vow, cons = [], []
	for i in range(len(word)):
	    if word[i] in 'aeiou':
	        vow.append(i)
	    else:
	        cons.append(i)
	return len(vow)*len(cons)


word = "ufycnhrtuggfiuygafgaf"
print(solve(word))