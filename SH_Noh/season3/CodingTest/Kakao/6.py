import sys
sys.setrecursionlimit(10**7)

def escape(n, m, x, y, r, c, k, route):
    global answer
    # d 남 > l 서 > r 동 > u 북 순서
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    if len(route) == k:
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 1 <= nx <= n and 1 <= ny <= m:
            if d == 0:
                route.append("d")
            if d == 1:
                route.append("l")
            if d == 2:
                route.append("r")
            if d == 3:
                route.append("u")
            if (nx, ny) == (r, c) and len(route) == k:
                answer = "".join(route)
                break
            escape(n, m, nx, ny, r, c, k, route)
            route.pop()
answer = ''
def solution(n, m, x, y, r, c, k):
    global answer
    escape(n, m, x, y, r, c, k, [])
    return "impossible" if answer == '' else answer