from sys import stdin

N = int(stdin.readline().strip())

dot = {}

for i in range(N):
    x,y = map(int,stdin.readline().strip().split())
    
    if x not in dot:
        dot[x] = 0
    dot[x] = max(dot[x],y)

# print(dot)
dot_x = sorted(dot)

rst = 0
for i in range(1,len(dot_x)):
    rst += (dot_x[i]-dot_x[i-1]) * (( dot[dot_x[i]] + dot[dot_x[i-1]])/2)


# print(rst)

if rst%1 == 0:
    print(int(rst))
else:
    print(rst)