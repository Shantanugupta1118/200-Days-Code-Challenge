

def row_win(r):
    if r[0]==r[1] and r[1]==r[2] and r[0]!="_":
        return True
    return False

def col_count(mat,s):
    count = 0
    for i in range(3):
        for j in range(3):
            if mat[i][j] == s:
                count+=1
    return count

def winner_approach(mat):
    win = []
    for i in range(3):
        if row_win(mat[i])==True:
            win.append(mat[i][0])
    for i in range(3):
        if row_win([mat[0][i],mat[1][i],mat[2][i]])==True:
            win.append(mat[0][i])
    d1,d2 = [],[]
    for i in range(3):
        d1.append(mat[i][i])
        d2.append(mat[i][2-i])
        
    if row_win(d1)==True:
        win.append(d1[0])
    if row_win(d2)==True:
        win.append(d2[0])
    return win

def solve(mat):
    win = winner_approach(mat)
    w = len(win)
    ww = len(set(win))
    UC = col_count(mat,'_')
    XC = col_count(mat,'X')
    OC = col_count(mat,'O')
    if UC == 9:
        return 2
    if ww>1 :
        return 3
    if XC<OC or XC>OC+1:
        return 3
    if w == 0 and UC == 0 and XC-OC == 1:
        return 1
    if ww == 1:
        if win[0]=="X" and XC-OC == 1:
            return 1
        if win[0]=="O" and XC-OC == 0:
            return 1
        else:
            return 3
    else:
        return 2
    
    

for i in range(int(input())):
    mat = []
    for i in range(3):
        re = str(input())
        r = []
        for i in re:
            r.append(i)
        mat.append(r)
    print(solve(mat))
        