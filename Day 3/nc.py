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