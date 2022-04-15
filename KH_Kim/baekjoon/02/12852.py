## 백준 12852
## 1로 만들기 2
## 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색
from collections import deque


def makeone(N):
    count = 0
    temp = []
    while N != 1:
        temp.append(N)
        if N % 3 == 1:
            N = N - 1
            count += 1
        elif N % 3 == 0:
            N = N // 3
            count += 1
        elif N % 2 == 0:
            N = N // 2
            count += 1
        else:
            N -= 1
            count += 1

        if N == 1:
            temp.append(N)

    return count, temp


def graph(n):
    ##* 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append([n])
    answer = []

    ##* 큐가 빌 떄까지 반복
    while queue:
        ##* 큐에서 하나의 원소를 뽑기
        a = queue.popleft()
        x = a[0]
        if x == 1:
            answer = a
            break

        if x % 3 == 0:
            queue.append([x // 3] + a)

        if x % 2 == 0:
            queue.append([x // 2] + a)

        queue.append([x - 1] + a)
    return answer


if __name__ == '__main__':
    N = int(input())
    # count, temp  = makeone(N)
    # print(count)
    # print(*temp)
    answer = graph(N)

    print(len(answer) - 1)
    print(*answer[::-1])
