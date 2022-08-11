from sys import stdin

# 초기 편집기에 입력되어 있는 문자열 배열로 변환해서 입력받기
arr = list(stdin.readline().strip())
# n 입력받기
n = int(stdin.readline())

# index 초기설정 (단, 0 <= index <= d)
index = len(arr)

for i in range(n):
    # 명령어 입력받기
    info = stdin.readline().strip()
    # 명령어가 'L'인 경우
    if info == 'L':
        # index 범위를 벗어난 경우
        if index == 0:
            continue
        # index 1 감소
        index -= 1
    # 명령어가 'D'인 경우
    elif info == 'D':
        # index 범위를 벗어난 경우
        if index == len(arr):
            continue
        # index 1 증가
        index += 1
    # 명령어가 'B'인 경우
    elif info == 'B':
        # index가 0인 경우
        if index == 0:
            continue
        # index에 해당되는 문자 삭제
        del arr[index]
        index -= 1
    # 명령어가 'P'인 경우
    else:
        if index < len(arr):
            arr.insert(index-1, info[-1])
            index += 1
        else:
            arr.append(info[-1])
            index += 1

print(''.join(arr))
