# https://www.acmicpc.net/problem/1198
# 넓이의 최댓값..!..

from sys import stdin

n = int(stdin.readline().strip())

dots = tuple(tuple(map(int,stdin.readline().strip().split())) for _ in range(n))
wide = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            wide = max(wide,abs((dots[i][0]*dots[j][1]+dots[j][0]*dots[k][1]+dots[k][0]*dots[i][1])-(dots[i][0]*dots[k][1]+dots[k][0]*dots[j][1]+dots[j][0]*dots[i][1]))/2)

print(round(wide,1))