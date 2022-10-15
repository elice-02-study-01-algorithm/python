from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    clothes = int(input())
    cloth_dict = {}
    for _ in range(clothes):
        cloth, type = input().split()
        if type in cloth_dict:
            cloth_dict[type] += 1
        else:
            cloth_dict[type] = 1
    # 해당 종류를 입을지 안입을지 모든 경우의 수 곱하기
    answer = 1
    for type in cloth_dict:
        answer *= cloth_dict[type] + 1
    # 알몸이 되는 경우 빼기
    print(answer - 1)
