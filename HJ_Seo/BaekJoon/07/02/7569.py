from sys import stdin
from collections import deque

M,N,H = map(int,stdin.readline().strip().split()) 
tomatos = []
Q = deque()
 
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int,stdin.readline().strip().split())))
        for k in range(M):
            if temp[j][k] == 1:
                Q.append((i,j,k))
    tomatos.append(temp)

d = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

while Q:
    x,y,z = Q.popleft()
    
    for i in d:
        a = x + i[0]
        b = y + i[1]
        c = z + i[2]
        if 0 <= a < H and 0 <= b < N and 0 <= c < M and tomatos[a][b][c] == 0:
            Q.append((a,b,c))
            tomatos[a][b][c] = tomatos[x][y][z] + 1
    
result = 0
for i in tomatos:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        result = max(result,max(j))

print(result - 1)

# N*M*H번 반복되었는데 0이 남아있으면 print(-1)... X.. deque를 쓰자.

'''
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
[[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]..
wanted ons-step output : 
[[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]]
'''