from sys import stdin

N = int(input())

cnt = 0
for i in range(N):
    ABstr = stdin.readline().strip()
    checktype = [0]
    
    for j in ABstr:
        if checktype[-1] != j:
            checktype.append(j)
        else:
            checktype = checktype[:-1]
    
    if len(checktype) == 1:
        cnt += 1
    
print(cnt)