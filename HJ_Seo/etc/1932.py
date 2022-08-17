# https://www.acmicpc.net/problem/1932

from sys import stdin

num = int(stdin.readline().strip())
# lst = [[int(stdin.readline().strip())]]
lst = []
for _ in range(num):
    lst.append(list(map(int,stdin.readline().strip().split())))
    
for i in range(1,num):
    for j in range(i+1):
        if j == 0:
            lst[i][j] += lst[i-1][j]
        elif j == i:
            lst[i][j] += lst[i-1][-1]
        else:
            lst[i][j] += max(lst[i-1][j-1:j+1])
    # print(lst[i])
            
print(max(lst[-1]))
