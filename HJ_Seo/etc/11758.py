# https://www.acmicpc.net/problem/11758

dots = [tuple(map(int,input().split())) for _ in range(3)]
a,b,c = dots

if (b[0]-a[0])*(c[1]-a[1]) == (c[0]-a[0])*(b[1]-a[1]):
    print(0)
elif (b[0]-a[0])*(c[1]-a[1]) > (c[0]-a[0])*(b[1]-a[1]):
    print(1)
else:
    print(-1)