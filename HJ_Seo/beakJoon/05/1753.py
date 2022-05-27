from math import inf
from sys import stdin, setrecursionlimit

setrecursionlimit(100000)

v,e = map(int,stdin.readline().strip().split())
stt = int(stdin.readline().strip())

dist = [inf for _ in range(v+1)]
dist[stt] = 0
visited = [False for _ in range(v+1)]

G = dict()
for _ in range(e):
    a,b,c = map(int,stdin.readline().strip().split())
    
    if dist[a] != inf:
        dist[b] = min(dist[b],dist[a]+c)

    if (a,b) not in G:
        G[(a,b)] = inf
    G[(a,b)] = min(G[(a,b)],c)

n = 0
while len(G) != 0:
    if n > len(G)+1:
        break
    
    G_keys = tuple(G.keys())
    for i in range(len(G_keys)):
        print(dist[5])
        if dist[G_keys[i][0]] != inf:
            init = G_keys[i][0]
            des = G_keys[i][1]
            cost = G.pop(G_keys[i])
            
            if dist[des] > dist[init] + cost:
                dist[des] = dist[init] + cost
                n = 0
        else:
            n += 1

for i in range(1,v+1):
    if dist[i] == inf:
        print('INF')
    else:
        print(dist[i])

# print(dist)
# while True:  # ! 이게 시간초과의 원인.
#     mini = inf
#     vtx = -1
#     for i in range(v):
#         if visited[i] == False and dist[i] < mini:
#             mini = dist[i]
#             vtx = i
    
#     if mini == inf:
#         break
    
#     visited[vtx] = True
    
#     for i in range(len(G)):
#         if vtx == G_keys[i][0]:
#             des = G_keys[i][1]
#             cost = G[G_keys[i]]    
        
#             if dist[des] > dist[vtx] + cost:
#                 dist[des] = dist[vtx] + cost
    
    
# for i in range(1,v+1):
#     if dist[i] == inf:
#         print('INF')
#     else:
#         print(dist[i])

# ! from elice.. timeover.
# v,e = map(int,stdin.readline().strip().split())
# stt = int(stdin.readline().strip())

# dist = [0] + [inf for _ in range(v)]
# dist[stt] = 0
# visited = [False for _ in range(v+1)]
# visited[0] = True

# G = dict()
# for _ in range(e):
#     a,b,c = map(int,stdin.readline().strip().split())
    
#     if (a,b) not in G:
#         G[(a,b)] = inf
#     G[(a,b)] = min(G[(a,b)],c)
    
# G_edge = sorted(G)

# while True:
#     mini = inf
#     vtx = -1
#     for i in range(v):
#         if visited[i] == False and dist[i] < mini:
#             mini = dist[i]
#             vtx = i
    
#     if mini == inf:
#         break
    
#     visited[vtx] = True
    
#     for i in range(len(G_edge)):
#         if vtx == G_edge[i][0]:
#             des = G_edge[i][1]
#             cost = G[G_edge[i]]    
        
#             if dist[des] > dist[vtx] + cost:
#                 dist[des] = dist[vtx] + cost
        
# for i in range(1,v+1):
#     if dist[i] == inf:
#         print('INF')
#     else:
#         print(dist[i])
