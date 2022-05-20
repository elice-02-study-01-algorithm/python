from sys import stdin

N = int(stdin.readline())

lst = []

for _ in range(N):
    lst.append(list(map(int,stdin.readline().strip().split())))
    
lst = sorted(lst,key = lambda x: (x[0],x[1]))

for i in lst:
    print(*i)
