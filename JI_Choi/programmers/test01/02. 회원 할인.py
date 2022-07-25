def solution(want, number, discount):
    count = 0
    trigger = 0
    
    # 길이가 10인 부분 배열 안에서 확인하는 경우
    for i in(len(discount)-9):
        discount_part = discount[i:i+10]
        # 구입하고자 하는 개수와 일치하는지 확인
        for j in range(len(want)):
            if discount_part.count(want[j]) == number[j]:
                # 일치하는 경우 trigger를 1 증가
                trigger += 1
        # trigger가 want의 길이와 일치하는 경우
        if trigger == len(want):
            # count를 1 증가
            count += 1
            # trigger 초기화
            trigger = 0
        # trigger가 want의 길이와 일치하지 않는 경우
        else:
            # trigger 초기화
            trigger = 0
    
    # 길이가 10보다 작은 부분 배열 안에서 확인하는 경우
    for i in range(len(discount)-8, len(discount)):
        discount_part = discount[i:]
        # 구입하고자 하는 개수와 일치하는지 확인
        for j in range(len(want)):
            if discount_part.count(want[j]) == number[j]:
                # 일치하는 경우 trigger를 1 증가
                trigger += 1
        # trigger가 want의 길이와 일치하는 경우
        if trigger == len(want):
            # count를 1 증가
            count += 1
            # trigger 초기화
            trigger = 0
        # trigger가 want의 길이와 일치하지 않는 경우
        else:
            # trigger 초기화
            trigger = 0
    
    return count