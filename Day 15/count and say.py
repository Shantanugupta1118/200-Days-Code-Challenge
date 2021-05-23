# Github: Shantanugupta1118
# DAY 15 of DAY 100
# 38 - Count and say - Interviewbit/Leetcode
# https://leetcode.com/problems/count-and-say/
# https://www.interviewbit.com/problems/count-and-say/



def main(n):
    if n==1: return "1"
    if n==2: return "11"
    s = "11"
    for i in range(3,n+1):
        s += "$"
        ls = len(s)
        count = 1
        temp = ""
        for j in range(1, ls):
            if s[j]!=s[j-1]:
                temp += str(count+0)
                temp += s[j-1]
                count = 1
            else:
                count += 1
        s = temp
    return s

n = int(input())
print(main(n))