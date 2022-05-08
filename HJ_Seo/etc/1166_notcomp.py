# 상자가 들어갈 수 있는 최대 갯수 = L//A * W//A * H//A..
# 상자의 갯수 = N..
# N, L, W, H가 주어질 때 max(A) = ?.... 오차는 10**-9 까지.
#! 어려운데..?..

N, L, W, H = map(int,input().strip().split())

if N < min(L,W,H):
    print(0)
    exit(0)

unit = 0
nbr = 1
cnt = 0
while True:
    if cnt == 14:
        print(unit)
        break
    
    Ldiv = L//(unit+nbr)
    Wdiv = W//(unit+nbr)
    Hidv = H//(unit+nbr)
    if Ldiv * Wdiv * Hidv >= N:
        unit += nbr
    else:
        nbr = nbr/10
        cnt += 1
