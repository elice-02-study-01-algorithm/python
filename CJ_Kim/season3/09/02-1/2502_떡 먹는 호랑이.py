import sys
input = sys.stdin.readline
# D= 할머니가 넘어온 날, K= 호랑이에게 준 떡의 갯수
D, K = map(int, input().split())

'''
다음 처럼 날짜가 정해지면 첫째날과 둘째날에 떡의 개수에 대한 계수가 정해집니다.
사실 이 과정 없이 첫째날, 둘째날을 임의의 조합으로 브루트포스 하는 경우도 있겠지만
반드시 시간 초과가 날 것!
따라서 경우의 수를 이렇게나마 줄여줘야 함.
RC[1] = F
RC[2] = S
RC[3] = F + S
RC[4] = F + 2S
RC[5] = 2F + 3S
RC[6] = 3F + 5S
'''

# 날짜에 대한 계수 각각 구하기
def whichDay(day):
    coefficientFList = [0, 1, 0, 1]
    coefficientSList = [0, 0, 1, 1]
    for i in range(4, day+1):
        coefficientFList.append(coefficientFList[i-2] + coefficientFList[i-1])
        coefficientSList.append(coefficientSList[i-2] + coefficientSList[i-1])
    return coefficientFList[day], coefficientSList[day]

coefficientF, coefficientS = whichDay(D)

# 첫째날의 떡 개수를 1부터 K까지 냅다 때려보기
def bruteForce():
    for firstRiceCake in range(1, K):
        secondRiceCake = (K-coefficientF*firstRiceCake)/coefficientS
        if int(secondRiceCake) == secondRiceCake and firstRiceCake<=secondRiceCake:
            return firstRiceCake, int(secondRiceCake)
f, s = bruteForce()
print(f)
print(s)
'''
1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 배탈나겄어...
'''