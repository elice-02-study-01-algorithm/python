def solution(a, b, n):
    answer = 0
    # a개를 마트에 줘야 콜라 b개 줌.. 나는 지금 n 개를 가지고 있음
    mok = 0
    while a <= n:
        mok = (n // a) * b
        answer += mok
        n = (n % a) + mok
    return answer