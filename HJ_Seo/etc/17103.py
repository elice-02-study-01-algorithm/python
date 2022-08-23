# https://www.acmicpc.net/problem/17103

from sys import stdin
        
Prime = [False,False] + [True for _ in range(1000000)]
for i in range(1000000):
    if Prime[i] == True:
        for j in range(2*i,1000000,i):
            Prime[j] = False

cases = int(stdin.readline().strip())

for _ in range(cases):
    case = 0
    num = int(stdin.readline().strip())
    for i in range(2,num//2+1):
        if Prime[i] and Prime[num-i]:
            case += 1
    
    print(case)