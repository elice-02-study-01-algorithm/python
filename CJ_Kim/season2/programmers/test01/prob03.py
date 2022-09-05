'''
택배 상하차 중 메인 컨테이너는 물품이 1부터 N개까지의 상자를 순서대로 갖다 준다.
서브 컨테이너는 stack 형태로 작동된다.

주어지는 상자 리스트대로 택배 차에 넣고자 할 때,
택배 차에 넣을 수 있는 상자의 개수?
'''

'''
아래 코드로는 100점 만점에 10점!
'''
'''
from collections import deque

def solution(order):
    main_container = deque([i for i in range(1, len(order)+1)])
    sub_container = deque([])

    send_box = 0
    
    for i in order:
        if len(sub_container)>0 and len(main_container)>0 and i != sub_container[-1] and i != main_container[0]:
            break
        if len(sub_container)>0 and i == sub_container[-1]:
            sub_container.pop()
            send_box += 1
        else:
            while True:
                if len(main_container) == 0:
                    break
                if i == main_container[0]:
                    main_container.popleft()
                    send_box += 1
                    break
                else:
                    sub_container.append(main_container.popleft())

    return send_box

print('solution is', solution([4, 3, 1, 2, 5])) # 2
print('solution is', solution([5, 4, 3, 2, 1])) # 5
print('solution is', solution([5, 3, 4, 2, 1])) # 1
print('solution is', solution([2, 4, 5, 3, 1])) # 5
'''

'''
종료 후 다시 풀어서 test case는 맞췄습니다.
'''
def solution(order):

    total_size = len(order)

    # main_container는 한 번 나오면 더 이상 되돌아가지 않으므로 integer로 관리 가능
    main_container = 1
    # sub_container는 stack으로 관리
    sub_container = []
    # 전체 order의 index
    index = 0
    # 상자 count
    result = 0

    while True:
        # sub_container에 아무것도 없고 main의 첫번째도 일치하지 않으면 sub에 넣어주기
        if len(sub_container) == 0 and main_container != order[index]:
            sub_container.append(main_container)
            main_container += 1
        # sub_container 마지막의 상자와 order가 일치하면 상자 보내기
        elif order[index] == sub_container[-1]:
            sub_container.pop()
            index += 1
            result += 1
            # 끝까지 보내면 탈출시키기
            if index == total_size:
                break
        # main_container 첫번째 상자와 order가 일치하면 상자 보내기
        elif order[index] == main_container:
            index += 1
            main_container += 1
            result += 1
        # 아무것도 일치하지 않으면 sub에 넣어주기
        else:
            # 끝까지 아무것도 없으면서 main_container가 초과했을 때 탈출시키기
            if main_container>total_size:
                break
            sub_container.append(main_container)
            main_container += 1

    return result

print('solution is', solution([4, 3, 1, 2, 5])) # 2
print('solution is', solution([5, 4, 3, 2, 1])) # 5
print('solution is', solution([5, 3, 4, 2, 1])) # 1
print('solution is', solution([2, 4, 5, 3, 1])) # 5