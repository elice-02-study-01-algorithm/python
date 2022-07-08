from sys import stdin

N,K,P,L = map(int,stdin.readline().strip().split())
if P == N:
    P = 0

playe = []
roun = 0
stt = 1

for i in range(K):
    playe.append([0]+list(map(int,stdin.readline().strip().split())))
    
while True:
    roun += 1
    # print('round = ',roun)
    if roun == L+1:
        print(-1)
        break
    
    for i in range(K):
        stt = (stt-playe[i][roun]) % N
        # print(stt)
        
        if stt == P:
            print(i+1,roun)
            exit(0)
    