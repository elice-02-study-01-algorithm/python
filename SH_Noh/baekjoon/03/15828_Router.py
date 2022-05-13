from sys import stdin
from collections import deque

input = stdin.readline
N = int(input()) # 라우터 크기, 라우터보다 더 많은 패킷이 들어오려고 하면 버려짐
# 양의 정수 : 입력 패킷 | 0 : 처리한 패킷 | -1 : 입력의 끝

packet = deque()
while True:
    tmp = int(input())
    if tmp == -1:
        break
    elif tmp == 0:
        packet.popleft()
    else:
        if len(packet) < N:
            packet.append(tmp)
        else:
            pass

if len(packet) == 0:
    print("empty")
else:
    print(*packet, sep = ' ')