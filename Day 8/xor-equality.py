# // GitHub ID: @Shantanugupta1118
# // Day 8 of 100
# // Xor Equality   -  codechef/MAY21

MOD = 10**9+7

def equality(n, x=2):
    res = 1
    x %= MOD
    if x==0: return 0
    while n>0:
        if n&1 != 0:
            res = (res*x)%MOD
        n = n>>1
        x = (x*x)%MOD
    return res



def main():
    for _ in range(int(input())):
        n = int(input())
        print(equality(n-1))

main()