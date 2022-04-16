# 요새푸스 한번 더!
#노송희님 하는 것을 보고 시작함.
'''
요세푸스 문제와 다르게 다음 사람을 고르기 위해서 두 숫자 a와 b를 이용한다. 현재 선택된 사람의 번호가 x라면, 다음 사람의 번호는 ax2+b mod N이 된다.

가장 처음 시작하는 사람의 번호는 0번이다. 다음 사람의 번호는 위의 식을 이용해서 고른다.

각 사람은 한 번의 기회를 더 받을 수 있다. 즉, 한 번 걸리면 술을 마시는 것이 아니고, 두 번 걸렸을 때, 술을 마시는 것이다.

만약, 어떤 사람이 세 번 걸렸다면, 그 즉시 모두 자리를 박차고 일어나 집으로 간다.

N과 a, b가 주어졌을 때, 술을 마시지 않고 집으로 가는 사람의 수를 구하는 프로그램을 작성하시오.
'''
#역시 당연히 시간초과... 흠...

def next(x):
    return (a*((x**2)%N)+b)%N

def usps_add(N):
    first = set()  #여기서 시간을 줄여야 하는데..,,,
    second = set()

    graped = b

    while True:
        if graped in second: #3번째 걸렸으니 break
            break
        elif graped in first:  
            second.add(graped) #두 번째로 걸린 사람이 넘어감.
        else:
            first.add(graped)  #처음 걸린 케이스.
        graped = next(graped) #next가 잡힘.

    return N - len(second)

while True:
    a = input()
    if a == '0':
        break
    N,a,b = map(int,a.strip().split())
    if a > N//2:
        a = a - N  #계산량을 조금이라도 줄여봅시다.
    if b > N//2:
        b = b - N  #계산량을 조금이라도 줄여봅시다.

    print(usps_add(N))


# 698253463 1 181945480  return : 698177783  --> 요런게 문제.
# 1000000000 999999999 999999999  return : 999999994 (걸리는 타겟의 수가 일방적으로 적어서 쉽게 clear)


###### 다른사람이 푼 시간효율도가 높은 코드.

# import sys
# si = sys.stdin.readline

# if __name__ == "__main__":
#     while True:
#         orders = si().split()
#         if len(orders) == 1:
#             break

#         n, a, b = map(int, orders)
        
#         flags = dict()
#         cur = 0
#         idx = 1
#         while True:
#             cur = (((a * cur) % n) * (cur % n) + b) % n
#             if cur in flags:
#                 print(n - idx + flags[cur])
#                 break
            
#             flags[cur] = idx
#             idx += 1