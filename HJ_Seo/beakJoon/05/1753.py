from math import inf
from sys import stdin

v,e = map(int,stdin.readline().strip().split())
stt = int(stdin.readline().strip())

dist = [inf for _ in range(v)]
dist[stt] = 0
des = [False for _ in range(v)]

G = dict()
for _ in range(e):
    a,b,c = map(int,stdin.readline().strip().split())
    
    if (min(a,b),max(a,b)) not in G:
        G[(min(a,b),max(a,b))] = inf
    G[(min(a,b),max(a,b))] = min(G[(min(a,b),max(a,b))],c)
    
G_edge = sorted(G)

while True:
    mini = inf
    aim = 0
    for i in range(len(G_edge)):
        break
