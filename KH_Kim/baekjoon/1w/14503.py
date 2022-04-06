# 백준
# 타입 : 구현, 시뮬레이션
# 14503번 : 로봇 청소기

##* N*M 크기 (3 <= N,M <= 50) | N:세로, M:가로
##* 위치: 북쪽에서부터 r번째, 서쪽에서부터 c번째 (r,c)
##* d:바라보는방향 | (0:북쪽), (1:동쪽), (2:남쪽), (3:서쪽)
##* 빈칸:0, 벽:1, 지도의 가장자리 칸은 모두 벽



def clean(row, col):
    space[row][col] = 2  #! 1로 바꿀시 case2 20뜸
    global cleanCount
    cleanCount += 1
    return

# d = [0, 1, 2, 3] | [북, 동, 남, 서]
# 방법 2)) 왼쪽회전후 d값 : (n+4-1)%4
def turnLeft(direction):
    global d  # d값 갱신
    global turnCount
    if direction== 0:
        d = 3
    elif direction == 1:
        d = 0
    elif direction == 2:
        d = 1
    elif direction == 3:
        d = 2
    turnCount += 1
    return

def isLeftDirty(row, col, direction):
    if direction== 0:
        if space[row][col-1] == 0:
            return True
    elif direction == 1:
        if space[row-1][col] == 0:
            return True
    elif direction == 2:
        if space[row][col+1] == 0:
            return True
    elif direction == 3:
        if space[row+1][col] == 0:
            return True
    else:
        return False
            
def goStraight(row, col, direction):
    global r
    global c
    global turnCount
    if direction == 0:
        r = row - 1
    elif direction == 1:
        c = col + 1
    elif direction == 2:
        r = row + 1
    elif direction == 3:
        c = col - 1
    turnCount = 0
    return

def isBackEmpty(row, col, direction):
    if direction == 0:
        if space[row+1][col] != 1:
            return True
    elif direction == 1:
        if space[row][col-1] != 1:
            return True
    elif direction == 2:
        if space[row-1][col] != 1:
            return True
    elif direction == 3:
        if space[row][col+1] != 1:
            return True
    else:
        return False
    
def goBack(row, col, direction):
    global r
    global c
    global turnCount
    if direction == 0:
        r = row + 1
    elif direction == 1:
        c = col - 1
    elif direction == 2:
        r = row - 1
    elif direction == 3:
        c = col + 1
    turnCount = 0
    return


if __name__ == '__main__':
    N, M = map(int, input().split())       # 세로, 가로
    r, c, d = map(int, input().split())     # r행 c열, d방향
    space = [list(map(int, input().split())) for _ in range(N)]
    turnCount = 0       # 한 자리에서 왼쪽으로 방향을 바꾼 횟수
    cleanCount = 0      # 청소한 위치 개수

    clean(r,c) # 시작 세팅
    while True:
        if isLeftDirty(r,c,d):  # 왼쪽 0일시 True
            turnLeft(d)         # d 갱신
            goStraight(r,c,d)   # 갱신된 d에 맞춰서 이동
            clean(r,c)          # loop
        else:                   # 왼쪽 0 False
            turnLeft(d)    
            if turnCount == 4:
                if isBackEmpty(r,c,d):  # 벽이 아닐경우 True
                    goBack(r,c,d)
                else:
                    break
                    
    print(cleanCount)