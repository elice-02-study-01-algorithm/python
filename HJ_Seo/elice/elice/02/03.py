from sys import stdin

N = int(stdin.readline().strip())

dot = []

for i in range(N):
    dot.append(tuple(map(int,stdin.readline().strip().split())))

dot = sorted(dot)

rst = 0
for i in range(1,N):
    rst += (dot[i][0]-dot[i-1][0]) * (( dot[i][1] + dot[i-1][1])/2)


# print(rst)

if rst%1 == 0:
    print(int(rst))
else:
    print(rst)