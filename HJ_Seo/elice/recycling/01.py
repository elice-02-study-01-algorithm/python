from sys import stdin

def main():
    N,K,P,L = map(int,stdin.readline().strip().split())

    if P == N:
        P = 0
    
    player = [[0]+list(map(int,stdin.readline().strip().split())) for _ in range(K)]
    roun = 0
    stt = 1

    while True:
        roun += 1
        if roun == L+1:
            print(-1)
            return
        
        for i in range(K):
            stt = (stt-player[i][roun])%N

            if stt == P:
                print(i+1,roun)
                return

if __name__=="__main__":
    main()