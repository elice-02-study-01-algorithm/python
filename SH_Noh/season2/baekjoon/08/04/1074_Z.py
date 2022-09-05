from sys import stdin
input = stdin.readline

N, r, c = map(int, input().split())
answer = 0
for i in range(N, 0, -1):
    mid = 2 ** (i - 1)
    end = 2 ** i
    # 1사분면
    if 0 <= r < mid and 0 <= c < mid:
        continue
    # 2사분면
    elif 0 <= r < mid and mid <= c < end:
        answer += mid * mid
        c -= mid
    # 3사분면
    elif mid <= r < end and 0 <= c < mid:
        answer += mid * mid * 2
        r -= mid
    # 4사분면
    elif mid <= r < end and mid <= c < end:
        answer += mid * mid * 3
        r -= mid
        c -= mid
        
print(answer)
