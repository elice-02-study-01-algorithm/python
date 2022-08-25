'''
# 시간 초과
import sys
input = sys.stdin.readline

testCaseNum = int(input())

for _ in range(testCaseNum):

    doubleBreak = False
    funcOrder = list(input().strip())
    seqNumber = int(input())
    seqInteger = list(input().strip()[1:-1].split(","))
    
    if seqInteger != ['']:
        seqInteger = list(map(int, seqInteger))
    elif funcOrder[0] == 'D':
        print('error')
        continue

    for order in funcOrder:
        if order == 'R':
            seqInteger = seqInteger[::-1]
        else:
            # RD 0 [] -> error
            if seqInteger == [''] or seqInteger == []:
                print('error')
                doubleBreak = True
                continue
            else:
                seqInteger = seqInteger[1:]
    if doubleBreak == False:
        # R 0 [] -> []
        if seqInteger == ['']:
            print([])
        else:
            print(str(seqInteger).replace(" ", ""))
'''
# 뒤집기 arr[::-1]를 줄이기 위해 다른 아이디어 도입
# 뒤집기를 실제로 하지 말고, 뒤집기 index를 따로 만들어서 순차면 0, 역순이면 -1
import sys
input = sys.stdin.readline

testCaseNum = int(input())

for _ in range(testCaseNum):

    doubleBreak = False

    funcOrder = list(input().strip())
    seqNumber = int(input())
    seqInteger = list(input().strip()[1:-1].split(","))

    reverseIndex = 0

    # 빈 배열로 들어오는 경우 ['']으로 들어온다.
    # 빈 배열이자 처음으로 'D'가 나오면 바로 error 반환하기
    if seqInteger != ['']:
        # 수를 받을 때 문자열 형태로 넣어버려서 다시 정수 형태로 바꿔주기
        seqInteger = list(map(int, seqInteger))
    elif funcOrder[0] == 'D':
        print('error')
        # for문 끝까지 패스하기
        continue

    # 함수 하나씩 실행하기
    for order in funcOrder:
        # 뒤집기의 경우 index만 교체해주기
        if order == 'R':
            if reverseIndex == 0:
                reverseIndex = -1
            else:
                reverseIndex = 0

        # 지우기의 경우
        else:
            # `RD 0 [] -> error`를 위해 seqInteger == [''] 추가
            if seqInteger == [''] or seqInteger == []:
                print('error')
                doubleBreak = True
                break
            else:
                # 역순일 경우 맨 끝의 것을 지우기
                if reverseIndex == -1:
                    seqInteger.pop()
                # 순차일 경우 맨 앞의 것을 지우기
                else:
                    seqInteger.pop(0)
    
    # 앞서 error가 출력되지 않은 경우
    if doubleBreak == False:
        # `R 0 [] -> []`를 위해 처리
        if seqInteger == ['']:
            print([])
        else:
            if reverseIndex == -1:
                # 솔직히 출력 여기서 틀렸습니다 뜨는 건 예의가 아니다...
                print(str(seqInteger[::-1]).replace(" ", ""))
            else:
                print(str(seqInteger).replace(" ", ""))
