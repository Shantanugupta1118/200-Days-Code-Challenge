# Railway Platform

def getPlatform(engines, rear, ne, nr):
    platform = 1
    for i in range(ne-1):
        if engines[i] < rear[i] and rear[i] < engines[i+1]:
            continue
        elif rear[i] >= engines[i+1]:
            platform += 1
    return platform


n_engines = int(input())
engines = []
for i in range(n_engines): engines.append(int(input()))
n_rear = int(input())
rear = []
for i in range(n_rear): rear.append(int(input()))

print(getPlatform(engines, rear, n_engines, n_rear))