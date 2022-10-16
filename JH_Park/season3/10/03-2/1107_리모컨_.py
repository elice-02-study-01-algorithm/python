import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken_buttons = {}
if m > 0:
    broken_buttons = set(input().split())
else:
    print(len(str(n)))
    exit(0)
# + 또는 - 로만 이동 가능한 최대 이동 회수
answer = abs(100 - n)
for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        # 번호에 부러진 버튼이 포함되어 있다면
        if num[j] in broken_buttons:
            break
    else:
         answer = min(answer, len(num) + abs(i - n))
print(answer)