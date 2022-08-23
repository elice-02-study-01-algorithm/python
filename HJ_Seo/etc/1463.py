n = int(input())

if n == 1:
    print(0)
    exit(0)

init = {n}
next = set()
cnt = 1
total = [False]*(n+1)
total[n] = True

while True:
    for i in init:
        if i-1>0 and not total[i-1]:
            next.add(i-1)
            total[i-1] = True
        if i%2 == 0 and i//2>0:
            if not total[i//2]:
                next.add(i//2)
                total[i//2] = True
        if i%3 == 0 and i//3>0:
            if not total[i//3]:
                next.add(i//3)
                total[i//3] = True
            
    if 1 in next:
        print(cnt)
        break
    
    init = next
    next = set()
    
    cnt += 1    
