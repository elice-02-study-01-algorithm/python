def solution(order):
    truck = []
    stack = []
    # order의 인덱스 선언
    j = 0

    # [1, 2, ... , len(order)+1]인 배열과 stack을 활용해 truck에 order과 같은 순서로 싣기
    for i in range(1, len(order)+1):
        check = 0
        # i와 order[j]가 같은 경우
        if i == order[j]:
            # 트럭에 싣기
            truck.append(i)
            # order의 index를 1 증가
            j += 1
            check = 1
        # stack의 원소가 order와 다를 때까지 트럭에 싣기
        while True:
            # stack이 비어있는 경우
            if stack == []:
                break
            # stack에 원소가 존재하는 경우
            else:
                # stack의 마지막 원소가 order[j]와 같은 경우
                if stack[-1] == order[j]:
                    # 트럭에 싣기
                    truck.append(stack.pop())
                    # order의 index를 1 증가
                    j += 1
                # stack의 마지막 원소가 order[j]와 같지 않은 경우
                else:
                    break
        # i를 트럭에 싣지 못한 경우
        if check == 0:
            # stack에 i 추가하기
            stack.append(i)
    # 짐 싣기에 성공한 상자 개수 구하기
    return len(truck)