from sys import stdin

N = int(input())

x1,y1,x2,y2 = map(int,stdin.readline().strip().split())

x_min,y_min,x_max,y_max = (x1+x2)/2,(y1+y2)/2,(x1+x2)/2,(y1+y2)/2

for i in range(N-1):
    x1,y1,x2,y2 = map(int,stdin.readline().strip().split())
    x_min = min(x_min,x1)
    x_max = max(x_max,x2)
    y_min = min(y_min,y1)
    y_max = max(y_max,y2)
    
print((x_max-x_min) * (y_max-y_min))

# ! 그냥 직사각형들의 합이 아님... 직사각형이 포개져있으면 짤린 넓이를 생각해야 함.