'''
r의 경우: 1 또는 2번째 구간 <2**(N-1)<= 3 또는 4번째 구간
c의 경우: 1 또는 3번째 구간 <2**(N-1)<= 2 또는 4번째 구간

구간이 정해지면 숫자 범위가 정해짐
14의 경우
r=3 c=2
N = 3
N = 2 (4)
    3 -> 1, 2번째 구간
    2 -> 1, 3번째 구간
    => 1번째 구간 (0-15)
N = 1 (2)
    3 -> 3, 4번째 구간
    2 -> 2 또는 4번째 구간
    => 4번째 구간 (12-15)
    [2번째 구간인 경우 c=c-2**N]
    [3번째 구간인 경우 r=r-2**N]
    [4번째 구간인 경우 r=r-2**N, c=c-2**N]
N = 0 (1)
    (1, 0)
    1 -> 3, 4번째 구간
    0 -> 1, 3번째 구간
    => 3번째 구간(14)

38의 경우
r=5 c=2
N=3
N=2 (4)
    5 -> 3, 4번째 구간
    2 -> 1, 3번째 구간
    => 3번째 구간 (32-47)
    r=r-2**N
N=1 (2)
    1 2
    1 -> 1, 2번째 구간
    2 -> 2, 4번째 구간
    => 2번째 구간 (36-39)
N=0 (1)
    1 0
    1 -> 3, 4번째 구간
    0 -> 1, 3번째 구간
    => 3번째 구간 (38)
'''

# 구간이 리스트 range로 주어졌을 때 N번째 구간인 경우 구간 자르기/값 정하기
def rangeNum(n, rangeInfo):
    start, end = rangeInfo
    rangeLength = end - start + 1
    rangeDivLength = rangeLength//4
    if rangeDivLength == 1:
        return rangeInfo[0] + n - 1
    return (start+(n-1)*(rangeDivLength), start+n*(rangeDivLength)-1)

N, r, c = map(int, input().split())

rangeInfo = (0, (2**N)**2-1)

while N>0:
    N -= 1
    rangeNth = 0
    # 행, 열 정보에 따라 구간을 확정짓기 위한 Boolean
    row1or2 = True if r < 2**N else False
    col1or3 = True if c < 2**N else False
    if row1or2 and col1or3:
        rangeNth = 1
    elif row1or2 and not col1or3:
        c=c-2**N
        rangeNth = 2
    elif not row1or2 and col1or3:
        r=r-2**N
        rangeNth = 3
    else:
        r=r-2**N
        c=c-2**N
        rangeNth = 4
    # 구간이 확정되면 해당 정보와 전체 range로 한 단계 낮은 range 뽑아내기
    rangeInfo = rangeNum(rangeNth, rangeInfo)

print(rangeInfo)
