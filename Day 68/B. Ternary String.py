# Github: Shantanugupta1118
# DAY 68 of DAY 100
# B. Ternary String  -  Codeforces
# https://codeforces.com/problemset/problem/1354/B
 
class Solution:
    def solve(self):
        n = list(input())
        str_dic = {'1':0, '2':0, '3':0}
        temp_str = {}
        flag = True
        for i in n:
            if i=='0':
                n.remove(i)
        for i in n:
            if i not in temp_str:
                temp_str[i] = 1
            if '1' in temp_str and '2' in temp_str and '3' in temp_str:
                flag = False
                break
        if flag:
            return 0
        initial = 0
        sub_str = []
        while '1' not in sub_str or '2' not in sub_str or '3' not in sub_str and len(n)>initial:
            sub_str.append(n[initial])
            initial += 1
        sub_str = sub_str[::-1]
        i = 0
        for i in range(len(sub_str)):
            if str_dic['1']==0 or str_dic['2']==0 or str_dic['3']==0:
                if sub_str[i] == '1':
                    str_dic['1'] += 1
                elif sub_str[i] == '2':
                    str_dic['2'] += 1
                elif sub_str[i] == '3':
                    str_dic['3'] += 1
                i += 1
            else:
                break
        return str_dic['1']+str_dic['2']+str_dic['3']




for _ in range(int(input())):
    print(Solution().solve())