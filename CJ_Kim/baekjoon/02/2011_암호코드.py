# list[range(1, 27)] = ['A', 'B', 'C', ..., 'Z']
# 'BEAN' = 25114
# 25114 = "BEAAD", "YAAD", "YAN", "YKD", "BEKD", "BEAN"
# 입력: 5000자리 이하의 암호
# 출력: 나올 수 있는 해석의 가짓수%1000000
# 암호가 잘못되어 해석할 수 없는 경우 0
'''
암호가 잘못된 경우는 뭐지?
0 이하의 정수?
10012 와 같이 중간에 0이 10이나 20이 될 수 없는 경우
'''
'''
암호 = k
암호의 길이 = N
T(k, 1)=1 (if 1<=k) T(k, 1)=0 (if k==0)
T(k, 2)=2 (if 11<=k<=26) T(k, 2)=1 (if 27<=k or k==10) T(k, 2)= 0 (if k<10)
T(100, 3) = 0
T(101, 3) = 1 + 0 / T(110, 3) = 0 + 1 
T(128, 3) = 2 + 0 / T(222, 3) = 2 + 1
T(k, N) = N일 때 가짓수
T(k, N) = T(k[:-1], N-1)(if 1<=k[-1]) + T(k[:-2]N-2)(if 10<= k[-2:] <= 26)
'''

import sys

def possibleCase(k, n):

    T = [None for _ in range(n+1)]

    if int(k[0])==0:
        return 0
    else:
        T[1] = 1
    
    if n==1: return T[1]

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
