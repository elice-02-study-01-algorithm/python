# 2 --> 3, 3 --> 4, 4 --> 7... P(n-2) 0,0,3,4,7
from sys import stdin

P = [0,0,3,4,7]

while True:
    n = stdin.readline().strip()
    if n == '':
        break
    
    n = int(n)
    
    if len(P)-1<n:
        for i in range(n-len(P)+1):
            P.append(P[-1]+P[-2])

    print(P[n])
    
# ! 종료 조건이 어떤 것일지를 생각해봐야 했다..!..
# 그래프이론의 매칭 카운트라 꿀문제..ㅇㅅㅇ