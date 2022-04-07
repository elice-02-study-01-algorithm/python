## 백준
## 2630번 : 색종이 만들기
## 분할 정복, 재귀

##* 문제 규칙
## 모두 같은 색으로 칠해져 있지 않으면 중간 부분 자름
## 종료 조건 : 모두 같은색, 하나의 정사각형 될경우
## 하얀색 0, 파란색 1
## 출력 첫째줄 : 하얀색 색종이 개수, 둘째줄 : 파란색 색종이 개수


def makepaper(x, y, N):
    global wCount, bCount
    color = paper[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                makepaper(x, y, N//2)
                makepaper(x, y+N//2, N//2)
                makepaper(x+N//2, y, N//2)
                makepaper(x+N//2, y+N//2, N//2)
                return

    if color == 0:
        wCount += 1
    else:
        bCount += 1


if __name__ == "__main__":
    N = int(input())  # N : 한변의 길이 ( N=2k, k는 1 이상 7 이하의 자연수 )
    paper = [list(map(int, input().split())) for _ in range(N)]
    wCount, bCount = 0, 0

    makepaper(0, 0, N)
    print(wCount)
    print(bCount)
