# 진공청소기가 생각나서 비슷한 도구를 이용해서 풀이

def main():
    N, M = map(int, input().split())
    arrowMap = []
    for _ in range(N):
        rowList = list(map(int, input().split()))
        arrowMap.append(rowList)
    start = list(map(int, input().split()))

    # 1 상 2 좌 3 우 4 하
    dirList = [(-1,0), (0, -1), (0, 1), (1, 0)]
    
    # 지나온 자리 기록하기
    record = [start]
    while True:
        # 밖으로 나가면
        if start[0]>N or start[0]<0 or start[1]>M or start[1]<0:
            print(-1)
            return
        direction=arrowMap[start[0]-1][start[1]-1]

        start = [start[0] + dirList[direction-1][0], start[1]+dirList[direction-1][1]]
        # 지나온 자리 중에 곧 나아가는 좌표가 있다면 반복될 것임
        if start in record:
            # 지난 기록 중에 겹치는 좌표의 인덱스와 곧 들어올 것 간의 차이를 구해 길이를 구한다
            print(len(record)-record.index(start))
            return
        else:
            record.append(start)

if __name__=="__main__":
    main()