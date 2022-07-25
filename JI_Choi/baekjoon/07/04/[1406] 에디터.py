from sys import stdin

# 초기 편집기에 입력되어 있는 문자열 배열로 변환해서 입력받기
left_str = list(stdin.readline().strip())
right_str = []

# n 입력받기
n = int(stdin.readline())

for i in range(n):
    # 명령어 입력받기
    info = stdin.readline().strip()
    # 명령어가 'L'인 경우
    if info == 'L':
        if left_str:
            right_str.append(left_str.pop())
    # 명령어가 'D'인 경우
    elif info == 'D':
        if right_str:
            left_str.append(right_str.pop())
    # 명령어가 'B'인 경우
    elif info == 'B':
        if left_str:
            left_str.pop()
    # 명령어가 'P'인 경우
    else:
        left_str.append(info[-1])

# 편집기에 입력되어 있는 문자열 출력하기
string = left_str + right_str[::-1]
print(''.join(string))
