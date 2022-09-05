'''
두 숫자형태의 문자열이 들어오는데,
두 숫자 간의 '짝꿍'이 되는 수의 최댓값을 문자열로 출력

여기서 짝꿍이란, 두 숫자간에 공통적으로 갖고 있는 수들로 만들 수 있는 수
만들 수 있는 짝꿍이 없다면, -1 출력
'''

'''
시간초과나서 70점으로 마무리
'''

## 중복값이 있어서 set을 쓰면 안됨
def solution(X, Y):
    # 입력값을 큰 수부터 정렬하는 리스트로 변환
    numX, numY = list([*X]), list([*Y])
    numX.sort(reverse=True)
    numY.sort(reverse=True)

    # 길이가 작은 것과 큰 것을 분류
    sml_list = numX if len(numX)<=len(numY) else numY
    lar_list = numX if sml_list==numY else numY

    # 만들 수 있는 짝꿍이 없으면 미리 제거
    if set(numX) & set(numY) == set():
        return '-1'

    # similar: 짝꿍을 이루는 수, remember_index: 마지막으로 꺼내 쓴 Index 저장
    similar = ''
    remember_index = 0

    # 작은 것들을 기준으로 하나씩 꺼내서 큰 것과 비교하기
    for i in range(len(sml_list)):
        # 이전에 큰 것에서 뺀 게 있다면 그 인덱스부터 다시 검사하기
        for j in range(remember_index, len(lar_list)):

            if sml_list[i] == lar_list[j]:
                remember_index = j
                similar += sml_list[i]
                # 한 번 쓰인 것은 -1로 바꾸기
                sml_list[i], lar_list[j] = -1, -1
    
    # '0..00'이 되는 경우는 '0'으로 바꾸기
    if similar.startswith('0'):
        return '0'
    
    return similar

print(solution("100", "2345")) # "-1"
print(solution("100", "203045")) # "0" # 1 0 0 / 5 4 3 2 0 0 
print(solution("100", "123450")) # "10"
print(solution("12321", "42531")) # "321"
print(solution("5525", "1255")) # "552"
