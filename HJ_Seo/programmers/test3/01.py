def solution(a, b, n):
    answer = 0
    while True:
        if n<a:
            break
        x,res = divmod(n,a)
        answer += x*b
        n = x*b+res

    return answer
