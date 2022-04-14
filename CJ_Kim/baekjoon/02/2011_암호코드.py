# list[range(1, 27)] = ['A', 'B', 'C', ..., 'Z']
# 'BEAN' = 25114
# 25114 = "BEAAD", "YAAD", "YAN", "YKD", "BEKD", "BEAN"
# 입력: 5000자리 이하의 암호
# 출력: 나올 수 있는 해석의 가짓수%1000000
# 암호가 잘못되어 해석할 수 없는 경우 0
'''
암호가 잘못된 경우는 뭐지?
0 이하의 정수?(아님)
**10012 와 같이 중간에 0이 10이나 20이 될 수 없는 경우**(매우 중요)
암호가 될 수 있는 숫자를 문자열처럼 핸들링하는 게 핵심인 것 같음
28 -> '28'로서는 해석 불가, '2', '8'로만 해석 해야함
10 -> '1', '0'으로는 해석 불가, '10'으로만 해석 해야함
'''

import sys

# k=암호, n=암호의 길이
def possibleCase(k, n):

    #T[N] : k[:N]일 때 암호가 될 수 있는 case의 수
    T = [None for _ in range(n+1)]
    
    # 첫자리가 0으로 시작할 때
    if int(k[0])==0:
        return 0
    else:
        T[1] = 1
    
    # 왜 여기서 조건문으로 나눴나면, 일단 메모이제이션을 위해 T[1]을 기록해야함과 동시에
    # 길이가 1, 2인 경우 아래 for문을 돌리지 않기 위함

    if n==1: return T[1]

    # 암호가 두 자리일 때
    # 1-i) 10, 20  => T[N] = 1
    # 1-ii) 30, 40, ..., 90 => T[N] = 0
    # 2) 27, 28, 29, 31, 32, ..., 99 => T[N] = 1
    # 3) 11, 12, 13, ..., 19, 21, ..., 26 => T[N] = 2
    if int(k[1])==0:
        if int(k[:2])==10 or int(k[:2])==20:
            T[2] = 1
        else:
            return 0
    elif 27<=int(k[:2]):
        T[2] = 1
    else:
        T[2] = 2

    if n==2: return T[2]

    # Bottom-up 방식으로 메모이제이션 시작
    # 1) ...10, ...20 인 경우 => T[N] = T[N-2]
    # 2) ...11, ...19, ...21 인 경우 => T[N] = T[N-1] + T[N-2]
    # 3) ...1, ...2, ..., ...9인 경우 => T[N] = T[N-1]
    # 4) ...30, ...40, ..., ...90인 경우 => 암호 해석 불가
    for i in range(3, n+1):
        if int(k[(i-2):i])==10 or int(k[(i-2):i])==20:
            T[i] = T[i-2]
        elif 11<= int(k[(i-2):i])<=26:
            T[i] = T[i-1] + T[i-2]
        elif 1<=int(k[i-1]):
            T[i] = T[i-1]
        else:
            return 0
    return T[n]

secretCode = sys.stdin.readline().strip()
print(possibleCase(secretCode, len(secretCode))%1000000 if possibleCase(secretCode, len(secretCode)) != 0 else 0)
