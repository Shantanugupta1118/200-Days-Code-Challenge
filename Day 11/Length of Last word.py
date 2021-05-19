# Github: Shantanugupta1118
# DAY 11 of DAY 100
# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/


def length_LW(s):
    count = 0
    ls = s.split()
    print(ls)
    for i in reversed(ls):
        if i != ' ':
            count = len(i)
            break
    return count

string = input()
print(length_LW(string))