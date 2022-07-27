def solution(X, Y):
    #숫자를 세기 위한 배열 각각 선언
    count_X = [0] * 10
    count_Y = [0] * 10
    # X 구성 숫자 세기
    for i in X:
        count_X[int(i)] += 1
    # Y 구성 숫자 세기
    for i in Y:
        count_Y[int(i)] += 1
    
    answer = ''
    # 짝꿍 만들기
    for i in range(0, 10):
        # X, Y에 공통으로 나타나는 정수인 경우
        if count_X[i] > 0 and count_Y[i] > 0:
            answer = str(i) * min(count_X[i], count_Y[i]) + answer
    # X, Y에 공통으로 나타나는 정수가 없는 경우
    if answer == '':
        return '-1'
    # X, Y에 공통으로 나타나는 정수가 0뿐인 경우
    if answer[0] == '0':
        return '0'
    
    return answer