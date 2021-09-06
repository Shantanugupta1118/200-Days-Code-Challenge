
def check_prime(n):
    n = int(n)
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True
    # print(n)

n = input()
x = []
summ = 0
for i in range(len(n)):
    for j in range(i,len(n)-1):
        if int(n[i:j+1]) not in x:
            if check_prime(n[i:j+1]):
                summ += int(n[i:j+1])
                # print(int(n[i:j+1]))
                x.append(int(n[i:j+1]))

# print(summ)















print(28)