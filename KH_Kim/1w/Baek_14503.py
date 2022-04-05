# 백준
# 타입 : 구현, 시뮬레이션
# 14503번 : 로봇 청소기

##* N*M 크기 (3 <= N,M <= 50) | N:세로, M:가로
##* 위치: 북쪽에서부터 r번째, 서쪽에서부터 c번째 (r,c)
##* d:바라보는방향 | (0:북쪽), (1:동쪽), (2:남쪽), (3:서쪽)
##* 빈칸:0, 벽:1, 지도의 가장자리 칸은 모두 벽

# d = [0, 1, 2, 3]
# 왼쪽회전후 d값 : (n+4-1)%4
def spin(d):
    new_d= (d+4-1) % 4
    return new_d

# d에 따른 이동할 위치
def changeD(r,c,d):
    if d == 0:
        rm = r
        cm = c - 1
        return rm, cm
    elif d == 3:
        r += 1
        return r, c
    elif d == 2:
        c += 1
        return r, c
    else:
        r -= 1
        return r, c

def robotmove(r,c,d,floor):
    count = 0 # 청소한 칸 갯수
    spin_count = 0
    while spin_count <4:
        nowpos = floor[r][c] # 현재 위치
        # clean
        print('one', count)
        if nowpos == 0:
            floor[r][c] = 1  # 1.clean
            #! nowpos = 1 ??? call by ??
            count +=1
            print('two',count)
        rm, cm = changeD(r, c, d)
        print('rm,cm: ',rm, cm)

        # 현 위치 왼쪽에 0인경우 회전 후 전진
        # 1인경우 회전 -> 왼쪽이 0인지 파악 후 반복
        
        if floor[rm][cm] == 0:
            r = rm
            c = cm
            d = spin(d)
            spin_count = 0
        elif spin_count < 3:
            d = spin(d)
            spin_count += 1
        else:
            spin_count += 1
            pass
        print('r,c::',r,c)
        print('d:',d)
        print('spincount:',spin_count)
    return count

#! case1 통과
#! case2 count = 20??

if __name__ == '__main__':
    N, M = map(int,input().strip().split())
    r,c,d = map(int,input().strip().split())

    floor = [[] for i in range(N)]   
    for i in range(N):
        floor[i] = list(map(int,input().strip().split()))  


    print(robotmove(r,c,d,floor))
    # print(floor[1])
    # print(floor[1][1])
