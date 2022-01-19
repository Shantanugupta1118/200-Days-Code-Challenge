# Github: Shantaugupta1118
# Day 101 of Day 200
# 345. Reverse Vowels of a String


# ------- 1956 MS RUNTIME ----------
'''

def reverseString(s):
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    ls = []
    for i in range(len(s)):
        if s[i] in vowels:
            ls.append(s[i])
            s = s[:i]+'_'+s[i+1:]
    print(s, ls)
    for i in range(len(s)):
        if s[i] == '_':
            temp = ls.pop()
            s = s[:i]+ temp + s[i+1:]
    return s
   '''


def reverseString(s):
    vowels = 'aeiouAEIOU'
    data = []
    for i in s:
        if i in vowels:
            data.append(i)
    res = ''
    for i in s:
        if i in vowels:
            res += data.pop()
        else:
            res+=i
    return res

print(reverseString("hello"))
print(reverseString("leetcode"))
