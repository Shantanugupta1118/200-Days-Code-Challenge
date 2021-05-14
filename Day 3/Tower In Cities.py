# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 3 of DAY 100
# HackWithInfy'21 - Qualification Round - Tower Installation in Cities

'''
Test Case: 

    5 //N                               |
    2  //R                              |   Output: 1
    [1,2,3,4,5]  //cities distance      |
    ---------------------------------------------------------------
    5                                   |
    0                                   |   Output: 5
    [8,16,32,4,2]                       |
    ---------------------------------------------------------------
    4                                   |
    10                                  |   Output: 2
    [42,31,5,19]                        |
    ---------------------------------------------------------------
    
'''

def sol(n, r, cities):
    cities.sort()
    numOfTower = 0
    i = 0
    while(i<n) :
        numOfTower += 1
        loc  = cities[i] + 2*r
        while (i < n and cities[i] <= loc):
            i += 1
    return numOfTower
                
def main():
    n = int(input())
    r = int(input())
    ls = []
    for i in range(n): ls.append(int(input()))
    
    print(sol(n, r, ls))

main()
