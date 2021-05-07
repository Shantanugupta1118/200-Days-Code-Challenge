# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 1 of DAY 100
# INFYTQ HackWithInfy - 2021 - Garland for Diwali



# Brute Force - O(n) Run Time Complexity
def main():
    def solution(a, b, c, x, y):
        a.sort()
        for ele in a:
            if ele<0:
                b.append(ele)
            else: c.append(ele)
        start = len(b)//3
        end = sum(c)
        return end-start

    x = int(input()) #2
    y = int(input()) #6
    a, b, c = [],[],[]
    for i in range(y):
        a.append(int(input())) #[3,-1,2,-4,5,-4]
    print(solution(a, b, c, x, y))

main()