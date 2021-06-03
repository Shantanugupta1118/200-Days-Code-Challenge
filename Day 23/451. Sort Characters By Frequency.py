# Github: Shantanugupta1118
# DAY 23 of DAY 100
# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/

def freq(s):
    dic = {}
    res = ''
    for i in s:
        if i in dic: dic[i] += 1
        else: dic[i] = 1
    sorted_dic = dict(sorted(dic.items(), key = lambda x:x[1], reverse=True))
    for key, val in sorted_dic.items():
        res += key*val 
    return res


s = input()
print(freq(s))