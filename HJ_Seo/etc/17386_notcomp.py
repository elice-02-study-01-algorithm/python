# https://www.acmicpc.net/problem/17386

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

x1,x2 = min(x1,x2),max(x1,x2)
y1,y2 = max(y1,y2),min(y1,y2)
x3,x4 = min(x3,x4),max(x3,x4)
y3,y4 = min(y3,y4),max(y3,y4)

if (x2-x1)*(y4-y3) == (x4-x3)*(y2-y1): #평행 case.
    print(0)
else:
    1
# print(0) if (x2-x1)*(y4-y3) == (x4-x3)*(y2-y1) else print(1) # 직선이 겹치면..
