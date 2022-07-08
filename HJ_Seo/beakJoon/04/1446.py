from sys import stdin
from collections import deque

n, rang = map(int,stdin.readline().strip().split()) #지금길의 갯수, 길이. 0<= n <=12, 0<= rang <= 10000
start = 0

roads = {}
for _ in range(n):
    a,b,c = map(int,stdin.readline().strip().split()) #a < b.
    if b > rang: #목표지점을 지나면 빠꾸가 안됨.
        continue 
    
    if b - a > c: #지름길의 길이가 원래보다 길어도 pass.
        if (a,b) not in roads:
            roads[(a,b)] = c
        else:
            roads[(a,b)] = min(roads[(a,b)],c) #지름길의 시/종점이 같은게 있으면 짧은거 pick.

pick_roads = sorted([[i] for i in roads])
roads_lst = sorted([i for i in roads])
dn = 0


# !  roads_lst 구하기.


rang_result = rang

for i in pick_roads:
    temp = rang
    for j in i:
        temp += roads[j] - (j[1]-j[0]) # i에 있는 각각의 j에 대해 + 지금길의 길이 - 원래 길의 길이

    rang_result = min(rang,temp)
    
print(rang_result)