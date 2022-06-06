n = int(input())

if n == 0:
    exit(0)

P = [1,0,1]

for i in range(n):
    k = int(input())
    
    if len(P)-2<k:
        for i in range(k):
            P.append(P[-1]+P[-2])
    
    print(P[k],P[k+1])
