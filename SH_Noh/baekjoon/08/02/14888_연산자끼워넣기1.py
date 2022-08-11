# pypy3로 통과
# 순열 사용
from sys import stdin
from itertools import permutations
input = stdin.readline

N = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = [op_list[i] for i in range(len(op_num)) for _ in range(op_num[i])]

maximum = -1e9
minimum = 1e9

def bruteforce():
    global maximum, minimum
    for case in permutations(op, N - 1):
        sum = num[0]
        for k in range(1, N):
            if case[k - 1] == '+':
                sum += num[k]
            elif case[k - 1] == '-':
                sum -= num[k]
            elif case[k - 1] == '*':
                sum *= num[k]
            elif case[k - 1] == '/':
                sum = int(sum / num[k])

        if sum > maximum:
            maximum = sum
        if sum < minimum:
            minimum = sum
            
if __name__ == "__main__":
    bruteforce()
    print(maximum)
    print(minimum)