# https://www.acmicpc.net/problem/1697

from sys import stdin

N,K = map(int,stdin.readline().strip().split())

def nums(poss):
    temp = set()
    for i in poss:
        if i-1 > -1 and i-1 not in temp2:
            temp.add(i-1)
            temp2.add(i-1)
        if i+1 <= 100000 and i+1 not in temp2:
            temp.add(i+1)
            temp2.add(i+1)
        if 2*i <= 100000 and 2*i not in temp2:
            temp.add(2*i)
            temp2.add(2*i)
        
    return temp

M = 0
temp = {N}
temp2 = set()
while True:
    if K in temp:
        print(M)
        break
    
    temp = nums(temp)
    M += 1
    
# 상한도 필요했다..