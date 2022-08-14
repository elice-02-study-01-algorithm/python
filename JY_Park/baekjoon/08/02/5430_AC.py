from sys import stdin
input = stdin.readline
from collections import deque
t = int(input())

# R은 배열 수의 순서 뒤집, D는 첫번 째 수 버리기, 빈 배열 D 연산은 에러
for i in range(t):
    p = input().rstrip()
    n = int(input())
    sequence = deque(input().rstrip()[1:-1].split(','))

    # 이걸 안넣어주니깐 [] 들어올 때 deque([''])로 들어가서
    # 다른 방법 없을까..?
    if n == 0:
        sequence = []

    flag = 0    
    R_count = 0
    for j in p:
        if j == 'R':
            R_count += 1
        elif sequence and j == 'D':
            sequence.popleft() if R_count % 2 == 0 else sequence.pop()
        elif not sequence and j == 'D':
            flag = 1
            print('error')
            break
    if flag == 0:
        if sequence:
            if R_count % 2 != 0:
                sequence.reverse()
            print("["+",".join(sequence)+"]") 
        else:
            print('[]')

'''
[ 포인트 1 : sequence.pop(0) ]
리스트의 첫번째 값을 출력해 주는 연산입니다. 
맨뒤에 값을 빼내는 pop는 복잡도가 O(1)인데 이것은 O(N)인 이유는 맨앞에 있는 값을 출력 해주기 위해 전체 복사를 해주기 위해서 입니다.
따라서 리스트 말고 deque를 이용하면 O(1)이 나옵니다. 백준에서 이 문제도 pop이 아닌 deque로 해결해야 시간초과 오류가 나지 않습니다.

[ 포인트 2 : sequence.reverse() ]
R이 나올 때마다 reverse하면 너무 오래걸림.
따라서 R의 개수를 count 하면서 홀수 개일 땐 뒤집힌 상태니깐 pop / 짝수 개는 원상태니깐 popleft 
마지막에 홀수 개 일 때만 reverse
'''

'''
문자열 처리하던 나의 노오력
    # re = [',','[',']'] 
    # sequence_list = deque([])
    # temp = ''
    # for i in sequence:
    #     if i not in re:
    #         temp += i
    #     elif i == ',' or i == ']':
    #         sequence_list.append(temp)
    #         temp = ''
'''