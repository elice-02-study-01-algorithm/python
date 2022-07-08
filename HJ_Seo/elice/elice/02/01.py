from sys import stdin

N,h = map(int,stdin.readline().strip().split())

result=[-1,0]
lst = []
for i in range(N):
    loc,hei,typ = map(int,stdin.readline().strip().split())
    
    if hei>h and typ == 3:
        if result[0] == -1:
            result[0] = loc
        else:
            result[0] = min(result[0],loc)
    
    lst.append((loc,hei,typ))

if result[0] != -1:
    for i in lst:
        if i[1]>h and i[2] == 1 and i[0]<result[0]:
            result[1] += 1
else:
    for i in lst:
        if i[1]>h and i[2] == 1:
            result[1] += 1

print(*result)

# 오답케이스 2개.. 뭐지?
# fix. --> 레이저가 멈추지 않는 케이스 2개.
