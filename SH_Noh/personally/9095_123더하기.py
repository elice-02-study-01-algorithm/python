from sys import stdin

case = {1:1, 2:2, 3:4} # 각각 n이 1, 2, 3일 때
def add123(n):
    global case
    if n in case:
        return case[n]
    case[n] = add123(n-1) + add123(n-2) + add123(n-3)
    return case[n] # 1, 2, 3을 더해서 n이 되는 경우의 수

# case = [0, 1, 2, 4]
T = int(stdin.readline())
for i in range(T):
    n = int(stdin.readline())
    print(add123(n))