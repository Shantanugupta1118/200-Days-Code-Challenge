def upgrade(place,uid):
    indx = solution.status[place]
    node = solution.lst[indx]
    if node.locked==True:
        return False
    temp = indx
    queue = []
    queue.append(temp)
    m = solution.child
    while queue:
        j = queue.pop(0)
        if solution.lst[j].uid != uid and j!=indx:
            return False
        for k in range(j*m+1,j*m+m+1):
            if k<=solution.n-1:
                queue.append(k)
            
        
    temp = indx
    queue = []
    queue.append(temp)
    cchild = 0
    while queue:
        cchild+=1
        j = queue.pop(0)
        solution.lst[j].countDesc = 0
        solution.lst[j].uid = None
        solution.lst[j].locked = False
        for k in range(j*m+1,j*m+m+1):
            if k<=solution.n-1:
                queue.append(k)
    node.countDesc  = 1
    node.locked = True
    node.uid = uid

    temp = indx
    while temp>=0:
        if temp!=indx:
            solution.lst[temp].countDesc +=1
            solution.lst[temp].countDesc -=cchild
        temp = (temp-1)//solution.child
    return True

def unlock(place,uid):
    indx = solution.status[place]
    node = solution.lst[indx]
    if node.locked == False or node.uid!=uid:
        return False
    else:
        node.locked = False
        node.countDesc +=1
        node.uid = None
        temp = indx
        
        while temp>0:
            solution.lst[temp].countDesc -=1
            temp = (temp-1)//solution.child
        return True

def lock(place,uid):
    indx = solution.status[place]
    node = solution.lst[indx]
    if node.locked==True:
        return False
    elif node.countDesc>0:
        return False
    else:
        temp = indx
        while temp>=0:
            if solution.lst[temp].locked == True:
                return False
            temp = (temp-1)//solution.child
        node.locked = True
        node.countDesc-=1
        node.uid = uid
        
        temp = indx
        while temp>=0:
            solution.lst[temp].countDesc +=1
            temp = (temp-1)//solution.child
        return True

class Node:
    def __init__(self,data):
        self.data = data
        self.locked = False
        self.countDesc = 0
        self.uid = None
    

class Narray:
    def __init__(self,n,child):
        self.lst = []
        self.status = {}
        self.child = child
        self.n = n

n = int(input())
cn = int(input())

apis = int(input())
solution = Narray(n,cn)

for i in range(n):
    place = input()
    node = Node(place)
    solution.status[node.data] = i
    solution.lst.append(node)

for _ in range(apis):
    op,place,uid = map(str,input().split())
    op = int(op)
    uid = int(uid)
    if op==1:
        print(lock(place,uid))
    elif op==2:
        print(unlock(place,uid))
    elif op==3:
        print(upgrade(place,uid))