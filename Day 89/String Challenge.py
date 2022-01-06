
s = input()
res = []

count = 0
temp = 1
flag = False
for i in range(len(s)-1):
    # print(temp, s[i])
    if s[i]==s[i+1]:
        temp += 1
    elif s[i]!=s[i+1]:
        if int(s[i]) <= temp:
            flag = True
            break
        else:
            temp = 1
        
print(flag)

