# https://www.acmicpc.net/problem/2178

from sys import stdin

N,M = map(int,stdin.readline().strip().split())

def check_update(lst,num):
    new_lst = set()
    dx = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in lst:
        for j in dx:
            if 0 <= i[0]+j[0] and i[0]+j[0] < N and 0 <= i[1]+j[1] and i[1]+j[1] < M:
                if leng[i[0]+j[0]][i[1]+j[1]] > num and Tmap[i[0]+j[0]][i[1]+j[1]] != '0':
                    new_lst.add((i[0]+j[0],i[1]+j[1]))
    # print(new_lst)
    return new_lst

leng = [[10001 for _ in range(M)] for _ in range(N)]

Tmap = [stdin.readline().strip() for _ in range(N)]

x = {(0,0)}
num = 1

while True:
    if leng[-1][-1] != 10001:
        print(leng[-1][-1])
        break
    
    for i in x:
        leng[i[0]][i[1]] = num

    x = check_update(x,num)
    
    num += 1
