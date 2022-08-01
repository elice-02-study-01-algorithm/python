# 상자 번호는 1부터 시작
# 보조 컨테이너 벨트는 스택
# 몇 개의 상자를 실을 수 있는지
from collections import deque
def solution(order):
    truck = []
    order = deque(order)
    main = deque([i for i in range(1, len(order) + 1)])
    sub = []
    for want in order:
        if len(main) > 0 and want == main[0]:
            truck.append(main.popleft())
        elif len(sub) > 0 and want == sub[-1]:
            truck.append(sub.pop())
        elif len(main) > 0 and want > main[0]:
            while main:
                if main[0] == want:
                    truck.append(main.popleft())
                    break
                sub.append(main.popleft())
        else:
            break

    return len(truck)

# 100점