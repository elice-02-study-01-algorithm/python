# 백준
# 16120번 : PPAP
# 자료구조, 그리디 알고리즘, 스택

# * 문제 규칙
# PPAP 문자열 O -> PPAP
# PPAP 문자열 X => NP
import sys


def ppapProgram(data):
    stack = []
    # print('길이 :', len(data))
    for i in range(len(data)):
        # print(data[i])
        stack.append(data[i])
        # print(stack)
    # stack.pop()
    # print('stack:', stack)

    # ! 파이썬 do while 문이 없음🤔
    i = 0
    while True:
        # task()
        temp = stack[i:i+4]
        # print('temp: ', temp)
        # classifier = print(*temp)
        classifier = ''.join(temp)
        # print('식별:', classifier)
        if classifier == 'PPAP':
            del stack[i]
            del stack[i]
            del stack[i]
            del stack[i]
            stack.insert(i, 'P')
            # print('delstack: ', stack)
            # i = 0
        else:
            i += 1

    # 종료 조건 1) 길이 4  len(data) == 4
    # 종료 조건 2) i가 끝일때
        if i < len(stack)-4:
            continue
        break
    # print('finalstack: ', stack)
    return stack


if __name__ == '__main__':
    data = sys.stdin.readline().strip()
    temp = ppapProgram(data)
    result = ''.join(temp)
    if result == 'PPAP':
        print(result)
    else:
        print('NP')


# 리스트 요소 한줄로 출력
##    classifier = print(*temp)

# join 함수로 리스트 요소 하나의 문자열로 합치기
# '구분자'.join(리스트)
