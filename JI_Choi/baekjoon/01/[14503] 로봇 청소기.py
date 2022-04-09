N, M = map(int, input().split())       # 세로, 가로
r, c, d = map(int, input().split())     # r행 c열, d방향
space = [list(map(int, input().split())) for _ in range(N)]
turnCount = 0       # 한 자리에서 왼쪽으로 방향을 바꾼 횟수
cleanCount = 0      # 청소한 위치 개수

def clean(row, col):
    space[row][col] = 2
    global cleanCount
    cleanCount += 1
    return

def turnLeft(direction):
    global d
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

### 청소 ###
clean(r,c)
while True:
    if isLeftDirty(r,c,d):
        turnLeft(d)
        goStraight(r,c,d)
        clean(r,c)
    else:
        turnLeft(d)    
        if turnCount == 4:
            if isBackEmpty(r,c,d):
                goBack(r,c,d)
            else:
                break
                
print(cleanCount)