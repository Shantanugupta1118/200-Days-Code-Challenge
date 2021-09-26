
n = int(input())
new_code = ""
while n>0:
    new_code += chr(abs(n%10+97))
    n = n//10
print(new_code[::-1])
