from sys import stdin

N,mod = map(int,input().strip().split())

# inital code. 역시 시간초과가 나오네... #! python 및 pypy로 돌아가지 않음.
lst=[]

def checknum(lst,mod):
    for i in range(len(lst)):
        if len(set(lst[i:])) != mod:
            break
    return len(lst) - i + 1

for _ in range(N):
    run = stdin.readline()
    
    if run[0] == '1':
        lst.append(int(run[2:])%mod)
    elif run[0] == '2' and len(lst)>0:
        lst.pop()
    elif run[0] == '3':
        if len(set(lst)) != mod:
            print(-1)
        else:
            print(checknum(lst,mod))
            