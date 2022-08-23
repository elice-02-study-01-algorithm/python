from sys import stdin

num = int(stdin.readline().strip())
lst = list(map(int,stdin.readline().strip().split()))
x = lst[0]
tmp = []
start = 0
for i in range(num):
    if lst[i] != x:
        tmp.extend([i+1]*(i-start))
        start = i
        x = lst[i]

tmp.extend([-1]*(num-start))

print(*tmp)