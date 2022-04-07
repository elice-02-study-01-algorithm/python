# b3 분산처리
n = int(input())

for _ in range(n):
    a,b = map(int,input().strip().split())
    a = a%10
    c=[a]
    
    for i in range(b):
        d = (c[-1]*a)%10
        if d in c:
            break
        c.append(d)

    e = b%len(c)
    if c[e-1] ==0:
        print(10)
    else:
        print(c[e-1])

# 7을 제곱했을때 1의자리. 7 9 3 1
# 3을 제곱했을 때 1의 자리. 3 9 7 1 ... 