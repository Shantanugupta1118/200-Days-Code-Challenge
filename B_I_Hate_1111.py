def check2(n, ones, mx):
    print(ones)

def check11(n):
    if len(str(n)) <= 2:
        return False
    else:
        ones = []
        mx = len(str(n))
        for i in range(2,mx):
            ones.append(int('1'*i))
            if n%int('1'*i)==0:
                return True
        else:
            print(check2(n, ones, mx))



for tc in range(int(input())):
    n = int(input())
    if n%11==0: print(True)
    elif n>11: 
        print(check11(n))


