from sys import stdin

N = int(stdin.readline())

# sequence = [N]
def makeOne(x):
    count = {1: 0} # 1은 1을 만들기 위해 연산이 0번 필요함
    sequence = [0 for _ in range(N+1)]
    # 숫자가 커지면 recursion error
    # if x in count:
    #     return count[x]
    # else:
    #     if x % 3 == 0 and x % 2 != 0: # 3의 배수만일 때
    #         count[x] = 1 + min(makeOne(x//3), makeOne(x-1))
    #     elif x % 2 == 0 and x % 3 != 0: # 2의 배수만일 때
    #         count[x] = 1 + min(makeOne(x//2), makeOne(x-1))
    #     elif x % 2 == 0 and x % 3 == 0: # 6의 배수일 때
    #         count[x] = 1 + min(makeOne(x//3), makeOne(x//2), makeOne(x-1))
    #     else: # -1만 가능할 때
    #         count[x] = 1 + makeOne(x-1)
    #     return count[x]

    for i in range(2, x+1):
        # -1만 가능할 때
        count[i] = 1 + count[i-1]
        sequence[i] = i-1
        if i % 3 == 0 and count[i//3] + 1 < count[i]: # 3의 배수이고 -1의 경우보다 작을 때
            count[i] = 1 + count[i//3]
            sequence[i] = i//3
        if i % 2 == 0 and count[i//2] + 1 < count[i]: # 2의 배수만일 때
            count[i] = 1 + count[i//2]
            sequence[i] = i//2

    return count[N]

print(makeOne(N))