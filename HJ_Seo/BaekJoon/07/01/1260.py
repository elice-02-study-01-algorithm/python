# https://www.acmicpc.net/problem/1260

from sys import stdin
from collections import deque

def dfs(graph,start):
    for i in range(V+1):
        if graph[start][i] == 1 and i not in dfs_lst:
            dfs_lst.append(i)
            dfs(graph,i)
# done..

def bfs(graph,start):
    Q = deque()
    Q.append(start)
    
    while len(Q) != 0:
        v = Q.popleft()
        for i in range(V+1):
            if graph[v][i] == 1 and i not in bfs_lst:
                Q.append(i)
                bfs_lst.append(i)

V,E,start = map(int,stdin.readline().strip().split())

graph = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    v1,v2 = map(int,stdin.readline().strip().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

dfs_lst = [start]
bfs_lst = [start]

dfs(graph,start)
bfs(graph,start)

print(*dfs_lst)
print(*bfs_lst)
