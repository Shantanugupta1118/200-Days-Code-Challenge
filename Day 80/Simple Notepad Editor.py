# Github: Shantanugupta1118
# DAY 80 of DAY 100


import sys

class notepad:
    def __init__(self):
        self.cache = []
        self.ans = ""
        
    def append(self, value):
        self.cache.append(self.ans)
        self.ans += value
    
    def delete(self, k):
        self.cache.append(self.ans)
        self.ans = self.ans[:len(self.ans)-k]
    
    def display(self, idx):
        if self.ans == "": return
        print(self.ans[idx-1])
        # self.cache.append("")
        
    def undo(self):
        if self.cache is None:
            return 
        self.ans = self.cache[-1]
        # print("___  ",self.cache)
        # print("<<>>  ",self.ans)
        self.cache.pop()
        


q = int(input())
Oprations = notepad()
for i in range(q):
    # opratn = list(map(str, input().split()))
    opratn = input().strip().split(' ')    
    # idx = input()
    if opratn[0] == "1":
        Oprations.append(opratn[1])
    elif opratn[0] == "2":
        Oprations.delete(int(opratn[1]))
    elif opratn[0] == "3":
        Oprations.display(int(opratn[1]))
    else:
        Oprations.undo()
# print("-->  ",Oprations.ans)

