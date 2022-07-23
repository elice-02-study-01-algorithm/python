from sys import stdin
# hint : power[i][j] i번째 날 j번째 도시에 있을 때 최소 피로도..
N,M = map(int,stdin.readline().strip().split())

D_i = [int(stdin.readline().strip()) for _ in range(N)]
C_i = [int(stdin.readline().strip()) for _ in range(M)]

need = [[0]*(N+1)] + [[float('inf')]*(N+1) for _ in range(M)]
for i in range(1,M+1):
    need[i][0] = 0
    
day = 1
# need[1][1] = C_i[0]*D_i[0]

while M != day:
    for i in range(day):
        for j in range(min(N,day)):
            need[i][j] = min(need[i][j],min(need[i][:j+1])+C_i[i]*D_i[j])

    day += 1
    
for i in need:
    print(i)